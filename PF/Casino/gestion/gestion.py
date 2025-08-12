'''
cliente=(
    "nombre_completo":"",
    "telefono":"",
    "domicilio":"",
    "genero":"",
    "dinero":"",
    "estatus":"",
    "membresia":"",
    )
'''

GOLD = "\033[38;5;220m"
BLACK = "\033[30m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"

import globales
import getpass
import conexionBD_
import hashlib

cliente={}
juegos={}

def hash_password(contraseña):
    return hashlib.sha256(contraseña.encode()).hexdigest()

def borrarPantalla():
    import os
    os.system("cls")

def borrarYcrear():
    borrarPantalla()
    print(f"\n{GOLD}{BOLD}:: CREAR CUENTA ::{RESET}\n")

def borrarYmodificar():
    borrarPantalla()
    print(f"\n{GOLD}{BOLD}:: MODIFICAR CUENTA ::{RESET}\n")

def borrarYcrearJuego():
    borrarPantalla()
    print(f"\n{GOLD}{BOLD}:: CREAR JUEGO ::{RESET}\n")

def borrarYmodificarJuego():
    borrarPantalla()
    print(f"\n{GOLD}{BOLD}:: MODIFICAR JUEGO ::{RESET}\n")

def espereTecla():
    input(f"\n{GOLD}{BOLD}... Oprima cualquier tecla para continuar ...{RESET}")

def crearCliente():
    borrarYcrear()
    conexionBD=conexionBD_.conectar()
    if conexionBD!=None:
        cancelar=input(f"{WHITE}{BOLD}Si no quieres crear una cuenta pulsa <Enter> para cancelar, pulsa cualquier otra tecla para continuar: ").upper().strip()
        if cancelar=="":
            print(f"\n{GOLD}{BOLD}:::¡LA OPERACION SE CANCELÓ! :::")
            return
        borrarYcrear()
        cliente.update({"nombre":input(f"{WHITE}{BOLD}Ingrese su nombre completo: {RESET}").upper()})
        while True:
            if cliente["nombre"]=="":
                borrarYcrear()
                print(f"{GOLD}{BOLD}Por favor ingrese un nombre valido{RESET}")
                cliente.update({"nombre":input(f"{WHITE}{BOLD}Ingrese su nombre completo: {RESET}").upper()})
            else:
                break
        while True:
            numero=input(f"{WHITE}{BOLD}Ingrese su numero de telefono: {RESET}")
            if numero.isdigit() and len(numero) == 10:
                cliente.update({"telefono": numero})
                break
            else:
                borrarYcrear()
                print(f"{GOLD}{BOLD}Por favor ingrese un numero de telefono valido{RESET}")
        cliente.update({"domicilio":input(f"{WHITE}{BOLD}Ingrese su domicilio: {RESET}").upper()})
        while True:
            if cliente["domicilio"]=="":
                borrarYcrear()
                print(f"{GOLD}{BOLD}Por favor ingrese un domicilio valido{RESET}")
                cliente.update({"domicilio":input(f"{WHITE}{BOLD}Ingrese su domicilio: {RESET}").upper()})
            else:
                break
        while True:
            genero=input(f"{WHITE}{BOLD}Ingrese su genero (\U0001F469 f/\U0001F9D1 m): ").lower().strip()
            if genero=="f":
                cliente.update({"genero":"FEMENINO"})
                break
            elif genero=="m":
                cliente.update({"genero":"MASCULINO"})
                break
            else:
                borrarYcrear()
                print(f"{WHITE}{BOLD}Por favor ingrese un genero valido{RESET}")
        cliente.update({"estatus": "ACTIVO"})
        while True:
            membresia=input(f"{WHITE}{BOLD}¿Quiere la membresia VIP (Costo $1500)?(\U0001F451 s/\U0001F6D1 n): {RESET}").lower().strip()
            if membresia=="s":
                cliente.update({"membresia":"VIP"})
                break
            if membresia=="n":
                cliente.update({"membresia":"ESTANDAR"})
                break
        while True:
            dinero = input(f"{WHITE}{BOLD}Ingrese el dinero que tiene: $ {RESET}")
            try:
                dinero_float = float(dinero)
                if dinero_float >= 500:
                    cliente.update({"dinero": dinero_float})
                    break
                else:
                    borrarYcrear()
                    print(f"{GOLD}{BOLD}No puede crear una cuenta con menos de $500{RESET}")
            except ValueError:
                borrarYcrear()
                print(f"{GOLD}{BOLD}Por favor ingrese una cantidad válida{RESET}")
        cliente.update({"contraseña":hash_password(getpass.getpass(f"{WHITE}{BOLD}Ingrese una contraseña: {RESET}"))})
        while True:
            if cliente["contraseña"]=="":
                borrarYcrear()
                print(f"{WHITE}{BOLD} Por favor ingrese una contraseña valida{RESET}")
                cliente.update({"contraseña":hash_password(getpass.getpass(f"{WHITE}{BOLD}Ingrese una contraseña: {RESET}"))})
            else:
                break
        cursor=conexionBD.cursor()
        sql="insert into clientes (nombre, telefono, domicilio, status, genero, membresia, dinero, contraseña) values (%s, %s, %s, %s, %s, %s, %s,%s) "
        val=(cliente["nombre"],cliente["telefono"],cliente["domicilio"],cliente["estatus"],cliente["genero"],cliente["membresia"],cliente["dinero"],cliente["contraseña"],)
        cursor.execute(sql,val)
        conexionBD.commit()
    print(f"{WHITE}{BOLD}\n\t\t .::LA OPERACION SE REALIZO CON EXITO!::.{RESET}")

