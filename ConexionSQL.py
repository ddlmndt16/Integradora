# Importacion de base de datos
import mysql.connector

class CConexion:

    def ConexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(user='root', password='200618Rm',
                                               host='localhost',
                                               database='ProyectoSQL',
                                               port='3306')

            print("Conexión exitosa a la base de datos.")

            return conexion

        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos: {}".format(error))

            return conexion
        
    ConexionBaseDeDatos()



