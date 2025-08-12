import random

def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input(f"\n\t... Oprima cualquier tecla pra continuar ...")

def poker(dinero):
    mas_apuesta=1
    borrarPantalla()
    print("Bienvenido al juego de Ultimate texas hold em")
    apuesta=input("Cuanto quiere apostar")
    palos = ['Tréboles', 'Picas', 'Corazones', 'Diamantes']
    valores = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    # Crear lista de cartas
    cartas_lista = []
    for i in range(52):
        palo = palos[i // 13]
        valor = valores[i % 13]
        cartas_lista.append({'valor': valor, 'palo': palo})
    random.shuffle(cartas_lista)
    cartas_jugador=(cartas_lista[0], cartas_lista[1])
    print("Sus cartas:\n")
    for carta in cartas_jugador:
        print(f"  {carta['valor']} de {carta['palo']}")
    while mas_apuesta !=3 and mas_apuesta!=4:
        mas_apuesta=int(input("¿Quiere aumentar su apuesta? (x3/x4)"))
    apuesta=apuesta*mas_apuesta
    print(apuesta)
    espereTecla()
    cartas_comunitarias=(cartas_lista[2:7])
    print("El flop es:\n")
    for carta in cartas_comunitarias[:3]:
        print(f"  {carta['valor']} de {carta['palo']}")
    cartas_dealer=(cartas_lista[7],cartas_lista[8])
    
    print(cartas_dealer)
    #Evaluar manos
    # Ahora puedes acceder así:
    #print(cartas_lista[0]['palo'])  # Tréboles
    #print(cartas_lista[0]['valor']) # As
        