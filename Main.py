import sys  # Libreria sys importada p
import csv
from libreria.videojuego import Videojuego # importamos la clase videojuego




# Función principal para gestionar fichero .csv
def menuGameAnalystic():
    videojuego=[]
    while True:
        print("<====GAME ANALYTICS===========>")
        print("<=====1. CARGAR FICHERO=========>")
        print("<=====2. MOSTRAR ESTADÍSTICAS===>")
        print("<====3.EXPORTAR CSV TRANSFORMADO=>")
        print("<====4.SALIR===================> ")
        try:
            opcionMenu = int(input("Seleccione una opción : "))

            match opcionMenu:
                case 1:
                    print(" Opcion 1")

                case 2:
                    print("Opcion 2")

                case 3:
                    print("Opcion 3")

                case 4:

                    sys.exit(0)

                case _:
                    print("Opción en desarrollo ")

        except ValueError:
            print("Valor inválido")


def cargarArchivoCsv():

    pass


def mostrarEstadisticas():
    pass


def transformarArchivo():
    pass


def main():
    menuGameAnalystic()


if __name__ == "__main__":
    main()
