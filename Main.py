import sys  # Libreria sys importada p
import csv
from libreria.jugador import jugador
from libreria.funciones_fichero import cargarArchivoCsv,mostrarEstadisticas,transformarArchivo  # importamos la clase videojuego
from pathlib import Path  # Importamos de la librerias pathlib el objeto Path

# Variables de ruta
directorio_Datos = Path(__file__).parent / "datos"
fichero_Salida = "jugadores_transformado.csv"


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
    while True:  
        print("<=={0:^25}==>".format("GAME ANALYSTIC")) # Indicamos el numero de espaciado 
        print("<=={0:^25}==>".format("1. CARGAR FICHERO"))
        print("<=={0:^25}==>".format("2. MOSTRAR ESTADÍSTICAS"))
        print("<=={0:^25}==>".format("3.EXPORTAR CSV TRANSFORMADO"))
        print("<=={0:^25}==>".format("4.SALIR"))
        try:
            try:
                opcion_Menu = int(input("Seleccione una opción : "))
            except ValueError:
                print("Debes de ingresar un numero")
                continue
            match opcion_Menu:
                case 1:
                    try:
                        ruta = input("Ingrese la ruta del archivo CSV ")
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
                    mostrarEstadisticas(juegos)
                case 3:
                    transformarArchivo(juegos)

                case 4:
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
