import sys  # Libreria sys importada p
import csv

from libreria.jugador import jugador
from libreria.funciones_fichero import (
    cargarArchivoCsv,
    mostrarEstadisticas,
)  # Importamos las dos funciones que necesitamos
from pathlib import Path  # Importamos de la librerias pathlib el objeto Path
from getpass import getuser

# Variables de ruta
directorio_Datos = Path(__file__).resolve().parent /"datos"/ "data.csv"

directorio_str=str(directorio_Datos)


fichero_cargado=cargarArchivoCsv(directorio_Datos)

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
def menuGameAnalystic():
    juegos: list[jugador] = []
    juegos = cargarArchivoCsv(fichero_cargado)

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
                opcion_Menu = int(input("Seleccione una opción : "))
            except ValueError:
                print("Debes de ingresar un numero")
                continue
            match opcion_Menu:
                case 1:

                    
                    print(f"El archivo {len(juegos)} se ha cargado correctamente.")

                case 2:
                    mostrarEstadisticas(juegos)
                case 3:
                    print("Has salido del programa...")
                    sys.exit(0)
                    

                case _:
                    print("Opción no válida ")

        except ValueError:
            print("Error! Has ingresado  un valor inválido")


# Función que  pedira y comproborara la ruta.


def main():
    menuGameAnalystic()


if __name__ == "__main__":
    main()
