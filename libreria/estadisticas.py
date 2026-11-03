from libreria import jugador


class estadisticas(jugador):
    def __init__(
        self,
        partido_totale,
        cantidad_aparece_jugador,
        numero_temporada,
        partido_ganado_equipo,
        gole_totale,
        porcentaje_victoria,
        cantidad_vece_rival,
    ):
        super().__ini__()
        self.partido_totale = partido_totale
        self.cantidad_aparece_jugador = cantidad_aparece_jugador
        self.numero_temporada = numero_temporada
        self.partido_ganado_equipo = partido_ganado_equipo
        self.gole_totale = gole_totale
        self.porcentaje_victoria = porcentaje_victoria
        self.cantidad_vece_rival = cantidad_vece_rival
