import mysql.connector
from mysql.connector import Error

def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            database='isaui',
            user='tu_usuario',
            password='tu_contraseña'
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
            return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
