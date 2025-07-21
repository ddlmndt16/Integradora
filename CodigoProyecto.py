import tkinter as tk
import sqlite3 as sql
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import font

# =============================
# CLASE PARA ORGANIZAR FUENTES
# =============================

#---Creando una clase que organice las fuentes que se ocuparan
#---Titulos, Textos, Botones, etiquetas.

class Fuentes:
    def __init__(self):

            self.Titulos = font.Font(family="Bahnschrift SemiLigh", size=32, weight="normal")
            self.Textos = font.Font(family="Arial", size=24, weight="bold")
            self.Boton_eje = font.Font(family="Roboto", size=30, weight="bold")
            self.Botones = font.Font(family="Roboto", size=16, weight="normal")
            self.Etiquetas = font.Font(family="Times New Roman", size=20, weight="normal")

# =============================
# CLASE PARA ORGANIZAR COLORES
# =============================

#---Creando la clase para organizar los colores que se ocuparan
#---A_P, A_P2, A_P3, A_P4, B_A

class Colores:

    def __init__(self):

        self.A_P = "#0429F1"
        self.A_P2 = "#3352F3"
        self.A_P3 = "#687EF4"
        self.A_P4 = "#A1AFF7"
        self.B_A = "#F4F5FE"

#3B05C4
color = Colores()

# =============================
# FUNCION DE CAMBIO DE VENTANA
# =============================

#---Creando la funcion para organizar la navegacion entre ventanas.

def Cambio_Ventana(ventana1,ventana2):

    ventana1.withdraw()#ocultar
    ventana2.deiconify()#mostrar 
  

# =============================
# VENTANA 1 - Inicio de Secion
# =============================

 
Inicio = tk.Tk()
Inicio.title("Estudio-VLSM")
Inicio.configure(bg=color.A_P4)
Inicio.geometry("1200x700")

fuente= Fuentes()

def Principal():

    Cambio_Ventana (Inicio,Principal)

def Registro():

    Cambio_Ventana (Inicio,Registro)

#Wiget superior de la ventana de inicio de sesión
F_Sup = tk.Frame(Inicio, bg= color.A_P, width=700, height=50)
F_Sup.pack(fill=tk.X, side= tk.TOP)

#Etiqueta de inicio de sesión
E_InicioS = tk.Label(F_Sup,text="Inicio de Sesión", font=fuente.Titulos, fg="white",bg=color.A_P)
E_InicioS.pack(pady=5)
#E_InicioS.grid(row=0, column=2, padx=10, pady=5, sticky= "n")

#Frame para el formulario de inicio de sesión
F_formulario = tk.Frame(Inicio, bg=color.A_P4)
F_formulario.pack(expand=True)

#Etiquetas y entradas para el formulario de inicio de sesión
E_matricula = tk.Label(F_formulario,text="Matricula", font= fuente.Etiquetas, fg="black", bg=color.A_P4)
E_matricula.grid(row=0, column=0, padx=10, pady=5, sticky="w")

EN_matricula = tk.Entry(F_formulario,width=40,font=("Arial",15), bd=0)
EN_matricula.grid(row=1, column=0, padx=10, pady=5, ipady=20)

E_correo = tk.Label(F_formulario,text="Correo electronico", font= fuente.Etiquetas, fg="black", bg=color.A_P4 )
E_correo.grid(row=2, column=0, padx=10, pady=5, sticky="w")

EN_correo = tk.Entry(F_formulario,width=40, font=("Arial",15),bd=0)
EN_correo.grid(row=3, column=0, padx=10, pady= 5, ipady=20)

E_clave = tk.Label(F_formulario,text="Contraseña", font=fuente.Etiquetas, fg="black", bg=color.A_P4)
E_clave.grid(row=4, column=0, padx=10, pady=5, sticky="w")

EN_clave = tk.Entry(F_formulario,width=40,font=("Arial",15), show="*",bd=0)
EN_clave.grid(row=5, column=0, padx=10, pady=5, ipady=20)

