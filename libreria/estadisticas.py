
class estadisticas: # Creamos clase estadistica 
    # CONSTRUCTOR
    def __init__(
        self,
        nombre_jugador,
        numero_temporada,
        partidos_ganados,
        partido_competicion,
        partido_club,
        partido_rival,
    ):
        self.__nombre_jugador = nombre_jugador
        self.__numero_temporada = numero_temporada
        self.__partidos_ganados = partidos_ganados
        self.__partido_competicion = partido_competicion
        self.__partido_club = partido_club
        self.__partido_rival = partido_rival

    # METODOS GETTERS YSETTES

    def get_nombre_jugador(self):
        return self.__nombre_jugador

    def get_partidos_por_competicion(self):
        return self.__partido_competicion

    def get_numero_temporadas(self):
        return self.__numero_temporada

    def get_partidos_ganados(self):
        return self.__partidos_ganados

    def get_partidos_por_club(self):
        return self.__partido_club

    def get_partidos_por_rival(self):
        return self.__partido_rival

    def get_total_partidos(self): #Calculamos el totla de partidos por competicion
        return sum(self.__partido_competicion.values())

    def __str__(  # Con este metodo imprimiremos la información del objeto estadistica sin necesitar de otro metodo
        self,
    ):
        return (
            f"Estadisticas: {self.__nombre_jugador}|Partidos:{self.get_total_partidos()}"
            f"|Temporadas:{self.__numero_temporada}|Ganados:{self.__partidos_ganados}"
        )