def mostrarCliente():
    borrarPantalla()
    conexionBD = conexionBD_.conectar()
    if conexionBD is not None:
        cursor = conexionBD.cursor()
        sql = "select * from clientes"
        cursor.execute(sql)
        registros = cursor.fetchall()
        print(f"\n{GOLD}{BOLD}:: Mostrar clientes ::{RESET}\n")
        if registros:
            print(f"{WHITE}{BOLD}{'ID':<10}{'Nombre':<25}{'Telefono':<15}{'Domicilio':<30}{'Estatus':<15}{'Genero':<15}{'Membresia':<15}{'dinero':<15}{RESET}")
            print(f"{GOLD}{BOLD}" + "-"*135 + f"{RESET}")
            for fila in registros:
                print(f"{WHITE}{BOLD}{fila[0]:<10}{fila[1]:<25}{fila[2]:<15}{fila[3]:<30}{fila[4]:<15}{fila[5]:<15}{fila[6]:<15}{fila[7]:<15}{RESET}")
            print(f"{GOLD}{BOLD}" + "-"*135 + f"{RESET}")
        else:
            print(f"\n{GOLD}{BOLD}No hay clientes en el Sistema{RESET}")

def borrarCliente():
    borrarPantalla()
    conexionBD = conexionBD_.conectar()
    if conexionBD is not None:
        mostrarCliente()
        id = input(f"{WHITE}{BOLD}Ingrese el id del cliente a borrar o pulsa <Enter> para cancelar: {RESET}").upper().strip()
        if id == "":
            print(f"\n{GOLD}{BOLD}:::¡LA OPERACION SE CANCELÓ! :::{RESET}")
            return
        cursor = conexionBD.cursor()
        sql = "select * from clientes where id_cliente=%s"
        val = (id,)
        cursor.execute(sql, val)
        registros = cursor.fetchall()
        if registros:
            borrarPantalla()
            print(f"\n{GOLD}{BOLD}:: Borrar clientes ::{RESET}\n")
            print(f"{WHITE}{BOLD}{'ID':<10}{'Nombre':<25}{'Telefono':<15}{'Domicilio':<30}{'Estatus':<15}{'Genero':<15}{'Membresia':<15}{'dinero':<15}{RESET}")
            print(f"{GOLD}{BOLD}" + "-"*135 + f"{RESET}")
            for fila in registros:
                print(f"{WHITE}{BOLD}{fila[0]:<10}{fila[1]:<25}{fila[2]:<15}{fila[3]:<30}{fila[4]:<15}{fila[5]:<15}{fila[6]:<15}{fila[7]:<15}{RESET}")
            print(f"{GOLD}{BOLD}" + "-"*135 + f"{RESET}")
            resp = input(f"{WHITE}{BOLD}¿Deseas borrar el cliente {id}? (Si/No): {RESET}").lower().strip()
            if resp == "si":
                sql = "delete from clientes where id_cliente=%s"
                val = (id,)
                cursor.execute(sql, val)
                conexionBD.commit()
                print(f"\n{GOLD}{BOLD}:::¡LA OPERACION SE REALIZÓ CON EXÍTO! :::{RESET}")
        else:
            print(f"\n{GOLD}{BOLD}No hay clientes en el Sistema con ese id{RESET}")

