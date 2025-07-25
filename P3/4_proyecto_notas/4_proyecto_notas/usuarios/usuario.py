from conexionBD import *
import datetime
import hashlib

def hash_password(contra):
    return hashlib.sha256(contra.encode()).hexdigest()

def registrar(nombre,apellidos,email,contra):
    try:
        fecha=datetime.datetime.now()
        contra=hash_password(contra)
        cursor.execute("insert into usuarios (nombre,apellidos,email,password,fecha) values (%s,%s,%s,%s,%s)",(nombre,apellidos,email,contra,fecha))
        conexion.commit()
        return True
    except:
        return False
    
def inicio_sesion(email,contra):
    try:
        contra=hash_password(contra)
        cursor.execute(("select*from usuarios where email=%s and password=%s"),(email,contra))
        return cursor.fetchone()
    except:
        return []
    