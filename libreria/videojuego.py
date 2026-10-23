class Videojuego:

    # Constructor de la c
    def __init__(self, id, titulo, genero, precio, horas_jugadas, valoracion):
        self.__id = id
        self.__titulo = titulo
        self.__genero = genero
        self.__precio = precio
        self.horas_jugadas = horas_jugadas
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
        if isinstance(precio, float):
            self.__precio = precio

    def get_horasJugadas(self):
        return self.__horas_jugadas

    def set_horasJugadas(self, horas_jugadas):
        if isinstance(horas_jugadas, int):
            self.__horas_jugadas = horas_jugadas

    def get_valoracion(self):
        return self.__valoracion

    def set_valoracion(self, valoracion):
        if isinstance(valoracion, float):
            self.__valoracion = valoracion
