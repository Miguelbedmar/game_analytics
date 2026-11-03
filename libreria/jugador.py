from datetime import date
from dataclasses import dataclass
@dataclass
class jugador:
    __nombre_jugador:str
    # Constructor de la c
    def __init__(
        self,
        nombre_jugador:str,
        temporada:str,
        competicion:str,
        jornada:str,
        fecha: date,
        sede:str,
        club:str,
        equipo_rival:str,
        resultado_partido,
        posicion,
        minuto,
        marcador,
        tipo,
        asistente_gol,
    ):
        self.__nombre_jugador = nombre_jugador
        self.__temporada = temporada
        self.__competicion = competicion
        self.__jornada = jornada
        self.__fecha = fecha
        self.__sede = sede
        self.__club = club
        self.__equipo_rival = equipo_rival
        self.__resultado_partido = resultado_partido
        self.__posicion = posicion
        self.__minuto = minuto
        self.__marcador = marcador
        self.__tipo = tipo
        self.__asistente_gol = asistente_gol

    #   # METODOS GETTERS Y SETTERS

    def get_jugador_partida(self):
        return self.__nombre_jugador

    def set_jugador_partida(self, nombre_jugador):
        if isinstance(nombre_jugador, str):
            self.__nombre_jugador = nombre_jugador

    def get_temporada(self):
        return self.__temporada

    def set_temporada(self, temporada):
        if isinstance(temporada, str):
            self.__temporada = temporada

    def get_posicion(self):
        return self.__posicion

    def set_posicion(self, posicion):
        if isinstance(posicion, float):
            self.__posicion = posicion

        ## def get_categoria_precio(self):
        ##   if self.__precio <= 20:
        ##     return "Economico"
        ##elif self.__precio <= 40:
        ##  return "Medio"
        ##return "Caro"

        ## def get_nivel_dedicacion(self):
        ## if self.__horas_jugadas <= 50:
        ## return "Casual"
        ##elif self.__horas_jugadas <= 150:
        ##return "Habitual"
        ##   return "Experto"

    def __str__(
        self,
    ):  # Con este metodo imprimiremos la información del objeto videojuego sin necesitar de otro metodo
        return f"Jugador: Nombre:{self.__nombre}|Apellido:{self.__apellido}|Liga{self.__liga}|Goles{self.__gole}|Posicion{self.__posicion}"
