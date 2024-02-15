import os
import random
import keyboard
import readchar


class Juego:
    def __init__(self, carpeta_mapas, pos_inicial, pos_final):
        self.pos_inicial = pos_inicial
        self.pos_final = pos_final

        # Obtener la lista de archivos en la carpeta de mapas
        lista_archivos = os.listdir(carpeta_mapas)

        # Seleccionar aleatoriamente un archivo de la lista
        archivo_mapa = random.choice(lista_archivos)

        # Construir la ruta completa al archivo del mapa
        ruta_mapa = os.path.join(carpeta_mapas, archivo_mapa)

        # Leer el contenido del archivo del mapa
        with open(ruta_mapa, 'r') as file:
            self.mapa = [list(linea.strip()) for linea in file]

    def limpiar_y_mostrar_matriz(self, px, py):
        # Limpiar la pantalla
        os.system('cls' if os.name == 'nt' else 'clear')

        # Copiar el mapa para no modificar el original
        mapa_mostrar = [fila[:] for fila in self.mapa]

        # Colocar al jugador en el mapa
        mapa_mostrar[py][px] = 'P'

        # Mostrar el mapa
        for fila in mapa_mostrar:
            print(' '.join(fila))

    def main_loop(self):
        # Coordenadas iniciales del jugador
        px, py = self.pos_inicial

        # Mensaje de bienvenida
        print("¡Bienvenido al laberinto!")
        print("Instrucciones: Utiliza las teclas 'W', 'A', 'S', 'D' para moverte y 'Q' para salir.")

        # Solicitar al usuario que ingrese su nombre
        nombre_jugador = input("Por favor, ingresa tu nombre: ")

        # Mensaje de bienvenida con el nombre del jugador
        print(f"\n¡Hola, {nombre_jugador}! Aquí está el laberinto para que lo explores:\n")

        # Bucle principal del juego
        while True:
            # Limpiar y mostrar el mapa
            self.limpiar_y_mostrar_matriz(px, py)

            # Leer la entrada del usuario
            movimiento = None
            while movimiento not in ['w', 'a', 's', 'd', 'q']:
                try:
                    key = readchar.readkey()
                    if key == 'w':
                        movimiento = 'w'
                    elif key == 'a':
                        movimiento = 'a'
                    elif key == 's':
                        movimiento = 's'
                    elif key == 'd':
                        movimiento = 'd'
                    elif key == 'q':
                        print("Has salido del juego.")
                        return
                except:
                    pass

            # Actualizar la posición del jugador según la entrada del usuario
            if movimiento == 'w' and py > 0 and self.mapa[py - 1][px] != '#':
                py -= 1
            elif movimiento == 's' and py < len(self.mapa) - 1 and self.mapa[py + 1][px] != '#':
                py += 1
            elif movimiento == 'a' and px > 0 and self.mapa[py][px - 1] != '#':
                px -= 1
            elif movimiento == 'd' and px < len(self.mapa[0]) - 1 and self.mapa[py][px + 1] != '#':
                px += 1

            # Verificar si el jugador llegó a la salida
            if (px, py) == self.pos_final:
                # Limpiar y mostrar el mapa por última vez
                self.limpiar_y_mostrar_matriz(px, py)
                print("\n¡Felicidades, has terminado el laberinto!")
                break
class JuegoArchivo(Juego):
    def __init__(self, carpeta_mapas, pos_inicial, pos_final):
        self.carpeta_mapas = carpeta_mapas
        lista_archivos = os.listdir(carpeta_mapas)
        archivo_mapa = random.choice(lista_archivos)
        ruta_mapa = os.path.join(carpeta_mapas, archivo_mapa)
        with open(ruta_mapa, 'r') as file:
            mapa = [linea.strip() for linea in file]
            super().__init__(mapa, pos_inicial, pos_final)


# Nuevo mapa proporcionado
laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

# Ruta de la carpeta que contiene los archivos de mapas
#carpeta_mapas = os.path.join(os.path.expanduser("~"), "Desktop", "carpeta_mapas")
carpeta_mapas = 'carpeta_mapas'
# Imprime la ruta de la carpeta de mapas
print("Ruta de la carpeta de mapas:", carpeta_mapas)

# Posiciones inicial y final
pos_inicial = (1, 2)
pos_final = (19, 20)

# Crear una instancia del juego
juego = Juego(carpeta_mapas, pos_inicial, pos_final)

# Iniciar el bucle principal del juego
juego.main_loop()