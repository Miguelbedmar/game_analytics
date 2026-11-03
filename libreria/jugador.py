class jugador:

    # Constructor de la c
    def __init__(self, jugador_partido, temporada, gole, posicion):
        self.__jugador_partido = jugador_partido
        self.__temporada = temporada
        self.__gole = gole
        self.__posicion = posicion

    #   # METODOS GETTERS Y SETTERS

    def get_jugador_partida(self):
        return self.__jugador_partido

    def get_gole(self):
        return self.__gole

    def set_gole(self, gole):
        if isinstance(gole, int, float):
            self.__gole = gole

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
