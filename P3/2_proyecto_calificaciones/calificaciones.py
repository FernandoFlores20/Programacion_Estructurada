import mysql.connector
from mysql.connector import Error

def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input(f"\n\t\t\U0001F552 Oprima cualquier tecla pra continuar ...")

def menu_principal():
    print(F"\n\t\t\t\u2B50 Gestion de Calificaciones \u2B50\n\n\t1\uFE0F\u20E3\tAgregar\n\t2\uFE0F\u20E3\tMostrar\n\t3\uFE0F\u20E3\tCalcular Promedios\n\t4\uFE0F\u20E3\tSalir")
    opcion=input(f"\t\t\U0001F4DD Elige una opcion: ").upper()
    return opcion

def conectar():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_calificaciones"
        )
        return conexion
    except Error as e:
        print(f"El error que se presenta es: {e}")
        return None

def agregarCalif(lista):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
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
        cursor=conexionBD.cursor()
        sql="insert into calificaciones ( nombre, calif1, calif2, calif3) values ( %s, %s, %s, %s)"
        for i in range(0,len(lista)):
            val=(lista[i][0],lista[i][1],lista[i][2],lista[i][3])
        cursor.execute(sql,val)
        conexionBD.commit()
        print("\n\t\t :::¡LA OPERACION SE REALIZÓ CON EXÍTO! :::")

def mostrarCalif(lista):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
      cursor=conexionBD.cursor()
      sql="select * from calificaciones"
      cursor.execute(sql)
      registros=cursor.fetchall()
      print("\n\t .:: Mostrar calificaciones ::.\n")
      if registros:
        print(f"\n\tMostrar las calificaciones")
        print(f"{'ID':<10}{'Nombre':<15}{'Calif 1':<15}{'Calif 2':<15}{'Calif 3':<15}{'Promedio':<15}")
        print(f"-"*80)
        for fila in registros:
          promedio=(fila[2]+fila[3]+fila[4])/3
          print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}")
        print(f"-"*80)

def calcularCalif(lista):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        cursor=conexionBD.cursor()
        sql="select * from calificaciones"
        cursor.execute(sql)
        registros=cursor.fetchall()
        print("\n\t .:: Calcular promedios ::.\n")
        if registros:
            for fila in registros:
                promedio=(fila[2]+fila[3]+fila[4])/3
                print(f"\n\t\t\t\u2705 Alumno: {fila[1]}")
                print(f"\t\t\t\u2705 Promedio: {promedio:.2f}")
        else:
            print("\t\t\t\u274C No hay calificaciones para calcular")
        espereTecla()