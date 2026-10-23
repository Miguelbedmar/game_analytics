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

                    except (
                        EOFError,ValueError,FileNotFoundError,
                    ) as i:  # utiliando as  podemos colocarle un alias a cualquier excepcion

                        print("ERROR! Has accedido al final del archivo", i)

                case 2:
                    print("Opcion 2")

                case 3:
                    print("Opcion 3")

                case 4:

                    sys.exit(0)

                case _:
                    print("Opción no válida ")

        except (ValueError, EOFError,TypeError) as e:
            print("Valor inválido", e)


# Función que  pedira y comproborara la ruta.
def cargarArchivoCsv(ruta: str) -> list[Videojuego]:

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
        with archivoCsv.open(
            "r", newline="", encoding="utf-8"
        ) as fichero:
            dato = csv.DictReader(fichero)
            for f in dato:
                
                print(f)

    except (PermissionError,EOFError,TypeError) as p:
        print("!ERROR: falta de permisos en el ficero", p)


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