#Botón para iniciar sesión
#---Boton que al ser presionado llama a la funcion Principal que es la ventana de presentación de ejercicios
boton_guardar = tk.Button(F_formulario,command= Principal, text="Iniciar Sesión", font=("Roboto", 15), bg= color.A_P2, fg= color.B_A,bd=0, width=15, height=2)
boton_guardar.grid(row=6, column=0, pady=30)

E_Pregunta = tk.Label(F_formulario,text="¿No tienes una cuenta?", font=("Arial", 15), fg="black", bg=color.A_P4)
E_Pregunta.grid(row=7, column=0, padx=10, pady=1, sticky="e"+"w")

#Botón para registrarse
#---Boton que al ser presionado llama a la funcion Registro que es la ventana de registro de usuario
boton_registro = tk.Button(F_formulario,command= Registro , text="Registrarse", font=("Roboto", 10, "underline","bold"), bg= color.A_P4, fg= "black",bd=0, activebackground=color.A_P4, width=15, height=2)
boton_registro.grid(row=8, column=0, pady=1)


#Funcion para guardar datos en la base de datos
"""
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
    conexionBD.close()"""


#messagebox.showinfo("Datos guardados correctamente")
#Variable(caja de texto).set("Abigaíl")
#boton para pasar a la segunda ventana

# =======================
# VENTANA 2 - Registro
# =======================

Registro = tk.Toplevel(Inicio)
Registro.title("Estudio-VLSM")
Registro.configure(bg=color.A_P4)
Registro.geometry("1200x700")

fuente= Fuentes()
Cambio_Ventana (Registro,Inicio)

F_Sup = tk.Frame(Registro, bg= color.A_P, width=700, height=50)
F_Sup.pack(fill=tk.X, side= tk.TOP)

E_InicioS = tk.Label(F_Sup,text="Registro de usuario", font=fuente.Titulos, fg="white", bg=color.A_P)
E_InicioS.pack(pady=5)

F_registro = tk.Frame(Registro, bg=color.A_P4)
F_registro.pack(expand=True)

#Etiquetas y entradas para el formulario de registro
E_nombre = tk.Label(F_registro,text="Nombre", font= fuente.Etiquetas, fg="black", bg=color.A_P4)
E_nombre.grid(row=0, column=0, padx=10, pady=5, sticky="w")

EN_nombre = tk.Entry(F_registro,width=40,font=("Arial",15), bd=0)
EN_nombre.grid(row=1, column=0, padx=10, pady=5, ipady=20)

E_matricula = tk.Label(F_registro,text="Matricula", font= fuente.Etiquetas, fg="black", bg=color.A_P4)
E_matricula.grid(row=2, column=0, padx=10, pady=5, sticky="w")

EN_matricula = tk.Entry(F_registro,width=40,font=("Arial",15), bd=0)
EN_matricula.grid(row=3, column=0, padx=10, pady=5, ipady=20)

E_correo = tk.Label(F_registro,text="Correo electronico", font= fuente.Etiquetas, fg="black", bg=color.A_P4 )
E_correo.grid(row=4, column=0, padx=10, pady=5, sticky="w")

EN_correo = tk.Entry(F_registro,width=40, font=("Arial",15),bd=0)
EN_correo.grid(row=5, column=0, padx=10, pady= 5, ipady=20)

E_clave = tk.Label(F_registro,text="Contraseña", font=fuente.Etiquetas, fg="black", bg=color.A_P4)
E_clave.grid(row=6, column=0, padx=10, pady=5, sticky="w")

EN_clave = tk.Entry(F_registro,width=40,font=("Arial",15), show="*",bd=0)
EN_clave.grid(row=7, column=0, padx=10, pady=5, ipady=20)

boton_guardar = tk.Button(F_registro,command= Inicio, text="Registarse", font=("Roboto", 15), bg= color.A_P2, fg= color.B_A,bd=0, activebackground=color.A_P, width=15, height=2)
boton_guardar.grid(row=8, column=0, pady=30)

