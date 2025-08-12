import random

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

def baccarat(dinero):
    tipo_de_apuesta=8
    volver="si"
    while volver=="si" and dinero>0:
        borrarPantalla()
        print(f"{BLACK}{GOLD}{BOLD}Bienvenido al juego de baccarat{RESET}")
        print(f"{GOLD}{BOLD}Tabla de pagos en Mini Baccarat (apuesta de $100 MXN){RESET}")
        print(f"{GOLD}{BOLD}" + "=" * 55 + f"{RESET}")
        print(f"{WHITE}{BOLD}{'{:<30} {:>20}'.format('Apuesta', 'Pago en pesos')}{RESET}")
        print(f"{GOLD}{BOLD}" + "-" * 55 + f"{RESET}")
        print(f"{WHITE}{BOLD}{'{:<30} {:>20}'.format('Jugador', '$100')}{RESET}")
        print(f"{WHITE}{BOLD}{'{:<30} {:>20}'.format('Banca', '$100')}{RESET}")
        print(f"{WHITE}{BOLD}{'{:<30} {:>20}'.format('Empate 8:1', '$800')}{RESET}")
        print(f"{GOLD}{BOLD}" + "=" * 55 + f"{RESET}")
        if dinero > 0:
            while True:
                tipo_de_apuesta=input(f"{WHITE}{BOLD}¿A qué quiere apostar?\n1.-Jugador\n2.-Banca\n3.-Empate\n4.-Salir\n{RESET}").strip()
                if tipo_de_apuesta.isdigit() and 0<int(tipo_de_apuesta)<5:
                    tipo_de_apuesta=int(tipo_de_apuesta)
                    break
                else:
                    print(f"{GOLD}{BOLD}Por favor ingrese una opción válida{RESET}")
        if tipo_de_apuesta==4:
            volver="no"
            return dinero
        while True:
            try:
                borrarPantalla()
                print(f"{WHITE}{BOLD}Dinero disponible: {GOLD}${dinero}{RESET}")
                apuesta=float(input(f"{WHITE}{BOLD}¿Cuánto quiere apostar? {RESET}"))
                if apuesta<=dinero and apuesta>=1:
                    break
            except ValueError:
                print(f"{GOLD}{BOLD}Por favor ingrese una cantidad válida{RESET}")
            else:
                print(f"{GOLD}{BOLD}Apuesta no válida{RESET}")
        borrarPantalla()
        print(f"{GOLD}{BOLD}:: Baccarat ::{RESET}\n")
        treboles = random.sample(range(1, 14), 13)
        for i in range (0,len(treboles)):
            if treboles[i]>=11:
                treboles[i]=10
        picas = random.sample(range(1, 14), 13)
        for i in range (0,len(picas)):
            if picas[i]>=11:
                picas[i]=10
        corazones = random.sample(range(1, 14), 13)
        for i in range (0,len(corazones)):
            if corazones[i]>=11:
                corazones[i]=10
        diamantes = random.sample(range(1, 14), 13)
        for i in range (0,len(diamantes)):
            if diamantes[i]>=11:
                diamantes[i]=10
        todas_las_cartas = treboles + picas + corazones + diamantes
        random.shuffle(todas_las_cartas)  
        cartas_mezcladas = tuple(todas_las_cartas)  # Convierte a tupla
        mano_jugador=(cartas_mezcladas[0]+cartas_mezcladas[2]) %10
        mano_banca=(cartas_mezcladas[1]+cartas_mezcladas[3]) %10
        print(f"{WHITE}{BOLD}Cartas jugador {cartas_mezcladas[0]} , {cartas_mezcladas[2]}\t-Resultado {mano_jugador}{RESET}")
        print(f"{WHITE}{BOLD}Cartas banca {cartas_mezcladas[1]} , {cartas_mezcladas[3]}\t-Resultado {mano_banca}{RESET}")
        espereTecla()
        if mano_jugador>=8 and mano_jugador<=9:
            print(f"{GOLD}{BOLD}Jugador gana y nadie saca más cartas{RESET}")
            if tipo_de_apuesta==1:
                print(f"{GOLD}{BOLD}Felicidades ganó {apuesta}{RESET}")
                dinero=dinero+apuesta
        else:    
            if mano_banca>=8 and mano_banca<=9:
                print(f"{GOLD}{BOLD}Banca gana y nadie saca más cartas{RESET}")
                if tipo_de_apuesta==2:
                    print(f"{GOLD}{BOLD}Felicidades ganó {apuesta}{RESET}")
                    dinero=dinero+apuesta
            else:
                if mano_jugador<=5 and mano_jugador>=0:
                    mano_jugador=(mano_jugador+cartas_mezcladas[4])%10
                    print(f"{WHITE}{BOLD}Tercer carta de jugador es {cartas_mezcladas[4]}{RESET}")
                    print(f"{WHITE}{BOLD}La mano del jugador es {mano_jugador}{RESET}")
                    espereTecla()
                elif mano_jugador==7:
                    print(f"{WHITE}{BOLD}Jugador no saca tercer carta{RESET}")
                    print(f"{WHITE}{BOLD}La mano del jugador es {mano_jugador}{RESET}")
                    espereTecla()
                if (mano_banca<=5 and mano_banca>=0) and (mano_jugador<=7 and mano_jugador>=6):
                    mano_banca=(mano_banca+cartas_mezcladas[5])%10
                    print(f"{WHITE}{BOLD}Tercer carta de banca \t{cartas_mezcladas[5]}{RESET}")
                    print(f"{WHITE}{BOLD}La mano de la banca es {mano_banca}{RESET}")
                    espereTecla()    
                elif mano_banca >=0 and mano_banca <=2:
                    mano_banca=(mano_banca+cartas_mezcladas[5])%10
                    print(f"{WHITE}{BOLD}Tercer carta de banca \t{cartas_mezcladas[5]}{RESET}")
                    print(f"{WHITE}{BOLD}La mano de la banca es {mano_banca}{RESET}")
                    espereTecla()
                elif mano_banca==3 and cartas_mezcladas[4] !=8:
                    mano_banca=(mano_banca+cartas_mezcladas[5])%10
                    print(f"{WHITE}{BOLD}Tercer carta de banca \t{cartas_mezcladas[5]}{RESET}")
                    print(f"{WHITE}{BOLD}La mano de la banca es {mano_banca}{RESET}")
                    espereTecla()
                elif (mano_banca ==4) and (cartas_mezcladas[4] >=2 and cartas_mezcladas[4]<=7):
                    mano_banca=(mano_banca+cartas_mezcladas[5])%10
                    print(f"{WHITE}{BOLD}Tercer carta de banca \t{cartas_mezcladas[5]}{RESET}")
                    print(f"{WHITE}{BOLD}La mano de la banca es {mano_banca}{RESET}")
                    espereTecla()
                elif (mano_banca ==5) and (cartas_mezcladas[4] >=4 and cartas_mezcladas[4]<=7):
                    mano_banca=(mano_banca+cartas_mezcladas[5])%10
                    print(f"{WHITE}{BOLD}Tercer carta de banca \t{cartas_mezcladas[5]}{RESET}")
                    print(f"{WHITE}{BOLD}La mano de la banca es {mano_banca}{RESET}")
                    espereTecla()
                elif (mano_banca ==6) and (cartas_mezcladas[4] >=6 and cartas_mezcladas[4]<=7):
                    mano_banca=(mano_banca+cartas_mezcladas[5])%10
                    print(f"{WHITE}{BOLD}Tercer carta de banca \t{cartas_mezcladas[5]}{RESET}")
                    print(f"{WHITE}{BOLD}La mano de la banca es {mano_banca}{RESET}")
                    espereTecla()
                elif (mano_banca==7):
                    print(f"{WHITE}{BOLD}La banca no saca tercer carta{RESET}")
                    print(f"{WHITE}{BOLD}La mano de la banca es {mano_banca}{RESET}")
                    espereTecla()
                if mano_jugador>mano_banca:
                    borrarPantalla()
                    print(f"{GOLD}{BOLD}Gana Jugador{RESET}")
                    if tipo_de_apuesta==1:
                        print(f"{GOLD}{BOLD}Felicidades ganó {apuesta}{RESET}")
                        dinero=dinero+apuesta
                    else:
                        print(f"{GOLD}{BOLD}Lastima{RESET}")
                        dinero=dinero-apuesta
                elif mano_banca>mano_jugador:
                    borrarPantalla()
                    print(f"{GOLD}{BOLD}Gana Banca{RESET}")
                    if tipo_de_apuesta==2:
                        print(f"{GOLD}{BOLD}Felicidades ganó {apuesta}{RESET}")
                        dinero=dinero+apuesta
                    else:
                        print(f"{GOLD}{BOLD}Lastima{RESET}")
                        dinero=dinero-apuesta
                elif mano_banca==mano_jugador:
                    borrarPantalla()
                    print(f"{GOLD}{BOLD}Empate{RESET}")
                    if tipo_de_apuesta==3:
                        print(f"{GOLD}{BOLD}Felicidades ganó {apuesta*8}{RESET}")
                        dinero=dinero+apuesta*8
                    else:
                        print(f"{GOLD}{BOLD}Lastima{RESET}")
                        dinero=dinero-apuesta
        volver=input(f"{WHITE}{BOLD}¿Quiere volver a jugar? (si/no){RESET}").lower().strip()
        while volver!="si" and volver!="no":
            borrarPantalla()
            volver=input(f"{WHITE}{BOLD}¿Quiere volver a jugar? (si/no){RESET}").lower().strip()
    if dinero<=0:
        borrarPantalla()
        print(f"{GOLD}{BOLD}No tiene dinero suficiente para jugar{RESET}")
    return dinero