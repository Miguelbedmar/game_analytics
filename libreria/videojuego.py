class Videojuego:

    # Constructor de la c
    def __init__(self, id, titulo, genero, precio, horas_jugadas, valoracion):
        self.__id = id
        self.__titulo = titulo
        self.__genero = genero
        self.__precio = precio
        self.__horas_jugadas = horas_jugadas
        self.__valoracion = valoracion

    # GETTERS Y SETTERS

    def get_id(self):
        return self.__id

    def set_id(self, id):
        if isinstance(id, int):
            self.__id = id

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        if isinstance(titulo, str):
            self.__titulo = titulo

    def get_genero(self):
        return self.__genero

    def set_genero(self, genero):
        if isinstance(genero, str):
            self.__genero = genero

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        if isinstance(precio, float,int):
            self.__precio = precio

    def get_horasJugadas(self):
        return self.__horas_jugadas

    def set_horasJugadas(self, horas_jugadas):
        if isinstance(horas_jugadas, int,float):
            self.__horas_jugadas = horas_jugadas

    def get_valoracion(self):
        return self.__valoracion

    def set_valoracion(self, valoracion):
        if isinstance(valoracion, float):
            self.__valoracion = valoracion

    def get_categoria_precio(self):
        if self.__precio <= 20:
            return "Economico"
        elif self.__precio <= 40:
            return "Medio"
        return "Caro"
        # METODOS
    def get_nivel_dedicacion(self):
        if self.__horas_jugadas <= 50:
            return "Casual"
        elif self.__horas_jugadas <= 150:
            return "Habitural"
        return "Experto"

    def __str__(
        self,
    ):  # Con este metodo imprimiremos la información del objeto videojuego sin necesitar de otro metodo
        return f"Videojuegos:ID{self.__id}|Nombre:{self.__titulo}|Genero:{self.__genero}|Precio{self.__precio}|Horas Jugadas{self.__horas_jugadas}|Valoracion{self.__valoracion}"
