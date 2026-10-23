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
                        ruta = input("Ingrese la ruta del archivo CSV")
                        cargarArchivoCsv(ruta)

                    except OSError as f:
                        # Capturamos todo caracter no válido o rutas mal formadas del sistema Operativo
                        # Con FileNotFound nos aseguramos de que el usuario ingrese un archivo por lo menos.
                        print("ERROR! valor no válido", f)

                case 2:
                    print("Opcion 2")

                case 3:
                    print("Opcion 3")

                case 4:

                    sys.exit(0)

                case _:
                    print("Opción no válida ")

        except ValueError as e:
            print("Valor inválido", e)


# Función que  pedira y comproborara la ruta.
def cargarArchivoCsv(ruta: str) -> Videojuego:
    while True:
        archivoCsv = Path(ruta.strip())
        try:
            if (
                not archivoCsv.is_file()
            ):  # Raise es equivalente a throws en java por lo tanto podemos personalizar excepciones
                raise FileNotFoundError(f"ERROR! El archivo no existe{archivoCsv}")
                # Con un mensaje para cada uno
            if (
                archivoCsv.suffix.lower() != ".csv"
            ):  # Comprobamos si la extensión del archivo es csv
                raise ValueError("ERROR! El fichero debe tener extensión .csv")
            with open("r","Videojuegos.csv",newline="", encoding="utf-8") as fichero:
                dato = csv.reader(fichero)
                for fila in dato:
                    print(fila)

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
