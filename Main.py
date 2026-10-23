import sys  # Libreria sys importada p
import csv
from libreria.videojuego import Videojuego  # importamos la clase videojuego
from pathlib import Path  # Importamos de la librerias pathlib el objeto Path


# Función principal para gestionar fichero .csv
def menuGameAnalystic():
    videojuego = []
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
                    try:
                        ruta=input("Ingrese la ruta del archivo CSV")
                    except (OSError ,FileNotFoundError)as f :
                        print("ERROR! valor no válido",f)

                case 2:
                    print("Opcion 2")

                case 3:
                    print("Opcion 3")

                case 4:

                    sys.exit(0)

                case _:
                    print("Opción no válida ")

        except ValueError as e:
            print("Valor inválido" ,e)

#Función que  pedira y comproborara la ruta.
def cargarArchivoCsv(ruta:str):
    while True:

        try:

            break
        except PermissionError as p:
            print("!ERROR:", p)


def mostrarEstadisticas():
    while True:
        try:

            break
        except FileNotFoundError as e:
            print("!ERROR:", e)


def transformarArchivo():
    while True:
        try:

            break
        except FileNotFoundError as e:
            print("!ERROR:", e)


def main():
    menuGameAnalystic()


if __name__ == "__main__":
    main()