def buscarCliente():
    borrarPantalla()
    conexionBD = conexionBD_.conectar()
    if conexionBD is not None:
        id = input(f"{WHITE}{BOLD}Dame el id del cliente o pulsa <Enter> para cancelar: {RESET}").upper().strip()
        if id == "":
            print(f"\n{GOLD}{BOLD}:::¡LA OPERACION SE CANCELÓ! :::{RESET}")
            return
        cursor = conexionBD.cursor()
        sql = "select * from clientes where id_cliente=%s"
        val = (id,)
        cursor.execute(sql, val)
        registros = cursor.fetchall()
        if registros:
            print(f"{WHITE}{BOLD}{'ID':<10}{'Nombre':<25}{'Telefono':<15}{'Domicilio':<30}{'Estatus':<15}{'Genero':<15}{'Membresia':<15}{'dinero':<15}{RESET}")
            print(f"{GOLD}{BOLD}" + "-"*130 + f"{RESET}")
            for fila in registros:
                print(f"{WHITE}{BOLD}{fila[0]:<10}{fila[1]:<25}{fila[2]:<15}{fila[3]:<30}{fila[4]:<15}{fila[5]:<15}{fila[6]:<15}{fila[7]:<15}{RESET}")
            print(f"{GOLD}{BOLD}" + "-"*130 + f"{RESET}")
        else:
            print(f"\n{GOLD}{BOLD}No hay clientes en el Sistema con ese id{RESET}")
    else:
        print(f"\n{GOLD}{BOLD}No hay clientes en el sistema{RESET}")

def modificarCliente():
    borrarPantalla()
    conexionBD = conexionBD_.conectar()
    if conexionBD is not None:
        mostrarCliente()
        id = input(f"{WHITE}{BOLD}Dame el id del cliente a modificar o pulsa <Enter> para cancelar: {RESET}").upper().strip()
        if id == "":
            print(f"\n{GOLD}{BOLD}:::¡LA OPERACION SE CANCELÓ! :::{RESET}")
            return
        cursor = conexionBD.cursor()
        sql = "select * from clientes where id_cliente=%s"
        val = (id,)
        cursor.execute(sql, val)
        registros = cursor.fetchall()
        if registros:
            borrarYmodificar()
            print(f"{WHITE}{BOLD}{'ID':<10}{'Nombre':<25}{'Telefono':<15}{'Domicilio':<30}{'Estatus':<15}{'Genero':<15}{'Membresia':<15}{'dinero':<15}{RESET}")
            print(f"{GOLD}{BOLD}" + "-"*135 + f"{RESET}")
            for fila in registros:
                print(f"{WHITE}{BOLD}{fila[0]:<10}{fila[1]:<25}{fila[2]:<15}{fila[3]:<30}{fila[4]:<15}{fila[5]:<15}{fila[6]:<15}{fila[7]:<15}{RESET}")
            print(f"{GOLD}{BOLD}" + "-"*135 + f"{RESET}")
            resp = input(f"{WHITE}{BOLD}¿Deseas modificar el cliente {id}? (Si/No): {RESET}").lower().strip()
            if resp == "si":
                borrarYmodificar()
                nuevo_nombre = input(f"{WHITE}{BOLD}Ingrese el nuevo nombre: {RESET}").upper()
                while nuevo_nombre == "":
                    borrarYmodificar()
                    print(f"{GOLD}{BOLD}Por favor ingrese un nombre valido{RESET}")
                    nuevo_nombre = input(f"{WHITE}{BOLD}Ingrese el nuevo nombre: {RESET}").upper()
                while True:
                    nuevo_telefono = input(f"{WHITE}{BOLD}Ingrese el nuevo telefono: {RESET}").upper().strip()
                    if nuevo_telefono.isdigit() and len(nuevo_telefono) == 10:
                        break
                nuevo_domicilio = input(f"{WHITE}{BOLD}Ingrese el nuevo domicilio: {RESET}").upper()
                while nuevo_domicilio == "":
                    borrarYmodificar()
                    print(f"{GOLD}{BOLD}Por favor ingrese un domicilio valido{RESET}")
                    nuevo_domicilio = input(f"{WHITE}{BOLD}Ingrese el nuevo domicilio: {RESET}").upper()
                while True:
                    nuevo_status = input(f"{WHITE}{BOLD}Ingrese el nuevo status: (ACTIVO/INACTIVO){RESET}").upper().strip()
                    if nuevo_status == "ACTIVO" or nuevo_status == "INACTIVO":
                        break
                while True:
                    nuevo_genero = input(f"{WHITE}{BOLD}Ingrese el nuevo genero: (M/F){RESET}").upper().strip()
                    if nuevo_genero == "M" or nuevo_genero == "F":
                        break
                while True:
                    nuevo_membresia = input(f"{WHITE}{BOLD}¿El cliente es VIP?: (S/N){RESET}").upper().strip()
                    if nuevo_membresia == "S":
                        nuevo_membresia = "VIP"
                        break
                    if nuevo_membresia == "N":
                        nuevo_membresia = "ESTANDAR"
                        break
                while True:
                    nuevo_dinero = input(f"{WHITE}{BOLD}Ingrese el dinero que tiene: ${RESET}")
                    try:
                        dinero_float = float(nuevo_dinero)
                        if dinero_float >= 0:
                            nuevo_dinero = dinero_float
                            break
                        else:
                            borrarYmodificar()
                            print(f"{GOLD}{BOLD}Por favor ingrese una cantidad válida (mayor o igual a 0){RESET}")
                    except ValueError:
                        borrarYmodificar()
                        print(f"{GOLD}{BOLD}Por favor ingrese un número válido{RESET}")
                nueva_contraseña = hash_password(getpass.getpass(f"{WHITE}{BOLD}Ingrese una nueva contraseña: {RESET}"))
                while nueva_contraseña == "":
                    borrarYmodificar()
                    nueva_contraseña = hash_password(getpass.getpass(f"{WHITE}{BOLD}Ingrese una nueva contraseña: {RESET}"))
                sql = "update clientes set nombre=%s, telefono=%s, domicilio=%s, status=%s, genero=%s, membresia=%s, dinero=%s, contraseña=%s where id_cliente=%s"
                val = (nuevo_nombre, nuevo_telefono, nuevo_domicilio, nuevo_status, nuevo_genero, nuevo_membresia, nuevo_dinero, nueva_contraseña, id)
                cursor.execute(sql, val)
                conexionBD.commit()
                print(f"\n{GOLD}{BOLD}:::¡LA OPERACION SE REALIZÓ CON EXÍTO! :::{RESET}")
        else:
            print(f"\n{GOLD}{BOLD}No hay clientes en el Sistema con ese id{RESET}")


