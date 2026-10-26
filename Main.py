import sys  # Libreria sys importada p
import csv
from libreria.videojuego import Videojuego  # importamos la clase videojuego
from pathlib import Path  # Importamos de la librerias pathlib el objeto Path
import logging

#====================================##
# OTRAS FUNCIONES
#================================= #


# Función principal para gestionar fichero .csv
def menuGameAnalystic():
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
                        EOFError
                    ) :  # utiliando as  podemos colocarle un alias a cualquier excepcion
                        logging.error('Ha ocurrido un error! Acceso mas alla del fichero')
                        
                    except PermissionError:
                        raise PermissionError(
                            " ERROR! El fichero no tiene suficientes permisos"
                        )
                    except TypeError :
                        raise TypeError("ERROR! Se ha detectado un argumento inválido")

                    except ValueError:
                        raise ValueError("Error! Has ingresado  un valor inválido")
                case 2:
                    print("Opcion 2")

                case 3:
                    print("Opcion 3")

                case 4:
                    logging.info('Has salido  el programa....')
                    sys.exit(0)

                case _:
                    print("Opción no válida ")

        except ValueError:
            raise ValueError("ERROR!: El valor ingresado no es válido.")


# Función que  pedira y comproborara la ruta.
def cargarArchivoCsv(ruta: str) -> list[Videojuego]:
    videojuegoLista = []
    archivoCsv = Path(ruta.strip())
    try:
        if (
            not archivoCsv.is_file()
        ):  # Raise es equivalente a throws en java por lo tanto podemos personalizar excepciones
            raise FileNotFoundError(f"ERROR! El archivo no existe en {archivoCsv}")
            # Con un mensaje para cada uno
        if (
            archivoCsv.suffix.lower() != ".csv"
        ):  # Comprobamos si la extensión del archivo es csv
            raise ValueError("ERROR! El fichero debe tener extensión .csv")
        with archivoCsv.open("r", newline="", encoding="utf-8") as fichero:
            dato = csv.DictReader(fichero)

            for f in dato:
                try:
                    precioValido = float(f["precio"])
                except ValueError:
                    raise ValueError("ERROR: El precio contiene valores no válidos.")
                juegoActual = Videojuego(
                    id=int(f["id"]),
                    titulo=str(f["titulo"]),
                    genero=str(f["genero"]),
                    precio=precioValido,
                    horas_jugadas=int(f["horas_jugadas"]),
                    valoracion=float(f["valoracion"]),
                )
                videojuegoLista.append(juegoActual)

    except PermissionError as p:
        print(p)
    return videojuegoLista


def mostrarEstadisticas():

    try:

        print()

    except FileNotFoundError as e:
        print("ERROR: No existe el fichero indicado")


def transformarArchivo():
    while True:
        try:

            break
        except FileNotFoundError as e:
            print(e)


def main():
    menuGameAnalystic()


if __name__ == "__main__":
    main()
