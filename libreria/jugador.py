class jugador:

    # Constructor de la c
    def __init__(self, idjugador, nombre, apellido, liga, gole, posicion):
        self.__idjugador = idjugador
        self.__nombre = nombre
        self.__apellido = apellido
        self.__liga = liga
        self.__gole = gole
        self.__posicion = posicion

    #   # METODOS GETTERS Y SETTERS

    def get_id(self):
        return self.__idjugador

    def set_id(self, idjugador):
        if isinstance(idjugador, int):
            self.__idjugador = idjugador

    def get_nombre(self):
        return self.__nombre

    def set_titulo(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre

    def get_apellido(self):
        return self.__apellido

    def set_apellido(self, apellido):
        if isinstance(apellido, str):
            self.__apellido = apellido

    def get_liga(self):
        return self.__liga

    def set_liga(self, liga):
        if isinstance(liga, float, int):
            self.__liga = liga

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

    def get_categoria_precio(self):
        if self.__precio <= 20:
            return "Economico"
        elif self.__precio <= 40:
            return "Medio"
        return "Caro"

    def get_nivel_dedicacion(self):
        if self.__horas_jugadas <= 50:
            return "Casual"
        elif self.__horas_jugadas <= 150:
            return "Habitual"
        return "Experto"

    def __str__(
        self,
    ):  # Con este metodo imprimiremos la información del objeto videojuego sin necesitar de otro metodo
        return f"Jugador:ID{self.__idjugador}|Nombre:{self.__nombre}|Apellido:{self.__apellido}|Liga{self.__liga}|Goles{self.__gole}|Posicion{self.__posicion}"
