from libreria import jugador
from pathlib import Path

directorio_Datos = Path(__file__).parent / "datos"


def cargarArchivoCsv(ruta: str | Path) -> list[jugador]:
    jugadorLista = []
    archivoCsv = Path(ruta.strip)

    if isinstance(ruta, str):
        archivoCsv = Path(ruta.strip)

    else:
        archivoCsv = Path(ruta)

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
                    precio_Valido = float(f["precio"])
                except ValueError:
                    raise ValueError("ERROR: El precio contiene valores no válidos.")
                try:
                    juegoActual = Videojuego(
                        id=int(f["id"]),
                        titulo=str(f["titulo"]),
                        genero=str(f["genero"]),
                        precio=precio_Valido,
                        horas_jugadas=int(f["horas_jugadas"]),
                        valoracion=float(f["valoracion"]),
                    )

                    jugadorLista.append(juegoActual)

                except ValueError:
                    print("Error! Valores numericos no válidos en el fichero.")

    except PermissionError:
        print("ERROR! No hay suficientes permisos en el fichero.")
    return jugadorLista


def mostrarEstadisticas(juegos: list[jugador]) -> None:
    if not juegos:
        print("ERROR! Debes cargar un archivo!")
        return

    precios = [p.get_precio() for p in juegos]  # Extraemos el precio de cada juego
    Horas = [h.get_horasJugadas() for h in juegos]
    print("<========Estadísticas==============>")
    print(f"Total Videojuegos: {len(juegos)}")
    print(f"precio medio : {avg(precios):.2f} €")
    print(f"Media de horas de juego : {avg(Horas):.2f} h")
