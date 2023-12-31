import mysql.connector
from mysql.connector import Error

class DAO:
    
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                database='lds_c'
            )
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    def ListarCursos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM usuarios")
                resultados = cursor.fetchall()
                cursor.close()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
