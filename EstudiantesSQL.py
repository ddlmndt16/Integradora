from ConexionSQL import *

class Estudiantes:

   
    def ingresarEstudiante(matricula, nombre, correo, contraseña):
     try:
        conexion = CConexion.ConexionBaseDeDatos()
        cursor = conexion.cursor()
        sql = "INSERT INTO Estudiante VALUES (%s, %s, %s, %s);"
        valores = (matricula, nombre, correo, contraseña)
        cursor.execute(sql, valores)
        conexion.commit()
        print(cursor.rowcount, "Estudiante registrado correctamente.")
        conexion.close()

     except mysql.connector.errors.IntegrityError as error:
        raise Exception("La matrícula o el correo ya están registrados.")
     except Exception as error:
        raise Exception(f"Error inesperado al insertar: {error}")
