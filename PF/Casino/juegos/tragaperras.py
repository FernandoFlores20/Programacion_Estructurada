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

def tragaperras(dinero):
    jugar="1"
    inicial=dinero
    ganancias=0
    contadorGlobal = {
            "contadorTiradas": 0,
            "contador1Cerezas": 0,
            "contador2Cerezas": 0,
            "contador3Cerezas": 0,
            "contadorBar1": 0,
            "contadorBar2": 0,
            "contadorBar3": 0,
            "contadorBarMezcla": 0,
            "contadorCampana": 0,
            "contadorLimon": 0,
            "contadorNaranja": 0,
            "contadorUva": 0,
            "contadorSiete": 0,
            "contadorPerdidas": 0
        }
    while jugar != "" and jugar !="no": 
        borrarPantalla()   
        print(f"{BLACK}{GOLD}{BOLD}Bienvenido al juego de tragaperras{RESET}")
        print(f"{GOLD}{BOLD}Tabla de pagos en pesos mexicanos (máquina de 3 carretes):{RESET}")
        print(f"{GOLD}{BOLD}" + "=" * 55 + f"{RESET}")
        print(f"{WHITE}{BOLD}{'{:<30} {:>20}'.format('Combinación', 'Pago en pesos')}{RESET}")
        print(f"{GOLD}{BOLD}" + "-" * 55 + f"{RESET}")
        print(f"{WHITE}{BOLD}{'{:<40} {:>25}'.format('3 Sietes (7️⃣ 7️⃣ 7️⃣)', '$500')}{RESET}")
        print(f"{WHITE}{BOLD}{'{:<40} {:>25}'.format('3 Campanas (🔔 🔔 🔔)', '$200')}{RESET}")
        print(f"{WHITE}{BOLD}{'{:<40} {:>25}'.format('3 BAR triples (🄱🄰🅁X3)', '$150')}{RESET}")
        print(f"{WHITE}{BOLD}{'{:<40} {:>25}'.format('3 BAR doble (🄱🄰🅁X2)', '$100')}{RESET}")
        print(f"{WHITE}{BOLD}{'{:<40} {:>25}'.format('3 BAR simple (🄱🄰🅁)', '$50')}{RESET}")
        print(f"{WHITE}{BOLD}{'{:<40} {:>25}'.format('Cualquier combinación de BAR', '$25')}{RESET}")
        print(f"{WHITE}{BOLD}{'{:<40} {:>25}'.format('3 Cerezas (🍒 🍒 🍒)', '$40')}{RESET}")
        print(f"{WHITE}{BOLD}{'{:<40} {:>25}'.format('2 Cerezas (🍒 🍒)', '$15')}{RESET}")
        print(f"{WHITE}{BOLD}{'{:<40} {:>25}'.format('1 Cereza (🍒)', '$5')}{RESET}")
        print(f"{WHITE}{BOLD}{'{:<40} {:>25}'.format('3 Limones (🍋 🍋 🍋)', '$30')}{RESET}")
        print(f"{WHITE}{BOLD}{'{:<40} {:>25}'.format('3 Naranjas (🍊 🍊 🍊)', '$30')}{RESET}")
        print(f"{WHITE}{BOLD}{'{:<40} {:>25}'.format('3 Uvas (🍇 🍇 🍇)', '$30')}{RESET}")
        print(f"{GOLD}{BOLD}" + "=" * 55 + f"{RESET}")
        jugar=input(f"{WHITE}{BOLD}Cada tirada cuesta $5\n¿Quiere empezar a jugar? (Pulse ENTER para jugar, 'no' para salir) Dinero disponible: {GOLD}${dinero}{RESET} ").lower().strip()
        while jugar=="" and dinero>=5:
            ganado = 0
            contadorGlobal["contadorTiradas"] += 1
            borrarPantalla()
            jugar="1"
            dinero=dinero-5
            #el juego da mucho dinero, se debe ajustar las probabilidades
            numeros = random.sample(range(1, 21), 20)
            iconos = ["🍒", "🍋", "🍊", "🍇", "🔔", "🄱🄰🅁", "🄱🄰🅁x2", "🄱🄰🅁x3", "7️⃣"]
            iconos_no_cereza = random.sample(iconos[1:9], 3)
            bar_mezcla = random.sample(iconos[5:8], 3)  # Mezclar los iconos de BAR
            carrete1=numeros[0]
            carrete2=numeros[1]
            carrete3=numeros[2]
            #debuguear
            # carrete1=17
            # carrete2=17
            # carrete3=17
            if ((carrete1>=5) and (carrete2>=5) and (carrete3>=1 and carrete3 <=4) or ((carrete1>=1 and carrete1 <=4)) and (carrete2>=5) and (carrete3>=5) or ((carrete1>=5)) and (carrete2>=1 and carrete2 <=4) and (carrete3>=5)):
                carrete1=iconos[0]
                carrete2=iconos_no_cereza[0]
                carrete3=iconos_no_cereza[0]
                dinero=dinero+1
                ganado += 1
                contadorGlobal["contador1Cerezas"] += 1
            elif ((carrete1>=5) and (carrete2>=1 and carrete2 <=4) and (carrete3>=1 and carrete3 <=4) or ((carrete1>=1 and carrete1 <=4)) and (carrete2>=5) and (carrete3>=1 and carrete3 <=4) or ((carrete1>=1 and carrete1 <=4)) and (carrete2>=1 and carrete2 <=4) and (carrete3>=5)):
                carrete1=iconos[0]
                carrete2=iconos[0]
                carrete3=iconos_no_cereza[0]
                dinero=dinero+5
                ganado += 5
                contadorGlobal["contador2Cerezas"] += 1
            elif (carrete1>=1 and carrete1 <=4) and (carrete2>=1 and carrete2 <=4) and (carrete3>=1 and carrete3 <=4):
                carrete1=iconos[0]
                carrete2=iconos[0]
                carrete3=iconos[0]
                dinero=dinero+20
                ganado += 20
                contadorGlobal["contador3Cerezas"] += 1
            elif (carrete1>=5 and carrete1 <=8) and (carrete2>=5 and carrete2 <=8) and (carrete3>=5 and carrete3 <=8):
                carrete1=iconos[7]
                carrete2=iconos[7]
                carrete3=iconos[7]
                dinero=dinero+150
                ganado += 150
                contadorGlobal["contadorBar3"] += 1
            elif (carrete1>=9 and carrete1 <=11) and (carrete2>=9 and carrete2 <=11) and (carrete3>=9 and carrete3 <=11):
                carrete1=iconos[6]
                carrete2=iconos[6]
                carrete3=iconos[6]
                dinero=dinero+100
                ganado += 100
                contadorGlobal["contadorBar2"] += 1
            elif (carrete1>=12 and carrete1 <=13) and (carrete2>=12 and carrete2 <=13) and (carrete3>=12 and carrete3 <=13):
                carrete1=iconos[5]
                carrete2=iconos[5]
                carrete3=iconos[5]
                dinero=dinero+50
                ganado += 50
                contadorGlobal["contadorBar1"] += 1
            elif (carrete1>=5 and carrete1 <=13) and (carrete2>=5 and carrete2 <=13) and (carrete3>=5 and carrete3 <=13):
                carrete1=bar_mezcla[0]
                carrete2=bar_mezcla[1]
                carrete3=bar_mezcla[2]
                dinero=dinero+25
                ganado += 25
                contadorGlobal["contadorBarMezcla"] += 1
            elif (carrete1>=14 and carrete1 <=16) and (carrete2>=14 and carrete2 <=16) and (carrete3>=14 and carrete3 <=16):
                carrete1=iconos[1]
                carrete2=iconos[1]
                carrete3=iconos[1]
                dinero=dinero+200
                ganado += 200
                contadorGlobal["contadorCampana"] += 1
            elif (carrete1>=17) and (carrete2>=17) and (carrete3>=17):
                carrete1=iconos[8]
                carrete2=iconos[8]
                carrete3=iconos[8]
                dinero=dinero+500
                ganado += 500
                contadorGlobal["contadorSiete"] += 1
            elif (carrete1>=18) and (carrete2>=18) and (carrete3>=18):
                carrete1=iconos[1]
                carrete2=iconos[1]
                carrete3=iconos[1]
                dinero=dinero+30
                ganado += 30
                contadorGlobal["contadorLimon"] += 1
            elif (carrete1>=19) and (carrete2>=19) and (carrete3>=19):
                carrete1=iconos[2]
                carrete2=iconos[2]
                carrete3=iconos[2]
                dinero=dinero+30
                ganado += 30
                contadorGlobal["contadorNaranja"] += 1
            elif (carrete1>=20) and (carrete2>=20) and (carrete3>=20):
                carrete1=iconos[3]
                carrete2=iconos[3]
                carrete3=iconos[3]
                dinero=dinero+30
                ganado += 30
                contadorGlobal["contadorUva"] += 1
            else:
                iconos = random.sample(iconos, 3)
                carrete1=iconos[0]
                carrete2=iconos[1]
                carrete3=iconos[2]
                ganado = 0
                contadorGlobal["contadorPerdidas"] += 1
            borrarPantalla()
            print(f"\n{GOLD}{BOLD}" + "=" * 41 + f"{RESET}")
            print(f"{BLACK}{GOLD}{BOLD}||        🎰  TRAGAPERRAS           ||{RESET}")
            print(f"{GOLD}{BOLD}" + "=" * 41 + f"{RESET}")
            print(f"{BLACK}{GOLD}{BOLD}||                                   ||{RESET}")
            print(f"{BLACK}{GOLD}{BOLD}||        ┌────────────────────┐     ||{RESET}")
            print(f"{BLACK}{GOLD}{BOLD}||        │{WHITE}{carrete1}   {carrete2}   {carrete3}   {GOLD}│     ||{RESET}")
            print(f"{BLACK}{GOLD}{BOLD}||        └────────────────────┘     ||{RESET}")
            print(f"{BLACK}{GOLD}{BOLD}||                                   ||{RESET}")
            print(f"{GOLD}{BOLD}" + "=" * 41 + f"{RESET}\n")
            if ganado > 0:
                print(f"{WHITE}{BOLD}Felicidades, has ganado {GOLD}${ganado}{RESET}")
            espereTecla()
            borrarPantalla()
            while jugar != "" and jugar !="no":
                borrarPantalla()
                jugar=input(f"{WHITE}{BOLD}Cada tirada cuesta $5\n¿Quiere volver a jugar? (Pulse ENTER para jugar, 'no' para salir) Dinero disponible: {GOLD}${dinero}{RESET}").lower().strip()
        if dinero < 5:
            borrarPantalla()
            print(f"{GOLD}{BOLD}No tiene dinero suficiente para jugar{RESET}")
    borrarPantalla()
    return dinero