def mostrar_menu_juegos():
    from . import juegos
    from . import ruleta
    from . import tragaperras
    from . import baccarat
    from . import blackjack
    from . import poker
    import globales

    # Colores y estilos
    GOLD = "\033[38;5;220m"
    BLACK = "\033[30m"
    WHITE = "\033[97m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    dinero = globales.dinero_cliente
    opcion = True

    def banner_juegos():
        print(f"{BLACK}{GOLD}{BOLD}")
        print(f"{BOLD}╔{'═' * 46}╗")
        print(f"{BOLD}║{' ' * 46}║")
        print(f"║{WHITE}{GOLD}{BOLD}{'🎲  JUEGOS DE CASINO  🎲'.center(44)}{RESET}{GOLD}{BOLD}║")
        print(f"{BOLD}║{' ' * 46}║")
        print(f"{BOLD}╚{'═' * 46}╝{RESET}")

    while opcion:
        blackjack.borrarPantalla()
        banner_juegos()
        print(f"{WHITE}{BOLD}Dinero disponible: {GOLD}${dinero}{RESET}")
        print(f"{GOLD}{BOLD}" + "-" * 46 + f"{RESET}")
        print(f"{WHITE}{BOLD}¿Qué quiere jugar el día de hoy?")
        print(f"{GOLD}{BOLD}  1.{WHITE}{BOLD} Blackjack")
        print(f"{GOLD}{BOLD}  2.{WHITE}{BOLD} Ruleta")
        print(f"{GOLD}{BOLD}  3.{WHITE}{BOLD} Tragaperras")
        print(f"{GOLD}{BOLD}  4.{WHITE}{BOLD} Baccarat")
        print(f"{GOLD}{BOLD}  5.{WHITE}{BOLD} Salir{RESET}")
        print(f"{GOLD}{BOLD}" + "-" * 46 + f"{RESET}")
        opcion = input(f"{WHITE}{BOLD}Elige una opción: {RESET}").strip()
        match opcion:
            case "1":
                dinero = blackjack.blackjack(dinero)
                globales.id_juego = 1
                juegos.espereTecla()
            case "2":
                dinero = ruleta.ruleta(dinero)
                globales.id_juego = 3
                juegos.espereTecla()
            case "3":
                dinero = tragaperras.tragaperras(dinero)
                globales.id_juego = 4
                juegos.espereTecla()
            case "4":
                dinero = baccarat.baccarat(dinero)
                globales.id_juego = 5
                juegos.espereTecla()
            case "5":
                print(f"\n{GOLD}{BOLD}Gracias por jugar. ¡Hasta luego!{RESET}")
                opcion = False
            case _:
                print(f"\n{GOLD}{BOLD}Opción inválida, vuelva a intentarlo.{RESET}")
                juegos.espereTecla()
    globales.dinero_cliente = dinero