def iniciarSesion(telefono, contraseña):
    conexionBD = conexionBD_.conectar()
    if conexionBD is not None:
        cursor = conexionBD.cursor()
        sql = "SELECT id_cliente, dinero FROM clientes WHERE telefono=%s AND contraseña=%s"
        val = (telefono, contraseña)
        cursor.execute(sql, val)
        registros = cursor.fetchall()
        if registros:
            id_cliente = registros[0][0]
            dinero = registros[0][1]
            return True, float(dinero), id_cliente
        else:
            return False,None, 0
    return False,None, 0

def actualizarDinero():
    borrarPantalla()
    conexionBD=conexionBD_.conectar()
    if conexionBD!=None:
        dinero=globales.dinero_cliente
        telefono=globales.telefono_cliente
        cursor = conexionBD.cursor()
        sql="update clientes set dinero=%s where telefono=%s"
        val=(dinero,telefono)
        cursor.execute(sql,val)
        conexionBD.commit()

def actualizarId():
    borrarPantalla()
    conexionBD=conexionBD_.conectar()
    if conexionBD!=None:
        id_cliente=globales.id_cliente
        id_juego=globales.id_juego
        cursor = conexionBD.cursor()
        sql="update juegos set id_cliente=%s where id_juego=%s"
        val=(id_cliente,id_juego)
        cursor.execute(sql,val)
        conexionBD.commit() 

