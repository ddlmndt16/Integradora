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
  
# ===========================
# ABRIENDO ARCHIVOS DE TEXTO
# ===========================

#---Abriendo los archivos de texto que contienen la bienvenida
with open("Bienvenida.txt", "r", encoding="utf-8") as bienvenida:
    Archivo_B = bienvenida.read()

#---Abriendo el archivo de texto que contiene la introduccion a los ejercicios
with open("IntroEjercicios.txt", "r", encoding="utf-8") as ejer:
    Archivo_E = ejer.read()

#---Abriendo el archivo de texto que contiene la introduccion a los quizzes
with open("IntroQuizzes.txt", "r", encoding="utf-8") as quizz:
    Archivo_Q = quizz.read()

#with administra el contenido sirve para abrir y cerrar el archivo automaticamente
#archivo es la variable que guarda el archivo abierto
#open abre el archivo en modo lectura ("r") y lo guarda en la variable contenido
#encoding="utf-8" asegura que se lea correctamente el texto si contiene caracteres especiales

"""f = open("archivo.txt", "r", encoding="utf-8")
contenido = f.read()
f.close()"""

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

EN_correo = tk.Entry(F_formulario, width=40, font=("Arial",15),bd=0)
EN_correo.grid(row=3, column=0, padx=10, pady= 5, ipady=20)

E_clave = tk.Label(F_formulario,text="Contraseña", font=fuente.Etiquetas, fg="black", bg=color.A_P4)
E_clave.grid(row=4, column=0, padx=10, pady= 5, sticky="w")

EN_clave = tk.Entry(F_formulario,width=40, font=("Arial",15), show="*",bd=0)
EN_clave.grid(row=5, column=0, padx=10, pady= 5, ipady=20)

#Botón para iniciar sesión
#---Boton que al ser presionado llama a la funcion Principal que es la ventana de presentación de ejercicios
boton_guardar = tk.Button(F_formulario,command= Principal, text="Iniciar Sesión", font=("Roboto", 15), bg= color.A_P2, fg= color.B_A, bd=0, width=15, height=2)
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
#Imagen de usuario
image_Usu = Image.open("Usuario.jpeg")  #Archivo de imagen 
image_Usu = image_Usu.resize((100,90))  # Se ajusta el tamaño de la imagen
imagen_Usu_tk = ImageTk.PhotoImage(image_Usu)

#Imagen de ajutes
image_Aju = Image.open("Ajustes.jpeg") 
image_Aju = image_Aju.resize((100,70))  
imagen_Aju_tk = ImageTk.PhotoImage(image_Aju)

# ====================================
# FUNCIONES DE NAVEGACIÓN - Ventana 3
# ====================================

def ejercicios():
    
    Cambio_Ventana(Principal, Ejercicios)

def quizzes():
   
   Cambio_Ventana(Principal, Quizzes)

def perfil():

    Cambio_Ventana(Principal, Perfil_Usu)


Barra_superior = tk.Frame(Principal, bg= color.A_P, width=700, height=30)
Barra_superior.pack(fill=tk.X, side= tk.TOP)

#Botones y etiqueta de la barra_superior

E_Titulo= tk.Label(Barra_superior, text="EJERCICIOS", font=("Times New Roman", 30), fg=color.B_A, bg=color.A_P)
E_Titulo.grid(row=0, column=1, pady=10, padx=390, sticky= "w"+"e")

Perfil = tk.Button(Barra_superior, bd=0, relief="raised", bg= color.A_P2, fg=color.A_P, width=60, height=60,image=imagen_Usu_tk, command= perfil)
Perfil.grid(row=0, column=2, pady=5, padx=30, sticky="e")

#CONTENEDOR PRINCIPAL
Contenedor = tk.Frame(Principal, bg=color.A_P4)
Contenedor.pack(fill="both", expand=True)

#Contenedor que une la barra superior
Cuerpo = tk.Frame(Contenedor, bg=color.A_P4)
Cuerpo.pack(fill="both", expand=True)

