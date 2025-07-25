import tkinter as tk
import mysql.connector
from tkinter import messagebox
from tkinter import font

# ======================================
# CONEXIÓN A LA BASE DE DATOS MYSQL
# ======================================

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="STFUimdyingofguilt000616",
        database="ProyectoIntegrador"
    )
except mysql.connector.Error as err:
    print("Error de conexión a la base de datos:", err)
    exit()

# ====================
# FUENTES Y COLORES
# ====================

#Creando una clase que organice las fuentes que se ocuparan
#,Titulos, Textos, Botones, etiquetas

"""class Fuentes:
    def __init__(self):

            self.Titulos = font.Font(family="Roboto", size=13, weight="bold")
            self.Textos = font.Font(family="Roboto", size=16, weight="light")
            self.Botones = font.Font(family="Roboto", size=13, weight="semibold")
            self.Etiquetas = font.Font(family="Roboto", size=13, weight="medium")"""
import sqlite3 as sql


#Creando una clase que organice las fuentes que se ocuparan
#,Titulos, Textos, Botones, etiquetas

def __init__(self):

        self.Titulos = font.Font(family="Roboto", size=13, weight="bold")
        self.Textos = font.Font(family="Roboto", size=16, weight="light")
        self.Botones = font.Font(family="Roboto", size=13, weight="semibold")
        self.Etiquetas = font.Font(family="Roboto", size=13, weight="medium")
        
#fuente= Fuentes()
def Cambio_Ventana(ventana1,ventana2):

    ventana1.withdraw()#ocultar
    ventana2.deiconify()#mostrar 

#Creando la clase para organizar los colores que se ocuparan
#,A_P, A_P2, A_P3, A_P4, B_A

class Colores:

    def __init__(self):

        self.A_P = "#3B05C4"
        self.A_P2 = "#3352F3"
        self.A_P3 = "#687EF4"
        self.A_P4 = "#A1AFF7"
        self.B_A = "#F4F5FE"

color = Colores()
#Creando la clase para organizar la navegacion en la pagina

#Cambio = Navegacion()

#def Crear_Ventana(Ventana):

    #Ventana.title("Estudio-VLS")
    #Ventana.configure(bg=color.B_A)
    #Ventana.geometry("1200x700")       

# =======================
# VENTANA 1 - Registro
# =======================

 
Inicio = tk.Tk()
Inicio.title("Estudio-VLS")
Inicio.configure(bg=color.B_A)
Inicio.geometry("1200x700")

#Crear_Ventana(Inicio)

def Principal():

    Cambio_Ventana (Inicio,Principal)

F_Der = tk.Frame(Inicio, bg= color.A_P3, width=300)
F_Izq= tk.Frame(Inicio, bg= color.A_P3, width=300)
F_Sup = tk.Frame(Inicio, bg= color.A_P, width=700, height=50)

F_Der.pack(fill=tk.Y, side=tk.RIGHT, expand= True)
F_Izq.pack(fill=tk.Y, side=tk.LEFT, expand= True)
F_Sup.pack(fill=tk.X, side= tk.TOP)

F_formulario = tk.Frame(Inicio, bg=color.B_A)
F_formulario.pack(expand=True)
#Etiquetas y entradas
E_usuario = tk.Label(F_formulario,text="Nombre de Usuario", font=("Roboto",13), fg="black")
E_usuario.grid(row=0, column=0, padx=10, pady=5, sticky="e")

EN_usuario = tk.Entry(F_formulario,width=30)
EN_usuario.grid(row=0, column=1, padx=10, pady=5)

E_correo = tk.Label(F_formulario,text="Correo electronico", font=("Roboto",13), fg="black")
E_correo.grid(row=1, column=0, padx=10, pady=5, sticky="e")

EN_correo = tk.Entry(F_formulario,width=30)
EN_correo.grid(row=1, column=1, padx=10, pady=5)

E_clave = tk.Label(F_formulario,text="Contraseña", font=("Roboto",13), fg="black")
E_clave.grid(row=2, column=0, padx=10, pady=5, sticky="e")

EN_clave = tk.Entry(F_formulario,width=30)
EN_clave.grid(row=2, column=1, padx=10, pady=5)

E_matricula = tk.Label(F_formulario,text="Matricula", font=("Roboto",13), fg="black")
E_matricula.grid(row=3, column=0, padx=10, pady=5, sticky="e")

EN_matricula = tk.Entry(F_formulario,width=30)
EN_matricula.grid(row=3, column=1, padx=10, pady=5)


