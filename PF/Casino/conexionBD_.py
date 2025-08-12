import mysql.connector

def conectar():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_casino"
        )
        cursor=conexion.cursor(buffered=True)
        return conexion
    except:
        print(f"En este momento no posible comunicarse con el sistema, intentelo mas tarde ...")
        return None
