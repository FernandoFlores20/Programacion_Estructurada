
def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input(f"\n\t\t\U0001F552 Oprima cualquier tecla pra continuar ...")

def menu_principal():
    print(F"\n\t\t\t\u2B50 Gestion de Calificaciones \u2B50\n\n\t1\uFE0F\u20E3\tAgregar\n\t2\uFE0F\u20E3\tMostrar\n\t3\uFE0F\u20E3\tCalcular Promedios\n\t4\uFE0F\u20E3\tSalir")
    opcion=input(f"\t\t\U0001F4DD Elige una opcion: ").upper()
    return opcion

def agregarCalif(lista):
    borrarPantalla()
    print("\t\t\t\U0001F4BE Agregar calificaciones \U0001F4BE")
    nombre=input("\t\t\U0001F464 Ingrese el nombre del alumnos: ").upper().strip()
    calificaciones=[]
    for i in range(1,4):
        continua=True
        while continua:
            try:
                #calificaciones.append(float(input(f"Calificacion #{i}: ")))
                cal=float(input(f"\t\t\U0001F4BE Calificacion #{i}: "))
                if cal>=0 and cal<=10:
                    calificaciones.append(cal)
                    continua=False
                else:
                    print("\t\t\t\u274C Ingresa una calificacion valida del 0 al 10")
            except ValueError:
                print("\t\t\t\u274C Ingresa un valor numerico")
    lista.append([nombre]+calificaciones)
    print("\t\t\t\u2705 Accion realizada con exito")
    print(lista)


def mostrarCalif(listas):
    borrarPantalla()
    print("\t\t\tU0001F440 Mostrar calificaciones \U0001F440")
    if len(listas)>=0:
        print(f"\t\t{'Nombre':<15}  {'Calif 1':<10}  {'Calif 2':<10}  {'Calif 3':<10}")
        print("\t\t","-"*45)
        for fila in listas:
            print(f"\t\t{fila[0]:<15}  {fila[1]:<10}  {fila[2]:<10}  {fila[3]:<10}")
        print("\t\t","-"*45)
        print("\t\t\tSon ",len(listas)," \U0001F464 Alumnos registrados")
    else:
        print("\t\t\u274C No hay calificaciones en el sistema")

def calcularCalif(lista):
        borrarPantalla()
        print("	\t\t\U0001F4CA Calificar a los Alumnos \U0001F4CA")
        if len(lista)>=0:
            print(f"\t\t{'Nombre':<15}  {'Promedio':<10} ")
            print("\t\t","-"*30)
            promedio_grupal=0
            for fila in lista:
                nombre=fila[0]
                #promedio=(fila[1]+fila[2]+fila[3])/3
                promedio=(sum(fila[1:]))/3
                print(f"\t\t{nombre:<15}  {promedio:.2f} ")
                promedio_grupal+=promedio
            print("\t\t","-"*30)
            promedio_grupal=promedio_grupal/len(lista)
            print(f"\t\t\U0001F4C2 El promedio del grupo es: {promedio_grupal:.2f}")
        else:
            print("\t\t\t\u274C No hay calificaciones en el sistema")
            