#Funcion para guardar datos en la base de datos
def guardar_datos():
    matricula = EN_matricula.get()  # Obtener el nombre de usuario
    nombre = EN_usuario.get()
    correo = EN_correo.get()
    clave = EN_clave.get()

    # Conexión a la base de datos SQLite
    # Guardar en la base de datos
    conexionBD = sql.connect("Estudiante")
    cursor = conexionBD.cursor()

    cursor.execute(f"INSERT INTO Estudiante (matricula,nombre, correo, contraseña) VALUES ('{matricula}', '{nombre}', '{correo}','{clave}')")

    conexionBD.commit()
    conexionBD.close()


#messagebox.showinfo("Datos guardados correctamente")
#image_Usu = Img.open("Usuario.jpg")
#Variable(caja de texto).set("Abigaíl")
#boton para pasar a la segunda ventana
boton_guardar = tk.Button(F_formulario,command= lambda:[guardar_datos(),Principal], text="Registarse", font=("Roboto", 15), bg= color.A_P, fg= color.B_A, width=10, height=2)
boton_guardar.grid(row=4, column=0, columnspan=2, pady=30)

# ====================================
# VENTANA 2 - Selección de Ejercicios 
# ====================================

Principal = tk.Toplevel(Inicio)
Principal.title("Estudio-VLS")
Principal.configure(bg=color.B_A)
Principal.geometry("1200x700")

#Crear_Ventana(Principal)

# ====================================
# FUNCIONES DE NAVEGACIÓN - Ventana 2
# ====================================

def vlsm():
    
    Cambio_Ventana(Principal, Ejer_VLSM)

def tablasDirec():
   
   Cambio_Ventana(Principal, Ejer_TablasDirec)

def Config():

   Cambio_Ventana(Principal, Ajustes)

def configRouter():

    Cambio_Ventana(Principal, Ejer_ConfiRouter)


Barra_superio = tk.Frame(Principal, bg= color.A_P , width=700, height=80)
Barra_superio.pack(fill=tk.X)

E_Titulo= tk.Label(Barra_superio, text="EJERCICIOS", font=("Times New Roman", 30), bg=color.B_A, fg="black")
E_Titulo.grid(row=0, column=0, columnspan=2, pady=20)

Ajustes = tk.Button(Barra_superio, text="Ajustes", font=("Roboto", 12), bg= color.A_P3, fg="white", width=10, height=2,command= Config)
Ajustes.grid(row=4, column=0, columnspan=2, pady=20)

"""Barra_superio = tk.Frame(Principal, bg= color.B_A, width=700, height=150)
Barra_superio.pack(fill=tk.X)"""

Etiqueta1 = tk.Frame(Principal, bg= color.B_A)
Etiqueta1.pack(expand=True)

#Etiquetas y botones
E_VLSM = tk.Label(Etiqueta1, text="VLSM", font=("Roboto", 30), bg= color.B_A, fg="black")
E_VLSM.grid(row=1, column=0, padx=20, pady=10, sticky="e")

B_EjerVLSM = tk.Button(Etiqueta1,text="Abrir", font=("Roboto", 15), bg= color.A_P, fg="white",width=10, height=2,command= vlsm)
B_EjerVLSM.grid(row=1, column=1, padx=10, pady=10)

#2
E_TablasDirec = tk.Label(Etiqueta1, text="Tablas de direccionamiento", font=("Roboto", 30), bg= color.B_A, fg="black")
E_TablasDirec.grid(row=2, column=0, padx=20, pady=10, sticky="e")

B_EjerTablasDirec = tk.Button(Etiqueta1,text="Abrir", font=("Roboto", 15), bg= color.A_P, fg="white",width=10, height=2,command= tablasDirec)
E_TablasDirec.grid(row=2, column=1, padx=10, pady=10)

#3
E_ConfiRouter = tk.Label(Etiqueta1, text="Configuración de un Router", font=("Roboto", 30), bg= color.B_A, fg="black")
E_ConfiRouter.grid(row=3, column=0, padx=20, pady=10, sticky="e")

B_EjerConfigRouter = tk.Button(Etiqueta1,text="Abrir", font=("Roboto", 15), bg= color.A_P, fg="white",width=10, height=2,command= configRouter)
E_ConfiRouter.grid(row=3, column=1, padx=10, pady=10)



# ======================================
# VENTANA Ajustes - Apartado de ajustes 
# ======================================

Ajustes = tk.Toplevel(Principal)
Ajustes.title("Estudio-VLS")
Ajustes.configure(bg=color.B_A)
Ajustes.geometry("1200x700")

#Crear_Ventana(Ajustes)
ventana= Ajustes
def principal(ventana):
    Cambio_Ventana(ventana,Principal)

