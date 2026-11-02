import jugador


def cargarArchivoCsv(ruta: str) -> list[jugador]:
    jugadorLista = []
    archivoCsv = Path(ruta.strip())
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


def transformarArchivo(juegos: list[jugador]) -> None:
    if not juegos:
        print("ERROR! Debes cargar un archivo!")
        return
    ruta = input("Ingrese la ruta de exportación del nuevo fichero")
    directori = Path(ruta) if ruta else directorio_Datos

    if not directori.is_dir():
        print("El directorio no existe")
        return
    destino_Fichero = directori / fichero_Salida
    with destino_Fichero.open("w", newline="", encoding="utf-8") as f:
        escrito = csv.writer(f)
        escrito.writerow(
            [
                "id",
                "titulo",
                "genero",
                "precio",
                "horas_jugadas",
                "valoracion",
                "categoria_precio",
                "nivel_dedicacion",
            ]
        )
        for j in juegos:
            escrito.writerow(
                [
                    j.get_id(),
                    j.get_titulo(),
                    j.get_genero(),
                    j.get_precio(),
                    j.get_horasJugadas(),
                    j.get_valoracion(),
                    j.get_categoria_precio(),
                    j.get_nivel_dedicacion(),
                ]
            )
        print(f"Fichero exportado en : {destino_Fichero} correctamente")
