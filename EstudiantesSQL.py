from ConexionSQL import *

class Estudiantes:

    def ingresarEstudiante(matricula, nombre, correo, contraseña):

        try:
            conexion = CConexion.ConexionBaseDeDatos()
            cursor = conexion.cursor()
            sql = "INSERT INTO Estudiante VALUES (%s, %s, %s, %s);"

            #La variable valores es una tupla que contiene los valores a insertar
            valores = (matricula, nombre, correo, contraseña)
            cursor.execute(sql, valores)
            conexion.commit()
            print(cursor.rowcount,"Estudiante registrado correctamente.")
            conexion.close()

        except mysql.connector.Error as error:
            print("Error al insertar el estudiante: {}".format(error))