#Contenedor que une la barra lateral y el contenido principal
Con_Principal= tk.Frame(Cuerpo, bg=color.A_P4)
Con_Principal.pack(fill="both", expand=True,side=tk.RIGHT )

#Frame del texto de bienvenida
F_Bienvenida = tk.Frame(Con_Principal, bg= color.A_P4)
F_Bienvenida.pack(expand=True, fill="both")

# Frame de la barra lateral
barra_lateral = tk.Frame(Cuerpo, width=200, height=700, bg=color.A_P3)

#botones de la barra lateral (Ubicados en la parte Superior)
H_Ejer = tk.Button(barra_lateral,text="Historial Ejercicios", bd=0, bg= color.A_P2, fg=color.B_A, font=("Arial",12,"bold"), width=15, height= 2)
H_Ejer.grid(row=0, column=1, pady=(50,5), padx=30, sticky="w"+"e")

H_Quizz = tk.Button(barra_lateral,text="Historial Quizzes", bd=0, bg= color.A_P2, fg=color.B_A, font=("Arial",12,"bold"), width=15, height= 2)
H_Quizz.grid(row=1, column=1, pady=(5,160), padx=30, sticky="w"+"e")

#botones de la barra lateral (Ubicados en la parte Inferior)
Cerrar_Se = tk.Button(barra_lateral,text="Cerrar Sesión", bd=0, bg= color.A_P2, fg=color.B_A, font=("Arial",12,"bold"), width=15, height= 2)
Cerrar_Se.grid(row=3, column=1, pady=(160,5), padx=30, sticky="w"+"e")

Regresar_Es = tk.Button(barra_lateral,text="Salir al Escritorio", bd=0, bg= color.A_P2, fg=color.B_A, font=("Arial",12,"bold"), width=15, height= 2)
Regresar_Es.grid(row=4, column=1, pady=5, padx=30, sticky="w"+"e")

#Funcion para la barra lateral
barra_visible = False

"""def toggle_barra():

    global barra_visible

    if barra_visible:
        barra_lateral.pack_forget()
        barra_visible = False
    else:
        barra_lateral.pack(side=tk.LEFT, fill=tk.Y)
        #barra_lateral.lift()
        barra_visible = True
# Inicialmente, oculta la barra lateral"""

def toggle_barra():
    global barra_visible
    if barra_visible:
        barra_lateral.place_forget()
        barra_visible = False
    else:
        barra_lateral.place(x=0, y=0, width=200, height=700)
        barra_lateral.lift()  # Asegura que esté encima de otros widgets
        barra_visible = True


Ajustes = tk.Button(Barra_superior, bd=0, bg= color.A_P2, width=60, height=60,image=imagen_Aju_tk,command= toggle_barra)
Ajustes.grid(row=0, column=0, pady=10, padx=40, sticky="w")

#Etiquetas y botones de F_Bienvenida
E_TablasDirec = tk.Label(F_Bienvenida, text="¡BIENVENIDO!", font=("Roboto", 20,"bold"), bg= color.A_P4, fg="black")
E_TablasDirec.grid(row=0, column=0, padx=320, pady=20, sticky="w"+"e")


E_ConfiRouter = tk.Label(F_Bienvenida, text= Archivo_B , justify="center", wraplength=700, font=("Roboto", 12), bg= color.A_P4, fg="black")
E_ConfiRouter.grid(row=1, column=0, padx=320, pady=2, sticky="w"+"e")

F_Ejercicios = tk.Frame(Con_Principal, bg= color.A_P4)
F_Ejercicios.pack(fill="both", expand=True,side=tk.RIGHT)

#Etiquetas y botones de F_Ejercicios
B_Ejercicios= tk.Button(F_Ejercicios,text="Ejercicios", font=fuente.Textos, bg= color.A_P, bd=0, fg=color.B_A, width=10, height=4, command= ejercicios)
B_Ejercicios.grid(row=1, column=0, padx=(150,50), pady=2, sticky="w")

E_Ejercicios = tk.Label(F_Ejercicios, text="¿Que encontrarás?", font=fuente.Etiquetas, bg= color.A_P4, fg="black")
E_Ejercicios.grid(row=0, column=1, padx=5, pady=5, sticky= "w")