def crearJuego():
    borrarYcrearJuego()
    conexionBD = conexionBD_.conectar()
    if conexionBD is not None:
        cancelar = input(f"{GOLD}{BOLD}Si no quieres crear un juego pulsa <Enter> para cancelar, pulsa cualquier otra tecla para continuar: {RESET}").upper().strip()
        if cancelar == "":
            print(f"\n{GOLD}{BOLD}:::¡LA OPERACION SE CANCELÓ! :::{RESET}")
            return
        borrarYcrearJuego()
        juegos.update({"nombre": input(f"{WHITE}{BOLD}Ingrese el nombre del juego: {RESET}").upper()})
        while juegos["nombre"] == "":
            borrarYcrearJuego()
            print(f"{GOLD}{BOLD}Por favor ingrese un nombre valido{RESET}")
            juegos.update({"nombre": input(f"{WHITE}{BOLD}Ingrese el nombre del juego: {RESET}").upper()})
        while True:
            tipo = input(f"{WHITE}{BOLD}El juego es de tipo (1.-Mesa, 2.-Maquina 3.-Cartas): {RESET}")
            match tipo:
                case "1":
                    juegos.update({"tipo": "MESA"})
                    break
                case "2":
                    juegos.update({"tipo": "MAQUINA"})
                    break
                case "3":
                    juegos.update({"tipo": "CARTAS"})
                    break
                case _:
                    print(f"{GOLD}{BOLD}Por favor ingrese un valor valido{RESET}")
        juegos.update({"descripcion": input(f"{WHITE}{BOLD}Ingrese la descripción: {RESET}")})
        while juegos["descripcion"] == "":
            borrarYcrearJuego()
            print(f"{GOLD}{BOLD}Ingrese una descripción{RESET}")
            juegos.update({"descripcion": input(f"{WHITE}{BOLD}Ingrese la descripción: {RESET}")})
        juegos.update({"estado": "ACTIVO"})
        juegos.update({"id_cliente": 1})
        cursor = conexionBD.cursor()
        sql = "insert into juegos (nombre, tipo, descripcion, estado, id_cliente) values (%s, %s, %s, %s, %s)"
        val = (juegos["nombre"], juegos["tipo"], juegos["descripcion"], juegos["estado"], juegos["id_cliente"])
        cursor.execute(sql, val)
        conexionBD.commit()
        print(f"\n{GOLD}{BOLD}::LA OPERACION SE REALIZO CON EXITO!::{RESET}")

def mostrarJuego():
    borrarPantalla()
    conexionBD = conexionBD_.conectar()
    if conexionBD is not None:
        cursor = conexionBD.cursor()
        sql = "select * from juegos"
        cursor.execute(sql)
        registros = cursor.fetchall()
        print(f"\n{GOLD}{BOLD}:: Mostrar juegos ::{RESET}\n")
        if registros:
            print(f"{WHITE}{BOLD}{'ID':<10}{'Nombre':<15}{'Tipo':<15}{'Estado':<15}{'ID Cliente':<15}{RESET}")
            print(f"{GOLD}{BOLD}" + "-"*80 + f"{RESET}")
            for fila in registros:
                print(f"{WHITE}{BOLD}{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[4]:<15}{fila[5]:<15}{RESET}")
            print(f"{GOLD}{BOLD}" + "-"*80 + f"{RESET}")
        else:
            print(f"\n{GOLD}{BOLD}No hay juegos en el Sistema{RESET}")

def borrarJuego():
    borrarPantalla()
    conexionBD = conexionBD_.conectar()
    if conexionBD is not None:
        mostrarJuego()
        id = input(f"{WHITE}{BOLD}Ingrese el id del juego a borrar o pulsa <Enter> para cancelar: {RESET}").upper().strip()
        if id == "":
            print(f"\n{GOLD}{BOLD}:::¡LA OPERACION SE CANCELÓ! :::{RESET}")
            return
        cursor = conexionBD.cursor()
        sql = "select * from juegos where id_juego=%s"
        val = (id,)
        cursor.execute(sql, val)
        registros = cursor.fetchall()
        if registros:
            borrarPantalla()
            print(f"\n{GOLD}{BOLD}:: Borrar juegos ::{RESET}\n")
            print(f"{WHITE}{BOLD}{'ID':<10}{'Nombre':<15}{'Tipo':<15}{'Estado':<15}{'ID Cliente':<15}{RESET}")
            print(f"{GOLD}{BOLD}" + "-"*80 + f"{RESET}")
            for fila in registros:
                print(f"{WHITE}{BOLD}{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[4]:<15}{fila[5]:<15}{RESET}")
            print(f"{GOLD}{BOLD}" + "-"*80 + f"{RESET}")
            resp = input(f"{WHITE}{BOLD}¿Deseas borrar el juego {id}? (Si/No): {RESET}").lower().strip()
            if resp == "si":
                sql = "delete from juegos where id_juego=%s"
                val = (id,)
                cursor.execute(sql, val)
                conexionBD.commit()
                print(f"\n{GOLD}{BOLD}:::¡LA OPERACION SE REALIZÓ CON EXÍTO! :::{RESET}")
        else:
            print(f"\n{GOLD}{BOLD}No hay juegos en el Sistema con ese id{RESET}")

