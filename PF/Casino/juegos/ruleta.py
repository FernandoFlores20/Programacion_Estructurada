import random
import time

GOLD = "\033[38;5;220m"
BLACK = "\033[30m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"

def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input(f"\n{WHITE}{BOLD}\t... Oprima cualquier tecla para continuar ...{RESET}")

def animarRuleta(color_ganador, numero_ganador):
    print(f"\n{GOLD}{BOLD}Girando la ruleta...{RESET}")
    for i in range(20):  # Número de vueltas visuales
        numero = random.randint(0, 37)
        color = "🔴" if numero % 2 == 0 else "⚫"
        if numero == 37:
            display = "00"
        else:
            display = str(numero)
        print(f"\r{BOLD}{color} {display} {RESET}", end="", flush=True)
        time.sleep(0.1)
        if i == 19:
            borrarPantalla()
            print(f"\n{GOLD}{BOLD}Número ganador: {color_ganador} {numero_ganador}{RESET}")
    print()

def ruleta(dinero):
    borrarPantalla()
    volver="s"
    color_ganador=""
    color=""
    docena=8
    par_non=""
    par_ganador=""
    mitad=0
    mitad_ganador=""
    apuesta=1
    numero_ganador=0
    docena_ganadora=0
    def banner_ruleta():
        print(f"{BLACK}{GOLD}{BOLD}")
        print(f"{BOLD}╔{'═' * 46}╗")
        print(f"{BOLD}║{' ' * 46}║")
        print(f"║{WHITE}{GOLD}{BOLD}{'🎡  RULETA  🎡'.center(44)}{RESET}{GOLD}{BOLD}║")
        print(f"{BOLD}║{' ' * 46}║")
        print(f"{BOLD}╚{'═' * 46}╝{RESET}")

    print(f"{WHITE}{BOLD}")
    banner_ruleta()
    print(f"{WHITE}{BOLD}Bienvenido al juego de ruleta{RESET}")
    while apuesta<=dinero and apuesta>0 and volver=="s" and dinero>0:
        while True:
            try:
                borrarPantalla()
                banner_ruleta()
                print(f"{WHITE}{BOLD}Dinero disponible: {GOLD}${dinero}{RESET}")
                apuesta=float(input(f"{WHITE}{BOLD}¿Cuánto dinero quiere apostar? {RESET}"))
                if apuesta<=dinero and apuesta>0:
                    break
                else:
                    print(f"{GOLD}{BOLD}Apuesta no válida{RESET}")
            except ValueError:
                print(f"{GOLD}{BOLD}Por favor ingrese una cantidad válida{RESET}")
        borrarPantalla()
        banner_ruleta()
        print(f"{WHITE}{BOLD}Tabla de pagos en pesos mexicanos (ruleta americana):{RESET}")
        print(f"{GOLD}{BOLD}" + "=" * 60 + f"{RESET}")
        print(f"{WHITE}{BOLD}{'{:<35} {:>20}'.format('Tipo de apuesta', 'Pago por $100')}{RESET}")
        print(f"{GOLD}{BOLD}" + "-" * 60 + f"{RESET}")
        print(f"{WHITE}{BOLD}{'{:<35} {:>20}'.format('Número específico (ej. 17)', '$3500')}{RESET}")
        print(f"{WHITE}{BOLD}{'{:<35} {:>20}'.format('Color rojo o negro', '$100')}{RESET}")
        print(f"{WHITE}{BOLD}{'{:<35} {:>20}'.format('Docena (1-12, 13-24, 25-36)', '$200')}{RESET}")
        print(f"{WHITE}{BOLD}{'{:<35} {:>20}'.format('Número par o impar', '$100')}{RESET}")
        print(f"{WHITE}{BOLD}{'{:<35} {:>20}'.format('Mitades (1-18 o 19-36)', '$100')}{RESET}")
        print(f"{GOLD}{BOLD}" + "=" * 60 + f"{RESET}")
        tipo_de_apuesta=input(f"{WHITE}{BOLD}Seleccione su tipo de apuesta\n1.-Un número\n2.- Rojo o negro\n3.-Una docena\n4.-Par o impar\n5.-Mitades \n6.-Salir\n{RESET}").strip()
        numero_ganador = random.randint(0, 37)
        match numero_ganador: 
            case 1 | 3 | 5 | 7 | 9 | 12 | 14 | 16 | 18 | 19 | 21 | 23 | 25 | 27 | 30 | 32 | 34 | 36:
                color_ganador="🔴"
            case 2 | 4 | 6 | 8 | 10 | 11 | 13 | 15 | 17 | 20 | 22 | 24 | 26 | 28 | 29 | 31 | 33 | 35:
                color_ganador="⚫"
            case 0:
                color_ganador="ninguno"
        match tipo_de_apuesta:
            case "1":
                while True:
                    borrarPantalla()
                    banner_ruleta()
                    try:
                        numero=int(input(f"{WHITE}{BOLD}¿A qué número quiere apostar? (0-36){RESET}"))
                        if 0 <= numero <= 36:
                            break
                        else:
                            print(f"{GOLD}{BOLD}Número no válido, por favor ingrese un número entre 0 y 36{RESET}")
                    except ValueError:
                        print(f"{GOLD}{BOLD}Por favor ingrese un número válido{RESET}")
                animarRuleta(color_ganador, numero_ganador)
                if numero==numero_ganador:
                    print(f"{GOLD}{BOLD}Felicidades usted ganó {apuesta*35}{RESET}")
                    dinero=dinero+apuesta*35
                    espereTecla()
                else:
                    print(f"{GOLD}{BOLD}Lastima{RESET}")
                    dinero=dinero-apuesta
                    espereTecla()
            case "2":
                while color!="rojo" and color!="negro":
                    borrarPantalla()
                    banner_ruleta()
                    color=input(f"{WHITE}{BOLD}¿A qué color quiere apostar? (Rojo/Negro){RESET}").lower().strip()
                if color=="rojo":
                    color="🔴"
                elif color=="negro":
                    color="⚫"
                animarRuleta(color_ganador, numero_ganador)
                if color==color_ganador:
                    print(f"{GOLD}{BOLD}Felicidades usted ganó {apuesta*2}{RESET}")
                    dinero=dinero+apuesta*2
                    color=""
                    espereTecla()
                else:
                    print(f"{GOLD}{BOLD}Lastima{RESET}")
                    color=""
                    dinero=dinero-apuesta
                    espereTecla()
            case "3":
                while True:
                    try:
                        borrarPantalla()
                        banner_ruleta()
                        docena=int(input(f"{WHITE}{BOLD}¿A qué docena quiere apostar?\n1.-1–12\n2.-13–24\n3.-25–36{RESET}"))
                        if 1 <= docena <= 3:
                            break
                        else:
                            print(f"{GOLD}{BOLD}Docena no válida, por favor ingrese un número entre 1 y 3{RESET}")
                    except ValueError:
                        print(f"{GOLD}{BOLD}Por favor ingrese un número válido{RESET}")
                match numero_ganador:
                    case 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12:
                        docena_ganadora=1
                    case 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24:
                        docena_ganadora=2
                    case 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | 33 | 34 | 35 | 36:
                        docena_ganadora=3
                borrarPantalla()
                banner_ruleta()
                animarRuleta(color_ganador, numero_ganador)
                if docena_ganadora==docena:
                    print(f"{WHITE}{BOLD}En la docena {docena_ganadora}{RESET}")
                    print(f"{GOLD}{BOLD}Felicidades usted ganó {apuesta*3}{RESET}")
                    dinero=dinero+apuesta*3
                    docena=8
                    espereTecla()
                else:
                    print(f"{WHITE}{BOLD}En la docena {docena_ganadora}{RESET}")
                    print(f"{GOLD}{BOLD}Lastima{RESET}")
                    dinero=dinero-apuesta
                    docena=8
                    espereTecla()
            case "4":
                while par_non !="par" and par_non !="non":
                    borrarPantalla()
                    banner_ruleta()
                    par_non=input(f"{WHITE}{BOLD}¿A qué quiere apostar? (par/non){RESET}").lower().strip()
                animarRuleta(color_ganador, numero_ganador)
                if numero_ganador%2 ==0:
                    par_ganador="par"
                else:
                    par_ganador="non"
                if par_non==par_ganador:
                    print(f"{WHITE}{BOLD}El número ganador es {par_ganador}{RESET}")
                    print(f"{GOLD}{BOLD}Felicidades usted ganó {apuesta*2}{RESET}")
                    dinero=dinero+apuesta*2
                    par_non=""
                    espereTecla()
                else:
                    print(f"{WHITE}{BOLD}El número ganador es {par_ganador}{RESET}")
                    print(f"{GOLD}{BOLD}Lastima{RESET}")
                    dinero=dinero-apuesta
                    par_non=""
                    espereTecla()
            case "5":
                while mitad !="1" and mitad !="2":
                    borrarPantalla()
                    banner_ruleta()
                    mitad=input(f"{WHITE}{BOLD}¿A qué quiere apostar?\n1.-Primera mitad (1-18)\n2.-Segunda mitad (19-36){RESET}").lower().strip()
                borrarPantalla()
                banner_ruleta()
                animarRuleta(color_ganador, numero_ganador)
                if numero_ganador>=1 and numero_ganador<=18:
                    mitad_ganador="1"
                else:
                    mitad_ganador="2"
                if mitad==mitad_ganador:
                    print(f"{WHITE}{BOLD}En la mitad {mitad_ganador}{RESET}")
                    print(f"{GOLD}{BOLD}Felicidades usted ganó {apuesta*2}{RESET}")
                    dinero=dinero+apuesta*2
                    mitad=""
                    espereTecla()
                else:
                    print(f"{WHITE}{BOLD}En la mitad {mitad_ganador}{RESET}")
                    print(f"{GOLD}{BOLD}Lastima{RESET}")
                    dinero=dinero-apuesta
                    mitad=""
                    espereTecla()
            case "6":
                volver="n"
            case _:
                print(f"{GOLD}{BOLD}Opción no válida, por favor ingrese una opción válida{RESET}")
    if dinero<=0:
        borrarPantalla()
        banner_ruleta()
        print(f"{GOLD}{BOLD}No tiene dinero suficiente para jugar{RESET}")
    return dinero