E_Ejercicios = tk.Label(F_Ejercicios, text= Archivo_E, font=("Arial", 12), bg= color.A_P4, fg="black",justify="left", wraplength=300)
E_Ejercicios.grid(row=1, column=1, padx=5, pady=10, sticky="n"+"w")

B_Quizz = tk.Button(F_Ejercicios, text="Quizzes", font=fuente.Textos, bg= color.A_P, bd=0, fg="white",width=10, height=4, command= quizzes)
B_Quizz.grid(row=3, column=0, padx=(150,50), pady=2, sticky="w")

E_Quizz = tk.Label(F_Ejercicios, text="¿Que encontrarás?", font=fuente.Etiquetas, bg= color.A_P4, fg="black")
E_Quizz.grid(row=2, column=1, padx=5, pady=5, sticky="w")

E_Quizz = tk.Label(F_Ejercicios, text= Archivo_Q, font=("Arial", 12), bg= color.A_P4, fg="black", justify="left", wraplength=300)
E_Quizz.grid(row=3, column=1, padx=5, pady=(10,2), sticky="n"+"w")

# ======================================
# VENTANA Ajustes - Apartado de ajustes 
# ======================================

Perfil_Usu = tk.Toplevel(Principal)
Perfil_Usu.title("Estudio-VLSM")
Perfil_Usu.configure(bg=color.A_P4)
Perfil_Usu.geometry("1200x700")

#Imagen de usuario
image_Usu2 = Image.open("Usuario2.jpeg")  
image_Usu2 = image_Usu2.resize((300,280))  
imagen_Usu2_tk = ImageTk.PhotoImage(image_Usu2)

image_Lap = Image.open("Lapiz.jpeg")  
image_Lap = image_Lap.resize((30,30))  
imagen_Lap_tk = ImageTk.PhotoImage(image_Lap)

ventana= Perfil_Usu

def principal(ventana):
    Cambio_Ventana(ventana,Principal)

Barra_superio_A = tk.Frame(Perfil_Usu, bg= color.A_P, width=700, height=50)
Barra_superio_A.pack(fill=tk.X,side=tk.TOP)

E_usuario = tk.Label(Barra_superio_A, text= "Perfil", font=fuente.Titulos, bg= color.A_P, fg="white")
E_usuario.grid(row=1, column=0, padx=620, pady=5, sticky="w"+"e")

F_perfil = tk.Frame(Perfil_Usu, bg= color.A_P4)
F_perfil.pack(expand=True)

#Etiquetas y Entradas

E_usuario = tk.Label(F_perfil, image= imagen_Usu2_tk, font=fuente.Etiquetas, bg= color.A_P4, fg="black")
E_usuario.grid(row=0, column=1, padx=100, pady=10, sticky="w")

E_Lapiz = tk.Label(F_perfil,image= imagen_Lap_tk, bg= color.A_P4)
E_Lapiz.grid(row=1, column=0, padx=(100,2), pady=5, sticky="w")

E_usuario = tk.Label(F_perfil, text= "Cambiar Nombre", font=fuente.Etiquetas, bg= color.A_P4, fg="black")
E_usuario.grid(row=1, column=1, padx=(2,5), pady=5, sticky="w")

EN_usuario = tk.Entry(F_perfil,width=40,font=("Arial",15), bd=0)
EN_usuario.grid(row=2, column=1, padx=10, pady=5, ipady=20, sticky="w")

E_Lap= tk.Label(F_perfil,image= imagen_Lap_tk, bg= color.A_P4)
E_Lap.grid(row=3, column=0, padx=(100,2), pady=5, sticky="w")

E_correo = tk.Label(F_perfil, text="Cambiar Correo", font= fuente.Etiquetas, bg= color.A_P4, fg="black")
E_correo.grid(row=3, column=1, padx=(2,5), pady=5, sticky="w")

EN_correo = tk.Entry(F_perfil,width=40,font=("Arial",15), bd=0)
EN_correo.grid(row=4, column=1, padx=10, pady=5, ipady=20, sticky="w")


