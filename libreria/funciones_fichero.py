from libreria.jugador import jugador
from pathlib import Path
from libreria.estadisticas import estadisticas
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
                    jugador_actual = jugador(
                        nombre_jugador=f["Player"],
                        temporada=f["Season"],
                        competicion=f["Competition"],
                        jornada=f["Matchday"],
                        fecha=f["Date"],
                        sede=f["Venue"],
                        club=f["Club"],
                        equipo_rival=f["Opponent"],
                        resultado_partido=f["Result"],
                        posicion=f["Playing_Position"],
                        minuto=f["Minute"],
                        marcador=f["At_score"],
                        tipo=f["Type"],
                        asistente_gol=f["Goal_assist"],
                    )

                    jugador_lista.append(jugador_actual)

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


# ====================================#
# FUNCIONES PREPACION DE DATOS Y Normalizacion
# =======================================##

# Columna competiciones normalizada

Competicione_normalizada = {  # por medio de diccionario
    "Champions League": "UEFA Champions League",
    "Troph\ufffde des Champions": "Trophée des Champions",
}


def normalizar_competicion(nombre: str) -> str:  # tratamos las competiciones
    nombre = nombre.strip()  # eliminamos los espacios
    return Competicione_normalizada.get(nombre, nombre)


def obtener_partido_jugador(listado: list[jugador], nombre: str) -> list[jugador]:
    partido = []

    for listado in listado:
        if listado.get_nombre_jugador().strip() == nombre:
            valor = (listado.get_fecha(), listado.get_equipo_rival().strip())
            if valor not in partido:
                partido[valor] = listado

    return list(partido.values())



def contar_partido_competicion(partido: list[jugador]) -> dict:
    contador = {}

    for partido in partido:
        competicion = normalizar_competicion(partido.get_competicion())
        contador[competicion] = contador.get(competicion, 0) + 1
    return dict(sorted(contador.items(), key=lambda x: x[1], reverse=True))


def contador_temporada(partido: list[jugador]) -> dict:
    temporada = {}
    for partido in partido:
        temporada.add(
            partido.get_temporada().strip()
        )  # otenemos la temporada y la añadimos a la lista
    return len(temporada)


def partido_victoria(partido: list[jugador]) -> bool:
    marcador = partido.get_resultado_partido().strip()[0]
    local, visitante = marcador.split(":")
    local = int(local)
    visitante = int(visitante)
    if partido.get_sede().strip() == "H":
        return local > visitante
    return visitante > local


def contador_victoria(
    partido: list[jugador],
) -> int:  # Por cada victoria que tenga el fichero el contador aumentara
    victorias = 0
    for partido in partido:
        if partido_victoria(partido):
            victorias += 1
    return victorias

def contar_partido_ganado(partido:contar_partido_competicion)-> int:
    contador = 0
    for partido in partido:
        if partido_victoria(partido):
            contador += 1
    return contador


def contador_partido_club(
    partido: list[jugador],
) -> dict:  # Esta función contara cada partido segun el club
    contador = {}

    for partido in partido:
        club = partido.get_club().split()
        contador[club] = contador.get(club, 0) + 1
    return contador


def contar_partido_rival(partido: list[jugador]) -> dict:
    contador = {}

    for partido in partido:
        equipo_rival = partido.get_equipo_rival().strip()
        contador[equipo_rival] = contador.get(equipo_rival, 0) + 1
    return contador


###
# ==================================================================|
# CRAMOS LAS ESTADISTICAS ANTES DE MOSTRALAS EN MOSTRAR_ESTADISTICAS|
# ==================================================================|
# ##############3

def crear_estadisticas(partido: list[jugador], nombre: str) -> estadisticas:
    partido = obtener_partido_jugador(partido, nombre)

    return estadisticas(
        nombre,
        contar_partido_competicion(partido),
        contador_temporada(partido),
        contador_victoria(partido),
