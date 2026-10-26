import sys  # Libreria sys importada p
import csv
from libreria.videojuego import Videojuego  # importamos la clase videojuego
from pathlib import Path  # Importamos de la librerias pathlib el objeto Path

# ====================================##
# OTRAS FUNCIONES
# ================================= #


# Función principal para gestionar fichero .csv
def menuGameAnalystic():
    while True:
        print("<====GAME ANALYTICS===========>")
        print("<=====1. CARGAR FICHERO=========>")
        print("<=====2. MOSTRAR ESTADÍSTICAS===>")
        print("<====3.EXPORTAR CSV TRANSFORMADO=>")
        print("<====4.SALIR===================> ")
        print("<====seleccione una opcion======>")
        try:
            try:
                opcionMenu = int(input("Seleccione una opción : "))
            except ValueError:
                print("Debes de ingresar un numero")
                continue
            match opcionMenu:
                case 1:
                    try:
                        ruta = input("Ingrese la ruta del archivo CSV")
                        juegos = cargarArchivoCsv(ruta)
                        print(f"El archivo {len(juegos)} se ha cargado correctamente.")

                    except (
                        EOFError
                    ):  # utiliando as  podemos colocarle un alias a cualquier excepcion
                        print("ERROR! Has accedido mas alla del fichero")

                    except TypeError:
                        print("ERROR! Se ha detectado un argumento inválido")
                    except ValueError:
                        print("Error! Has ingresado  un valor inválido")
                    except FileNotFoundError:
                        print("ERROR: No existe el fichero indicado ")
                case 2:
                    print("Opcion 2")

                case 3:
                    print("Opcion 3")

                case 4:
                    print("Has salido del programa...")
                    sys.exit(0)

                case _:
                    print("Opción no válida ")

        except ValueError:
            print("Error! Has ingresado  un valor inválido")


# Función que  pedira y comproborara la ruta.
def cargarArchivoCsv(ruta: str) -> list[Videojuego]:
    videojuegoLista = []
    archivoCsv = Path(ruta.strip())
    try:
        if (
            not archivoCsv.is_file()
        ):  # Raise es equivalente a throws en java por lo tanto podemos personalizar excepciones
            raise FileNotFoundError("ERROR: No existe el fichero indicado")
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
                try:
                    juegoActual = Videojuego(
                        id=int(f["id"]),
                        titulo=str(f["titulo"]),
                        genero=str(f["genero"]),
                        precio=precioValido,
                        horas_jugadas=int(f["horas_jugadas"]),
                        valoracion=float(f["valoracion"]),
                    )

                    videojuegoLista.append(juegoActual)

                except ValueError:
                    print("Error! Valores numericos no válidos en el fichero.")

    except PermissionError:
        print("ERROR! No hay suficientes permisos en el fichero.")
    return videojuegoLista


def mostrarEstadisticas(juegos: list[Videojuego]) -> None:
    if  not juegos:
        print("ERROR! Debes cargar un archivo!")
        return

    precios=[ j.get_precio for j in juegos]
    
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
