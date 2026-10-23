import sys  # Libreria sys importada p
import csv
from libreria.videojuego import Videojuego  # importamos la clase videojuego
from pathlib import Path  # Importamos de la librerias pathlib el objeto Path

# MENSAJES DE ERROR
mensajeErrorValor = "ERROR! Valor introducido no válido"
mensajeErroFichero = "ERROR! El fichero no existe"
mensajeErrorPermisosFichero = "ERROR! Falta de permisos"
mensajeErrorTypo = "ERROR! tipo inválido"
mensajeErrorFueraFichero = "ERROR! Has accedido al final del archivo"


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
                        listaCsv = cargarArchivoCsv(ruta)
                        
                    except (
                        EOFError
                    ) as i:  # utiliando as  podemos colocarle un alias a cualquier excepcion

                        print(mensajeErrorFueraFichero, i)
                    except PermissionError as p:
                        print(mensajeErrorPermisosFichero, p)
                    except TypeError as tpE:
                        print(mensajeErrorTypo, tpE)
                case 2:
                    print("Opcion 2")

                case 3:
                    print("Opcion 3")

                case 4:

                    sys.exit(0)

                case _:
                    print("Opción no válida ")

        except (ValueError, EOFError) as e:
            print(mensajeErrorValor, e)


# Función que  pedira y comproborara la ruta.
def cargarArchivoCsv(ruta: str) -> list[Videojuego]:
    videojuegoLista = []
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
        with archivoCsv.open("r", newline="", encoding="utf-8") as fichero:
            dato = csv.DictReader(fichero)
            for f in dato:
                juego = Videojuego(
                    id=int(f["id"]),
                    titulo=str(f["titulo"]),
                    genero=str(f["genero"]),
                    precio=float(f["precio"]),
                    horas_jugadas=int(f["horas_jugadas"]),
                    valoracion=float(f["valoracion"]),
                )
            videojuegoLista.append(juego)
            print(videojuegoLista.__str__)
    except PermissionError as p:
        print(mensajeErrorPermisosFichero, p)
    except ValueError as v:
        print("", v)
    return videojuegoLista


def mostrarEstadisticas():
    
    try:
        print()


        
    except FileNotFoundError as e:
        print(e)


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