Barra_superio_A = tk.Frame(Ajustes, bg= color.A_P, width=700, height=80)
Barra_superio_A.pack(fill=tk.X,side=tk.TOP)

F_Ajustes = tk.Frame(Ajustes, bg= color.B_A)
F_Ajustes.pack(expand=True)

#Etiquetas y Entradas
E_usuario = tk.Label(F_Ajustes, text="Cambiar Nombre ", font=("Roboto",15), bg= color.A_P4, fg="white")
E_usuario.pack(pady=5, padx=200)

EN_usuario = tk.Entry(F_Ajustes,width=30,font=(18))
EN_usuario.pack(pady=5, padx=20)

E_correo = tk.Label(F_Ajustes, text="Cambiar Correo", font=("Roboto",15), bg= color.A_P4, fg="white")
E_correo.pack(pady=5, padx=10)

EN_correo = tk.Entry(F_Ajustes,width=30,font=(18))
EN_correo.pack(pady=5, padx=20)


B_Ajustes = tk.Button(F_Ajustes,text="Guardar", font=("Roboto", 15), bg= color.A_P, fg="white",width=10, height=2,command= principal(ventana))
B_Ajustes.pack(pady=30)

# ============================
# VENTANA 3 - Ejercicio VLSM
# ============================

Ejer_VLSM =tk.Toplevel(Principal)
Ejer_VLSM.title("Estudio-VLS")
Ejer_VLSM.configure(bg=color.B_A)
Ejer_VLSM.geometry("1200x700")

#Crear_Ventana(Ejer_VLSM)

# Barra superior
Barra_superior3 = tk.Frame(Ejer_VLSM, bg= color.A_P, height=20)
Barra_superior3.grid(row=0, column=1, padx=10)

B_Regresar = tk.Button(Barra_superior3, text="Regresar", font=("Roboto", 12), bg= color.A_P3, fg="white", width=10, height=2, command= principal(Ejer_VLSM))
B_Regresar.grid(row=0, column=0, pady=5)

# Título centrado
E_Titulo = tk.Label(Barra_superior3, text="EJERCICIO VLSM", font=("Times New Roman", 30), bg= color.A_P, fg="black")
E_Titulo.grid(row=0, column=4,padx= 300)

#Etiqueta
#Etiqueta1_V3 = tk.Frame(ventana3, bg="#FFFFFF")
#Etiqueta1_V3.pack(pady=40, fill=tk.X, padx=10)

# ============================
# VENTANA 4 - Tablas de direccionamiento
# ============================

Ejer_TablasDirec= tk.Toplevel(Principal)
Ejer_TablasDirec.title("Estudio-VLS")
Ejer_TablasDirec.configure(bg=color.B_A)
Ejer_TablasDirec.geometry("1200x700")

#Crear_Ventana(Ejer_TablasDirec)

# Barra superior
Barra_superior4 = tk.Frame(Ejer_TablasDirec, bg= color.A_P, height=70)
Barra_superior4.pack(fill=tk.X)

# Título centrado
E_Titulo = tk.Label(Barra_superior4, text="Tablas de direccionamiento", font=("Times New Roman", 39), bg= color.A_P, fg="black")
E_Titulo.pack(pady=20)

# Botón a la izquierda
B_Regresar = tk.Button(Barra_superior4, text="Regresar", font=("Roboto", 12), bg=color.A_P3, fg="white", width=10, height=2, command= principal(Ejer_TablasDirec))
B_Regresar.pack(pady=10)

# ============================
# VENTANA 5 - Configuración de Router
# ============================

Ejer_ConfiRouter = tk.Toplevel(Principal)
Ejer_ConfiRouter.title("Estudio-VLS")
Ejer_ConfiRouter.configure(bg=color.B_A)
Ejer_ConfiRouter.geometry("1200x700")

#Crear_Ventana(Ejer_ConfiRouter)

# Barra superior
Barra_superior5= tk.Frame(Ejer_ConfiRouter, bg= color.A_P, height=70)
Barra_superior5.pack(fill=tk.X)

B_Regresar = tk.Button(Barra_superior5, text="Regresar", font=("Roboto", 12), bg= color.A_P3, fg="white", width=10, height=2, command= principal(Ejer_ConfiRouter))
B_Regresar.pack(pady=10)

E_Titulo = tk.Label(Barra_superior5, text="Configuración de un Router", font=("Times New Roman", 39), bg= color.A_P, fg="black")
E_Titulo.pack(pady=20)


#Etiqueta1_V5 = tk.Frame(ventana5, bg="#FFFFFF")
#Etiqueta1_V5.pack(pady=40, fill=tk.X, padx=10)

# iniciar el bucle de eventos
Inicio.mainloop()
