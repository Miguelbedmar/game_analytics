import sys
def menuGameAnalystic():

    while True:
        print(f"<====GAME ANALYSTICS===========>")
        print(f"<=====1. CARGAR FICHERO=========>")
        print(f"<=====2. MOSTRAR ESTADÍSTICAS===>")
        print(f"<====3.EXPORTAR CV TANRFORMADO=>")
        print(f"<====4.SALIR===================>")
        try:
            opcionMenu = int(input(f"Seleccione una opción"))

            match opcionMenu:
                case 1: print("")

                case 2:print("")

                case 3: print("")

                case 4: sys.exit(0) 

                case _: print(f"Opción en desarrollo")  

        except ValueError:
            print(f"Valor inválido")



def main():
        menuGameAnalystic()

if __name__ == "__main__":
    main()