# ====================================
# VENTANA 3 - Selección de Ejercicios 
# ====================================

Principal = tk.Toplevel(Inicio)
Principal.title("Estudio-VLSM")
Principal.configure(bg=color.A_P4)
Principal.geometry("1200x700")

fuente= Fuentes()
image_Usu = Image.open("Usuario.png")  # Asegúrate de que la imagen esté en el mismo directorio o proporciona la ruta correcta
image_Usu = image_Usu.resize((60,60))  # Ajusta el tamaño según sea necesario
imagen_Usu_tk = ImageTk.PhotoImage(image_Usu)

# ====================================
# FUNCIONES DE NAVEGACIÓN - Ventana 3
# ====================================

def vlsm():
    
    Cambio_Ventana(Principal, Ejer_VLSM)

def tablasDirec():
   
   Cambio_Ventana(Principal, Ejer_TablasDirec)

def Config():

   Cambio_Ventana(Principal, Ajustes)

def configRouter():

    Cambio_Ventana(Principal, Ejer_ConfiRouter)


Barra_superior = tk.Frame(Principal, bg= color.A_P, width=700, height=30)
Barra_superior.pack(fill=tk.X)


Ajustes = tk.Button(Barra_superior, bd=0, bg= color.A_P2, width=10, height=2,command= Config)
Ajustes.grid(row=0, column=0, pady=10, padx=40, sticky="w")

E_Titulo= tk.Label(Barra_superior, text="EJERCICIOS", font=("Times New Roman", 30), fg=color.B_A, bg=color.A_P)
E_Titulo.grid(row=0, column=1, pady=10, padx=300, sticky= "w"+"e")

Perfil = tk.Button(Barra_superior, bd=0, bg= color.A_P2, fg=color.A_P, width=60, height=60,image=imagen_Usu_tk,command= Config)
Perfil.grid(row=0, column=2, pady=5, padx=40, sticky="e")

F_Bienvenida = tk.Frame(Principal, bg= color.A_P4)
F_Bienvenida.pack(expand=True)

E_TablasDirec = tk.Label(F_Bienvenida, text="Tablas de direccionamiento", font=("Roboto", 30), bg= color.B_A, fg="black")
E_TablasDirec.grid(row=0, column=0, padx=20, pady=10, sticky="e")

E_ConfiRouter = tk.Label(F_Bienvenida, text="Configuración de un Router", font=("Roboto", 30), bg= color.B_A, fg="black")
E_TablasDirec.grid(row=1, column=0, padx=20, pady=10, sticky="e")

F_Ejercicios = tk.Frame(Principal, bg= color.A_P4)
F_Ejercicios.pack(expand=True)

#Etiquetas y botones

B_Ejercicios= tk.Button(F_Ejercicios,text="Ejercicios", font=("Roboto", 15), bg= color.A_P, bd=0, fg="white",width=10, height=2)
B_Ejercicios.grid(row=0, column=0, padx=10, pady=10)

E_Ejercicios = tk.Label(F_Ejercicios, text="VLSM", font=("Roboto", 30), bg= color.A_P4, fg="black")
E_Ejercicios.grid(row=0, column=1, padx=20, pady=10, sticky="e")

B_Quizz = tk.Button(F_Ejercicios,text="Quizzes", font=("Roboto", 15), bg= color.A_P, pd=0, fg="white",width=10, height=2)
B_Quizz.grid(row=1, column=0, padx=10, pady=10)

E_Quizz = tk.Label(F_Ejercicios, text="Tablas de direccionamiento", font=("Roboto", 30), bg= color.A_P4, fg="black")
E_Quizz.grid(row=1, column=1, padx=20, pady=10, sticky="e")


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
# VENTANA 4 - Ejercicio VLSM
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
# VENTANA 5 - Tablas de direccionamiento
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
# VENTANA 6 - Configuración de Router
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
