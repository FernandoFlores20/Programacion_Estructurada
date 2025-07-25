'''
contactos={
        "Ruben":["6181111111","ruben@gmail.com"]


}
'''

import mysql.connector
from mysql.connector import Error

def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input(f"\n\t\t\U0001F552 Oprima cualquier tecla pra continuar ...")

def menu_principal():
    print(F"\n\t\t\t\U0001F4DE Sistema de gestion de agenda de contactos  \U0001F4DE\n\n\t1\uFE0F\u20E3\tAgregar contacto \n\t2\uFE0F\u20E3\tMostrar todos los contactos\n\t3\uFE0F\u20E3\tBuscar contacto por nombre\n\t4\uFE0F\u20E3\tModificar contacto\n\t5\uFE0F\u20E3\tBorrar un contacto\n \t6\uFE0F\u20E3\tSalir")
    opcion=input(f"\t\t\U0001F4DD Elige una opcion (1-4): ").upper()
    return opcion

def conectar():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_agenda"
        )
        return conexion
    except Error as e:
        print(f"El error que se presenta es: {e}")
        return None

def agregarContac(agenda):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\t\t Agregar contactos ")
        nombre=input("Ingrese su nombre: ").upper().strip()
        telefono=input("Ingrese su numero de telefono: ").upper()
        email=input("Ingrese su correo electronico: ").lower().strip()
        agenda[nombre]=[telefono,email]
        cursor=conexionBD.cursor()
        sql="insert into agenda ( nombre, telefono, email) values ( %s, %s, %s)"
        for i in agenda:
            val=(i,agenda[i][0],agenda[i][1])
        cursor.execute(sql,val)
        conexionBD.commit()            
        print("Operacion realizada con exito")


def mostrarContac(agenda):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\t\t Mostrar contactos ")
        cursor=conexionBD.cursor()
        cursor.execute("select * from agenda")
        registros=cursor.fetchall()
        print(f"\n\t\t\t\U0001F4DE Contactos guardados en la agenda \U0001F4DE")
        print(f"-"*80)
        print(f"{'ID':<5}{'Nombre':<20}{'Telefono':<20}{'Email':<20}")
        print(f"-"*80)
        for fila in registros:
            print(f"{fila[0]:<5}{fila[1]:<20}{fila[2]:<20}{fila[3]:<20}")
        print(f"-"*80)

def buscarContac(agenda):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\t\t Buscar contacto ")
        cursor=conexionBD.cursor()
        nombre=input("Ingrese el nombre del contacto a buscar: ").upper().strip()
        cursor.execute("select * from agenda where nombre=%s", (nombre,))
        resultado=cursor.fetchone()
        if resultado:
            print(f"\n\t\t\t\U0001F4DE Contacto encontrado \U0001F4DE")
            print(f"-"*80)
            print(f"{'ID':<5}{'Nombre':<20}{'Telefono':<20}{'Email':<20}")
            print(f"-"*80)
            print(f"{resultado[0]:<5}{resultado[1]:<20}{resultado[2]:<20}{resultado[3]:<20}")
            print(f"-"*80)
        else:
            print("Contacto no encontrado")

def modificarContac(agenda):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\t\t Modificar contacto ")
        nombre=input("Ingrese el nombre del contacto a modificar: ").upper().strip()
        if nombre in agenda:
            print(f"\n\t\t\t\U0001F4DE Contacto encontrado \U0001F4DE")
            print(f"-"*80)
            print(f"{'ID':<5}{'Nombre':<20}{'Telefono':<20}{'Email':<20}")
            print(f"-"*80)
            print(f"{agenda[nombre][0]:<5}{nombre:<20}{agenda[nombre][1]:<20}")
            print(f"-"*80)
            nuevo_telefono=input("Ingrese el nuevo numero de telefono: ").upper()
            nuevo_email=input("Ingrese el nuevo correo electronico: ").lower().strip()
            agenda[nombre]=[nuevo_telefono,nuevo_email]
            cursor=conexionBD.cursor()
            sql="update agenda set telefono=%s, email=%s where nombre=%s"
            val=(nuevo_telefono,nuevo_email,nombre)
            cursor.execute(sql,val)
            conexionBD.commit()
            print("Contacto modificado con exito")
        else:
            print("Contacto no encontrado")

def borrarContac(agenda):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\t\t Borrar contacto ")
        nombre=input("Ingrese el nombre del contacto a borrar: ").upper().strip()
        if nombre in agenda:
            confirmacion=input(f"Esta seguro que desea borrar el contacto {nombre}? (S/N): ").upper().strip()
            if confirmacion != "S":
                print("Operacion cancelada")
                return
            cursor=conexionBD.cursor()
            sql="delete from agenda where nombre=%s"
            val=(nombre,)
            cursor.execute(sql,val)
            conexionBD.commit()
            del agenda[nombre]
            print("Contacto borrado con exito")
        else:
            print("Contacto no encontrado")



            
                
                
