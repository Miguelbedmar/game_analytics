import sys  # Libreria sys importada p
import csv

from libreria import jugador
from libreria.funciones_fichero import cargar_archivo_csv, mostrar_estadisticas
from pathlib import Path  # Importamos de la librerias pathlib el objeto Path
from getpass import getuser

# Variables de ruta
directorio_Datos = Path(__file__).resolve().parent / "datos" / "data.csv"


# Obtenemos el usuario del equipo utilizando la libreria getPass especificando que unicamente nos importe el metodogetUser().
usuario_ordenador = getuser()


# ====================================##
# OTRAS FUNCIONES
# ================================= #
def avg(
    valor: list[float],
) -> (
    float
):  # Definicion de la funcion avg  ya que python no tiene integrada avg() nativamente aunque podriamos utilizar otras librerias como estadictis
    if not valor:
        return 0
    return sum(valor) / len(valor)


# Función principal para gestionar fichero .csv
def menu_game_analystic():
    juegos: list[jugador] = []
    juegos = cargar_archivo_csv(directorio_Datos)

    while True:
        print(
            "<=={0:^25}==>".format("GAME ANALYSTIC")
        )  # Indicamos el numero de espaciado
        print(
            "<=={0:^25}==>".format(f"BIENVENIDO : {usuario_ordenador}")
        )  # Personalizamos  el menu saludando al usuario
        print("<=={0:^25}==>".format("1. MOSTRAR ESTADÍSTICAS CRISTIANO"))
        print("<=={0:^25}==>".format("2.MOSTRAR ESTADISTICAS MESSI"))
        print("<=={0:^25}==>".format("3.SALIR"))
        try:
            try:
                opcion_menu = int(input("Seleccione una opción : "))
            except ValueError:
                print("Debes de ingresar un numero")
                continue
            match opcion_menu:
                case 1:
                    mostrar_estadisticas(juegos)

                case 2:
                    mostrar_estadisticas(juegos)
                case 3:
                    print("Has salido del programa...")
                    sys.exit(0)

                case _:
                    print("Opción no válida ")

        except ValueError:
            print("Error! Has ingresado  un valor inválido")


# Función que  pedira y comproborara la ruta.


def main():
    menu_game_analystic()


if __name__ == "__main__":
    main()
