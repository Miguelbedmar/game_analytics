from libreria.jugador import jugador
from pathlib import Path
import csv


def cargar_archivo_csv(ruta: str | Path) -> list[jugador]:
    jugador_lista = []

    if isinstance(ruta, str):
        archivo_csv = Path(ruta.strip())

    else:
        archivo_csv = Path(ruta)

    try:
        if (
            not archivo_csv.is_file()
        ):  # Raise es equivalente a throws en java por lo tanto podemos personalizar excepciones
            raise FileNotFoundError("ERROR: No existe el fichero indicado")
            # Con un mensaje para cada uno
        if (
            archivo_csv.suffix.lower() != ".csv"
        ):  # Comprobamos si la extensión del archivo es csv
            raise ValueError("ERROR! El fichero debe tener extensión .csv")
        with archivo_csv.open("r", newline="", encoding="utf-8") as fichero:
            dato = csv.DictReader(fichero)

            for f in dato:

                try:    
                    jugador_actual=juegador()
                        

                    jugador_lista.append(juegador_actual)

                except ValueError:
                    print("Error! Valores numericos no válidos en el fichero.")

    except PermissionError:
        print("ERROR! No hay suficientes permisos en el fichero.")
    return jugador_lista


def mostrar_estadisticas(juegos: list[jugador]) -> None:
    if not juegos:
        print("ERROR! Debes cargar un archivo!")
        return

    precios = [p.get_precio() for p in juegos]  # Extraemos el precio de cada juego
    horas = [h.get_horasJugadas() for h in juegos]
    print("<========Estadísticas==============>")
    print(f"Total Videojuegos: {len(juegos)}")
    print(f"precio medio : {avg(precios):.2f} €")
    print(f"Media de horas de juego : {avg(horas):.2f} h")
