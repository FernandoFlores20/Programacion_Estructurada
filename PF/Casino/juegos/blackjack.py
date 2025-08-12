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

def blackjack(dinero):
    borrarPantalla()
    volver="s"
    print(f"{BLACK}{GOLD}{BOLD}Bienvenido al juego de blackjack{RESET}")
    cancelar=input(f"{WHITE}{BOLD}¿Quiere cancelar el juego? (Presione 'Enter' para cancelar){RESET}")
    if cancelar == "":
        volver="no"
        return dinero
    while volver=="s" and dinero>0:
        otra_carta=""
        doblar=""
        dividir=""
        uno_u_once=2
        j=4
        mano_dealer=1
        mano_jugador=1
        volver=""
        otra_carta_dividida1=""
        otra_carta_dividida2=""
        borrarPantalla()
        while True:
            try:
                borrarPantalla()
                apuesta=float(input(f"{WHITE}{BOLD}¿Cuánto quiere apostar? (Dinero disponible: {GOLD}${dinero}{WHITE}) {RESET}"))
                if apuesta > dinero:
                    print(f"{GOLD}{BOLD}No puede apostar más de lo que tiene{RESET}")
                elif apuesta <= 0:
                    print(f"{GOLD}{BOLD}No puede apostar 0 o menos{RESET}")
                else:
                    break
            except ValueError:
                print(f"{GOLD}{BOLD}Por favor ingrese una cantidad válida{RESET}")
        dinero=dinero-apuesta
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
        random.shuffle(todas_las_cartas)  # Desordena la lista
        cartas_mezcladas = todas_las_cartas
        #Cosas para alterar la baraja y debuguear
        #cartas_mezcladas[0]=10
        #cartas_mezcladas[2]=1
        # cartas_mezcladas[1]=10
        # cartas_mezcladas[3]=11
        #Fin de cosas para debugear
        #Si las 2 primeras cartas son 1
        if cartas_mezcladas[1]==1 and cartas_mezcladas[3]==1:
            cartas_mezcladas[1]=1
            cartas_mezcladas[3]=11
        if cartas_mezcladas[0]==1 and cartas_mezcladas[2]==1:
            cartas_mezcladas[0]=1
            cartas_mezcladas[2]=11
        else:
            #Si una de las primeras cartas es 1 en la mano del dealer
            if cartas_mezcladas[1]==1 or cartas_mezcladas[3]==1:
                for i in range (1,4,2):
                    if cartas_mezcladas[i]==1:
                        cartas_mezcladas[i]=11
        #Si una de las cartas del jugador es 1 se le pregunta si quiere que sea 1 u 11
        for i in range (0,4,2):
            if cartas_mezcladas[i]==1:
                while uno_u_once !=1 and uno_u_once!=11:
                    print(f"{WHITE}{BOLD}Sus cartas son: {cartas_mezcladas[0]} y {cartas_mezcladas[2]}\ttotal {mano_jugador}{RESET}")
                    uno_u_once=int(input(f"{WHITE}{BOLD}¿Quiere que su as valga 1 u 11? (1/11){RESET}"))
                    cartas_mezcladas[i]=uno_u_once
        mano_jugador=cartas_mezcladas[0]+cartas_mezcladas[2]
        mano_dealer=cartas_mezcladas[1]+cartas_mezcladas[3]
        borrarPantalla()
        print(f"{WHITE}{BOLD}Sus cartas son: {cartas_mezcladas[0]} y {cartas_mezcladas[2]}\ttotal {mano_jugador}{RESET}")
        print(f"{WHITE}{BOLD}La carta del dealer es: {cartas_mezcladas[1]}{RESET}")
        if mano_jugador==21:
            print(f"{GOLD}{BOLD}Felicidades, tiene blackjack{RESET}")
            print(f"{GOLD}{BOLD}Gana {apuesta*2.5}{RESET}")
            dinero=dinero+apuesta*2.5
        else:
            #Si las 2 primeras cartas son iguales y quiere dividir su mano
            if cartas_mezcladas[0]==cartas_mezcladas[2]:
                while dividir !="s" and dividir!="n":
                    dividir=input(f"{WHITE}{BOLD}¿Quiere dividir su mano? (s/n){RESET}").lower().strip()
                    dinero=dinero-apuesta
                    apuesta=apuesta+apuesta
                    if apuesta>dinero:
                        apuesta=apuesta-apuesta/2
                        print(f"{GOLD}{BOLD}No puede dividir su mano, no tiene suficiente dinero{RESET}")
                        print(f"{WHITE}{BOLD}Dinero {dinero}{RESET}")
                        print(f"{WHITE}{BOLD}Apuesta {apuesta}{RESET}")
                        dividir="n"
            if mano_dealer==21 and mano_jugador!=21:
                print(f"{WHITE}{BOLD}Las cartas del dealer son: {cartas_mezcladas[1]} y {cartas_mezcladas[3]}\ttotal {mano_dealer}{RESET}")
                print(f"{GOLD}{BOLD}Lastima, el dealer tiene blackjack{RESET}")
            else:
                while doblar !="s" and doblar!="n" and dividir!="s":
                    doblar=input(f"{WHITE}{BOLD}¿Quiere doblarse? (s/n){RESET}").lower().strip()
                    if doblar=="s":
                        apuesta=apuesta+apuesta
                        if apuesta>dinero:
                            i=i+1
                            apuesta=apuesta-apuesta/2
                            print(f"{GOLD}{BOLD}No puede doblar su mano, no tiene suficiente dinero{RESET}")
                            print(f"{WHITE}{BOLD}Dinero {dinero}{RESET}")
                            print(f"{WHITE}{BOLD}Apuesta {apuesta}{RESET}")
                            doblar="n"
                        else:
                            mano_jugador=mano_jugador+cartas_mezcladas[4]
                if dividir=="s":
                    j=5
                    mano_jugador_dividida1=cartas_mezcladas[4]+cartas_mezcladas[0]
                    print(f"{WHITE}{BOLD}Sus cartas en su primer mano son: {cartas_mezcladas[0]} y {cartas_mezcladas[4]}\ttotal {mano_jugador_dividida1}{RESET}")
                    print(f"{WHITE}{BOLD}La carta del dealer es: {cartas_mezcladas[1]}{RESET}")
                    while otra_carta_dividida1 !="s" and otra_carta_dividida1 !="n":
                        otra_carta_dividida1=input(f"{WHITE}{BOLD}¿Quiere otra carta en su mano 1? (s/n){RESET}").lower().strip()
                    while otra_carta_dividida1=="s" and mano_jugador_dividida1 <=21:
                        mano_jugador_dividida1=mano_jugador_dividida1+cartas_mezcladas[j]
                        print(f"{WHITE}{BOLD}Su nueva carta en su primer mano es: {cartas_mezcladas[j]} y su total es: {mano_jugador_dividida1}{RESET}")
                        j+=1
                        otra_carta_dividida1=""
                        while otra_carta_dividida1 !="s" and otra_carta_dividida1 !="n" and mano_jugador_dividida1<=21:
                            otra_carta_dividida1=input(f"{WHITE}{BOLD}¿Quiere otra carta? (s/n){RESET}").lower().strip()
                    mano_jugador_dividida2=cartas_mezcladas[2]+cartas_mezcladas[j]
                    print(f"{WHITE}{BOLD}Sus cartas en su segunda mano son: {cartas_mezcladas[2]} y {cartas_mezcladas[j]}\ttotal {mano_jugador_dividida2}{RESET}")
                    print(f"{WHITE}{BOLD}La carta del dealer es: {cartas_mezcladas[1]}{RESET}")
                    j+=1
                    while otra_carta_dividida2 !="s" and otra_carta_dividida2 !="n":
                        otra_carta_dividida2=input(f"{WHITE}{BOLD}¿Quiere otra carta en su mano 2? (s/n){RESET}").lower().strip()
                    while otra_carta_dividida2=="s" and mano_jugador_dividida2 <=21:
                        mano_jugador_dividida2=mano_jugador_dividida2+cartas_mezcladas[j]
                        print(f"{WHITE}{BOLD}Su nueva carta en su segunda mano es: {cartas_mezcladas[j]} y su total es: {mano_jugador_dividida2}{RESET}")
                        j+=1
                        otra_carta_dividida2=""
                        while otra_carta_dividida2 !="s" and otra_carta_dividida2 !="n" and mano_jugador_dividida2<=21:
                            otra_carta_dividida2=input(f"{WHITE}{BOLD}¿Quiere otra carta? (s/n){RESET}").lower().strip()
                    borrarPantalla()
                    print(f"{WHITE}{BOLD}Tu mano 1 es: {mano_jugador_dividida1}{RESET}")
                    print(f"{WHITE}{BOLD}Tu mano 2 es: {mano_jugador_dividida2}{RESET}")
                    print(f"{WHITE}{BOLD}Las cartas del dealer son: {cartas_mezcladas[1]} y {cartas_mezcladas[3]}\ttotal {mano_dealer}{RESET}")
                    while mano_dealer<17 and mano_jugador_dividida1 <= 21 and mano_jugador_dividida2 <= 21:
                        if cartas_mezcladas[j]==1:
                            cartas_mezcladas[j]=11
                            mano_dealer=mano_dealer+cartas_mezcladas[j]
                            if mano_dealer>21:
                                cartas_mezcladas[j]=1
                                mano_dealer=mano_dealer+cartas_mezcladas[j]-11
                        else:
                            mano_dealer=mano_dealer+cartas_mezcladas[j]
                        print(f"{WHITE}{BOLD}La nueva carta del dealer es: {cartas_mezcladas[j]} y su total es: {mano_dealer}{RESET}")
                        j+=1
                    if mano_jugador_dividida1 > 21:
                        print(f"{GOLD}{BOLD}Lastima perdió la mano 1{RESET}")
                    else:
                        espereTecla()
                        if (mano_jugador_dividida1 > 21) or (mano_jugador_dividida1 < mano_dealer and mano_dealer <= 21):
                            print(f"{GOLD}{BOLD}Lastima perdió la mano 1{RESET}")
                        elif mano_jugador_dividida1 > mano_dealer and mano_jugador_dividida1 <= 21 or (mano_dealer > 21 and mano_jugador_dividida1 <= 21):
                            print(f"{GOLD}{BOLD}Felicidades ganó la mano 1{RESET}")
                            dinero += apuesta
                        elif mano_jugador_dividida1 == mano_dealer:
                            print(f"{WHITE}{BOLD}Empató la mano 1{RESET}")
                            dinero += apuesta
                    if mano_jugador_dividida2 > 21:
                        print(f"{GOLD}{BOLD}Lastima perdió la mano 2{RESET}")
                    else:
                        if (mano_jugador_dividida2 > 21) or (mano_jugador_dividida2 < mano_dealer and mano_dealer <= 21):
                            print(f"{GOLD}{BOLD}Lastima perdió la mano 2{RESET}")
                        elif mano_jugador_dividida2 > mano_dealer and mano_jugador_dividida2 <= 21 or (mano_dealer > 21 and mano_jugador_dividida2 <= 21):
                            print(f"{GOLD}{BOLD}Felicidades ganó la mano 2{RESET}")
                            dinero += apuesta
                        elif mano_jugador_dividida2 == mano_dealer:
                            print(f"{WHITE}{BOLD}Empató la mano 2{RESET}")
                            dinero += apuesta
                else:
                    if mano_jugador !=21:
                        while otra_carta !="s" and otra_carta !="n" and doblar!="s":
                            otra_carta=input(f"{WHITE}{BOLD}¿Quiere otra carta? (s/n){RESET}").lower().strip()
                        while otra_carta=="s" and mano_jugador <=21:
                            i=j
                            mano_jugador=mano_jugador+cartas_mezcladas[i]
                            print(f"{WHITE}{BOLD}Su nueva carta es: {cartas_mezcladas[i]} y su total es: {mano_jugador}{RESET}")
                            j+=1
                            otra_carta=""
                            while otra_carta !="s" and otra_carta !="n" and mano_jugador<=21:
                                otra_carta=input(f"{WHITE}{BOLD}¿Quiere otra carta? (s/n){RESET}").lower().strip()
                        borrarPantalla()
                        print(f"{WHITE}{BOLD}Su nueva carta es: {cartas_mezcladas[i]} y su total es: {mano_jugador}{RESET}")
                        if mano_jugador>21:
                            print(f"{GOLD}{BOLD}Lastima{RESET}")
                        else:
                            print(f"{WHITE}{BOLD}Las cartas del dealer son: {cartas_mezcladas[1]} y {cartas_mezcladas[3]}\ttotal {mano_dealer}{RESET}")
                            while mano_dealer<17:
                                if cartas_mezcladas[j]==1:
                                    cartas_mezcladas[j]=11
                                    mano_dealer=mano_dealer+cartas_mezcladas[j]
                                    if mano_dealer>21:
                                        cartas_mezcladas[j]=1
                                        mano_dealer=mano_dealer+cartas_mezcladas[j]-11
                                else:
                                    mano_dealer=mano_dealer+cartas_mezcladas[j]
                                print(f"{WHITE}{BOLD}La nueva carta del dealer es: {cartas_mezcladas[j]} y su total es: {mano_dealer}{RESET}")
                                j+=1
                            if (mano_jugador>mano_dealer and mano_jugador<=21) or (mano_dealer>21 and mano_jugador<=21):
                                print(f"{GOLD}{BOLD}Felicidades usted gana {apuesta}{RESET}")
                                dinero=dinero+apuesta*2
                            elif mano_jugador<mano_dealer and mano_dealer<=21:
                                print(f"{GOLD}{BOLD}Lastima{RESET}")
                    
                    if mano_dealer==mano_jugador:
                        print(f"{WHITE}{BOLD}Empate{RESET}")
                        dinero=dinero+apuesta
        while volver!="s" and volver!="n":
            volver=input(f"{WHITE}{BOLD}¿Quiere volver a jugar? (s/n){RESET}").lower().strip()
    if dinero<=0:
        print(f"{GOLD}{BOLD}No tiene suficiente dinero para seguir jugando.{RESET}")
        espereTecla()
    borrarPantalla()
    return dinero