B_Ajustes = tk.Button(F_perfil,text="Guardar", font=("Roboto", 15), bg= color.A_P2, fg="white",width=15, height=2, bd=0,command= lambda: principal(ventana))
B_Ajustes.grid(row=5, column=1, pady=30, padx=150, sticky="w")

# =======================
# VENTANA 4 - Ejercicios
# =======================

Ejercicios =tk.Toplevel(Principal)
Ejercicios.title("Estudio-VLSM")
Ejercicios.configure(bg=color.A_P4)
Ejercicios.geometry("1200x700")


# Barra superior
Barra_supe = tk.Frame(Ejercicios, bg= color.A_P, width=700, height=30)
Barra_supe.pack(fill=tk.X, side= tk.TOP)

E_Ejercicios = tk.Label(Barra_supe, text="Ejercicios", font=("Times New Roman", 30), bg= color.A_P, fg="black")
E_Ejercicios.grid(row=0, column=0, padx= 300)

B_perfil = tk.Button(Barra_supe, bd=0, relief="raised", bg= color.A_P2, fg=color.A_P, width=60, height=60,image=imagen_Usu_tk)
B_perfil.grid(row=0, column=1, pady=5, padx=30, sticky="e")

# Título centrado

# ====================
# VENTANA 5 - QUIZZES
# ====================
Quizzes= tk.Toplevel(Principal)
Quizzes.title("Estudio-VLSM")
Quizzes.configure(bg=color.A_P4)
Quizzes.geometry("1200x700")

# Barra superior
Barra_super = tk.Frame(Quizzes, bg= color.A_P, height=70)
Barra_super.pack(fill=tk.X)

# Etiqueta de titulo 
E_Quizz = tk.Label(Barra_super, text="Quizzes", font=("Times New Roman", 39), bg= color.A_P, fg="black")
E_Quizz.grid(row=0, column=0, padx= 300)

# Botón de perfil
B_perfil = tk.Button(Barra_supe, bd=0, relief="raised", bg= color.A_P2, fg=color.A_P, width=60, height=60,image=imagen_Usu_tk)
B_perfil.grid(row=0, column=1, pady=5, padx=30, sticky="e")

# ====================================
# VENTANA 6 - Historial de Ejercicios
# ====================================

Historial_E = tk.Toplevel(Principal)
Historial_E.title("Estudio-VLSM")
Historial_E.configure(bg=color.A_P4)
Historial_E.geometry("1200x700")

# Barra superior
Barra_His= tk.Frame(Historial_E, bg= color.A_P, height=50)
Barra_His.pack(fill=tk.X)

# Etiqueta de titulo
E_historialEjer = tk.Label(Barra_His, text="Historial de QUIZZES", font=("Times New Roman", 39), bg= color.A_P, fg="black")
E_historialEjer.grid(row=0, column=0, padx= 300)

# Botón de ajustes
Ajustes = tk.Button(Barra_His, bd=0, bg= color.A_P2, width=60, height=60,image=imagen_Aju_tk)
Ajustes.grid(row=0, column=0, pady=10, padx=40, sticky="w")


# ====================================
# VENTANA 7 - Historial de Quizzes
# ====================================

Historial_Q = tk.Toplevel(Principal)
Historial_Q.title("Estudio-VLSM")
Historial_Q.configure(bg=color.A_P4)
Historial_Q.geometry("1200x700")

# Barra superior
Barra_His= tk.Frame(Historial_Q, bg= color.A_P, height=50)
Barra_His.pack(fill=tk.X)

# Etiqueta de titulo
E_historialEjer = tk.Label(Barra_His, text="Historial de QUIZZES", font=("Times New Roman", 39), bg= color.A_P, fg="black")
E_historialEjer.grid(row=0, column=0, padx= 300)

# Botón de ajustes
Ajustes = tk.Button(Barra_His, bd=0, bg= color.A_P2, width=60, height=60,image=imagen_Aju_tk)
Ajustes.grid(row=0, column=0, pady=10, padx=40, sticky="w")


# iniciar el bucle de eventos
Inicio.mainloop()
