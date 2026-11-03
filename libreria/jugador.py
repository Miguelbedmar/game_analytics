from datetime import date
from datetime import time


class jugador():

    # Constructor de la c
    def __init__(
        self,
        nombre_jugador: str,
        temporada: str,
        competicion: str,
        jornada: str,
        fecha: date,
        sede: str,
        club: str,
        equipo_rival: str,
        resultado_partido,
        posicion,
        minuto: time,
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

    def get_nombre_jugador(self):
        return self.__nombre_jugador

    def get_temporada(self):
        return self.__temporada

    def get_competicion(self):
        return self.__competicion

    def get_jornada(self):
        return self.__jornada

    def get_fecha(self):
        return self.__fecha

    def get_club(self):
        return self.__club

    def get_sede(self):
        return self.__sede

    def get_equipo_rival(self):
        return self.__equipo_rival

    def get_resultado_partido(self):
        return self.__resultado_partido

    def get_posicion(self):
        return self.__posicion

    def get_minuto(self):
        return self.__minuto

    def get_marcador(self):
        return self.__marcador

    def get_tipo(self):
        return self.__tipo

    def get_asistente_gol(self):
        return self.__asistente_gol

    def __str__(
        self,
    ):  # Con este metodo imprimiremos la información del objeto videojuego sin necesitar de otro metodo
        return (
            f"Jugador: Nombre del Jugador: {self.__nombre_jugador}f|Temporada:{self.__temporada}|Competicion: {self.__competicion}",
            f"|Jornada: {self.__jornada}|Fecha:{self.__fecha}|Club: {self.__club}",
            f"|Sede:{self.__sede}|Equipo Rival : {self.__equipo_rival}| Resultado del Partido: {self.__resultado_partido}
            f"|Posicion: {self.__posicion}|Minuto: {self.__minuto}|Marcador:{self.__marcador}"
            f"|Tipo:{self.__tipo}|Asistencia: {self.__asistente_gol}"
            
            
            )