def buscarJuego():
    borrarPantalla()
    conexionBD = conexionBD_.conectar()
    if conexionBD is not None:
        cursor = conexionBD.cursor()
        id = input(f"{WHITE}{BOLD}Ingrese el id del juego a buscar o pulsa <Enter> para cancelar: {RESET}").upper().strip()
        if id == "":
            print(f"\n{GOLD}{BOLD}:::¡LA OPERACION SE CANCELÓ! :::{RESET}")
            return
        sql = "select * from juegos where id_juego=%s"
        val = (id,)
        cursor.execute(sql, val)
        registros = cursor.fetchall()
        if registros:
            borrarPantalla()
            print(f"{GOLD}{BOLD}:: Buscar juegos ::{RESET}\n")
            print(f"{WHITE}{BOLD}{'ID':<10}{'Nombre':<15}{'Tipo':<15}{'Estado':<15}{'ID Cliente':<15}{RESET}")
            print(f"{GOLD}{BOLD}" + "-"*80 + f"{RESET}")
            for fila in registros:
                print(f"{WHITE}{BOLD}{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[4]:<15}{fila[5]:<15}{RESET}")
            print(f"{GOLD}{BOLD}" + "-"*80 + f"{RESET}")
        else:
            print(f"\n{GOLD}{BOLD}No hay juegos en el Sistema con ese id{RESET}")

def modificarJuego():
    borrarPantalla()
    conexionBD = conexionBD_.conectar()
    if conexionBD is not None:
        cursor = conexionBD.cursor()
        mostrarJuego()
        id = input(f"{WHITE}{BOLD}Ingrese el id del juego a modificar o pulsa <Enter> para cancelar: {RESET}").upper().strip()
        if id == "":
            print(f"\n{GOLD}{BOLD}:::¡LA OPERACION SE CANCELÓ! :::{RESET}")
            return
        sql = "select * from juegos where id_juego=%s"
        val = (id,)
        cursor.execute(sql, val)
        registros = cursor.fetchall()
        if registros:
            borrarYmodificarJuego()
            print(f"{WHITE}{BOLD}{'ID':<10}{'Nombre':<15}{'Tipo':<15}{'Estado':<15}{'ID Cliente':<15}{RESET}")
            print(f"{GOLD}{BOLD}" + "-"*80 + f"{RESET}")
            for fila in registros:
                print(f"{WHITE}{BOLD}{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[4]:<15}{fila[5]:<15}{RESET}")
            print(f"{GOLD}{BOLD}" + "-"*80 + f"{RESET}")
            nombre = input(f"{WHITE}{BOLD}Ingrese el nuevo nombre del juego: {RESET}").strip()
            tipo = input(f"{WHITE}{BOLD}Ingrese el nuevo tipo del juego: {RESET}").strip()
            descripcion = input(f"{WHITE}{BOLD}Ingrese la nueva descripcion del juego: {RESET}").strip()
            estado = input(f"{WHITE}{BOLD}Ingrese el nuevo estado del juego: {RESET}").strip()
            id_cliente = input(f"{WHITE}{BOLD}Ingrese el nuevo id del cliente: {RESET}").strip()
            sql = "update juegos set nombre=%s, tipo=%s, descripcion=%s, estado=%s, id_cliente=%s where id_juego=%s"
            val = (nombre, tipo, descripcion, estado, id_cliente, id)
            cursor.execute(sql, val)
            conexionBD.commit()
            print(f"\n{GOLD}{BOLD}:::¡LA OPERACION SE REALIZÓ CON EXÍTO! :::{RESET}")
        else:
            print(f"\n{GOLD}{BOLD}No hay juegos en el Sistema con ese id{RESET}")

def exportarClientesExcel():
    import pandas as pd
    conexionBD = conexionBD_.conectar()
    if conexionBD is not None:
        df = pd.read_sql_query("SELECT * FROM clientes", conexionBD)
        df.to_excel("Tabla_clientes.xlsx", index=False)
        borrarPantalla()
        print(f"{GOLD}{BOLD}Datos exportados a Tabla_clientes.xlsx{RESET}")
    else:
        print(f"\n{GOLD}{BOLD}No se pudo conectar a la base de datos{RESET}")

def exportarJuegosExcel():
    import pandas as pd
    conexionBD = conexionBD_.conectar()
    if conexionBD is not None:
        df = pd.read_sql_query("SELECT * FROM juegos", conexionBD)
        df.to_excel("Tabla_juegos.xlsx", index=False)
        borrarPantalla()
        print(f"{GOLD}{BOLD}Datos exportados a Tabla_juegos.xlsx{RESET}")
    else:
        print(f"\n{GOLD}{BOLD}No se pudo conectar a la base de datos{RESET}")