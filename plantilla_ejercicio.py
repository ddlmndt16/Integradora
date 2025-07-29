import tkinter as tk
from tkinter import messagebox
import mysql.connector

# ====== CONEXIÓN MYSQL ======

import mysql.connector

class CConexion:

    def ConexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(
                user='root',
                password='200618Rm',
                host='localhost',
                database='ProyectoSQL',
                port='3306'
            )
            print("Conexión exitosa a la base de datos.")
            return conexion
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos: {}".format(error))
            return None

# ====== Informacion Estudiante ======

class Estudiantes:

    def ingresarEstudiante(matricula, nombre, correo, contraseña):
        conexion = CConexion.ConexionBaseDeDatos()
        if conexion is None:
            raise Exception("Error al conectar a la base de datos.")

        try:
            cursor = conexion.cursor()
            sql = "INSERT INTO Estudiante (matricula, nombre, correo, contraseña) VALUES (%s, %s, %s, %s);"
            valores = (matricula, nombre, correo, contraseña)
            cursor.execute(sql, valores)
            conexion.commit()
            print("Estudiante registrado correctamente.")
        except mysql.connector.errors.IntegrityError:
            raise Exception("La matrícula o el correo ya están registrados.")
        except Exception as e:
            raise Exception(f"Error al insertar el estudiante: {e}")
        finally:
            conexion.close()

# ====== APLICACIÓN PRINCIPAL ======

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Scripted Networks - Inicio")
        self.root.geometry("1750x1150")
        self.root.configure(bg="#A5B4FC") 

        # Fuentes

        self.fuente_titulo = ("Georgia", 22)
        self.fuente_etiquetas = ("Arial", 10, "bold")
        self.fuente_link = ("Arial", 9, "italic")

        self.frame_actual = None
        self.mostrar_login()

    def limpiar_frame(self):
        if self.frame_actual:
            self.frame_actual.destroy()

    def crear_campo(self, contenedor, texto, es_password=False):
        frame = tk.Frame(contenedor, bg="#A5B4FC")
        frame.pack(pady=15) 

        # Icono de etiqueta

        tk.Label(bg="#A5B4FC", font=("Arial", 12)).pack(anchor="w", padx=5)
        tk.Label(frame, text=texto.upper(), bg="#A5B4FC", fg="black",
                 font=self.fuente_etiquetas).pack(anchor="w", padx=5)

        entrada = tk.Entry(frame, width=40, font=("Arial", 12), bg="#F1F5F9", relief="flat",
                           show="*" if es_password else "")
        entrada.pack(ipady=8, pady=5)
        return entrada

    # ======= Mostrar inicio de sesión =======

    def mostrar_login(self):
        self.root.title("Scripted Networks - Inicio de Sesión")
        self.limpiar_frame()
        self.frame_actual = tk.Frame(self.root, bg="#A5B4FC")
        self.frame_actual.pack(expand=True, pady=10)

        # Encabezado azul

        encabezado = tk.Frame(self.frame_actual, bg="#003CFF", height=80)
        encabezado.pack(fill="x")
        tk.Label(encabezado, text="Inicio de sesión", bg="#003CFF", fg="white",
                 font=self.fuente_titulo).pack(pady=20)

        # Campos

        self.login_matricula = self.crear_campo(self.frame_actual, "Matrícula")
        self.login_correo = self.crear_campo(self.frame_actual, "Correo Electrónico")
        self.login_contraseña = self.crear_campo(self.frame_actual, "Contraseña", es_password=True)

        # Botón de inicio de sesión

        tk.Button(self.frame_actual, text="INICIAR SESIÓN", bg="#3B82F6", fg="white",
                  width=25, height=2, font=("Arial", 12, "bold"),
                  command=self.iniciar_sesion).pack(pady=30)

        # Texto inferior (link de registro)

        frame_link = tk.Frame(self.frame_actual, bg="#A5B4FC")
        frame_link.pack()
        tk.Label(frame_link, text="¿No tienes cuenta?", bg="#A5B4FC", font=self.fuente_link).pack(side="left")

        link = tk.Label(frame_link, text="Registrarse", bg="#A5B4FC", fg="#1D4ED8",
                        font=self.fuente_link, cursor="hand2")
        link.pack(side="left", padx=5)
        link.bind("<Button-1>", lambda e: self.mostrar_registro())

    # ======= Mostrar registro de usuario =======

    def mostrar_registro(self):
        self.root.title("Scripted Networks - Registro de Usuario")
        self.limpiar_frame()
        self.frame_actual = tk.Frame(self.root, bg="#A5B4FC")
        self.frame_actual.pack(expand=True, pady=10)

        encabezado = tk.Frame(self.frame_actual, bg="#003CFF", height=80)
        encabezado.pack(fill="x")
        tk.Label(encabezado, text="Registro de usuario", bg="#003CFF", fg="white",
                 font=self.fuente_titulo).pack(pady=20)

        # Campos del registro
        
        self.reg_matricula = self.crear_campo(self.frame_actual, "Matrícula")
        self.reg_nombre = self.crear_campo(self.frame_actual, "Nombre")
        self.reg_correo = self.crear_campo(self.frame_actual, "Correo Electrónico")
        self.reg_contrasena = self.crear_campo(self.frame_actual, "Contraseña", es_password=True)

        # Botón de registrar

        tk.Button(self.frame_actual, text="REGISTRAR", bg="#3B82F6", fg="white",
                  width=25, height=2, font=("Arial", 12, "bold"),
                  command=self.registrar_usuario).pack(pady=30)

    # Registrar usuario en la base de datos

    def registrar_usuario(self):
        matricula = self.reg_matricula.get()
        nombre = self.reg_nombre.get()
        correo = self.reg_correo.get()
        contraseña = self.reg_contrasena.get()
        if not (matricula and nombre and correo and contraseña):
            messagebox.showwarning("Campos vacíos", "Completa todos los campos.")
            return
        try:
            Estudiantes.ingresarEstudiante(matricula, nombre, correo, contraseña)
            messagebox.showinfo("Éxito", "Registro exitoso. Ahora puedes iniciar sesión.")
            self.mostrar_login()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ====== Iniciar sesión en la aplicación ======

    def iniciar_sesion(self):
        matricula = self.login_matricula.get()
        correo = self.login_correo.get()
        contraseña = self.login_contraseña.get()

        if not (matricula and correo and contraseña):
            messagebox.showwarning("Campos vacíos", "Completa todos los campos.")
            return
        try:
            conexion = CConexion.ConexionBaseDeDatos()
            if conexion:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM Estudiante WHERE matricula=%s AND correo=%s AND contraseña=%s",
                               (matricula, correo, contraseña))
                resultado = cursor.fetchone()
                conexion.close()
                if resultado:
                    self.root.destroy()
                    
                    nueva_ventana = tk.Tk()
                    VentanaPrincipal(nueva_ventana, matricula)
                    nueva_ventana.mainloop()
                else:
                    messagebox.showerror("Error", "Credenciales incorrectas.")
            else:
                messagebox.showerror("Error", "No se pudo conectar a la base de datos.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


# ====== VENTANA PRINCIPAL ======

class VentanaPrincipal:
    def __init__(self, root, matricula):
        self.root = root
        self.matricula = matricula
        self.root.title("Scripted Networks - Pantalla Principal")
        self.root.geometry("1750x1150")
        self.root.configure(bg="#A5B4FC")

        encabezado = tk.Frame(self.root, bg="#003CFF", height=80)
        encabezado.pack(fill="x")

        icono_menu = tk.Label(encabezado, text="☰", font=("Arial", 22), bg="#003CFF", fg="white")
        icono_menu.place(x=15, y=20)

        perfil_frame = tk.Frame(encabezado, bg="#003CFF")
        perfil_frame.pack(side="right", padx=20)
        editar_label = tk.Label(perfil_frame, text="Editar Perfil", font=("Arial", 9, "bold"),
                        bg="#003CFF", fg="white", cursor="hand2")
        editar_label.pack()
        editar_label.bind("<Button-1>", self.abrir_editar_perfil)

        mensaje = tk.Label(self.root, text="¡Bienvenido!\nNos alegra tenerte aquí.\n"
            "Esta aplicación ha sido diseñada para ayudarte a aprender, practicar\n"
            "y dominar los conceptos fundamentales de redes inteligentes,\n"
            "combinando teoría con actividades prácticas e interactivas.",
            font=("Georgia", 11), bg="#A5B4FC", justify="center")
        mensaje.pack(pady=15)

        # Crear la sección de ejercicios
        self.crear_seccion(
            titulo="Ejercicios",
            descripcion="En este apartado podrás encontrar diversos\n"
                        "ejercicios de subnetting para practicar.",
            boton_text="Ir a Ejercicios",
            comando=self.abrir_ejercicios
        )

        # Crear la sección de quizzes
        self.crear_seccion(
            titulo="Quizzes",
            descripcion="Aquí podrás responder preguntas rápidas\n"
                        "para evaluar tus conocimientos.",
            boton_text="Ir a Quizzes",
            comando=lambda: messagebox.showinfo("Quizzes", "Sección de Quizzes aún no implementada.")
        )

    def crear_seccion(self, titulo, descripcion, boton_text, comando):
        contenedor = tk.Frame(self.root, bg="#A5B4FC", bd=1, relief="solid")
        contenedor.pack(pady=8, padx=15, fill="x")

        icono = tk.Label(contenedor, text=titulo, bg="#003CFF", fg="white",
                         font=("Georgia", 13, "italic"), width=12, height=4)
        icono.pack(side="left", padx=20)

        contenido = tk.Frame(contenedor, bg="#A5B4FC")
        contenido.pack(side="left", pady=10)

        tk.Label(contenido, text="¿Qué encontrarás?", font=("Arial", 11, "bold"),
                 bg="#A5B4FC").pack(anchor="w")
        tk.Label(contenido, text=descripcion, font=("Arial", 10),
                 bg="#A5B4FC", justify="left").pack(anchor="w")

        tk.Button(contenido, text=boton_text, command=comando,
                  bg="#3B82F6", fg="white", width=20).pack(pady=5)

    def abrir_ejercicios(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        VentanaEjercicios(self.root, self.volver_a_principal)

    def volver_a_principal(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        VentanaPrincipal(self.root, self.matricula)
        
    def abrir_editar_perfil(self, event=None):
        self.root.destroy()
        editar_root = tk.Tk()
        EditarPerfil(editar_root, self.matricula)
        editar_root.mainloop()

# ====== EDITAR PERFIL ======

class EditarPerfil:
    def __init__(self, root, matricula):
        self.root = root
        self.matricula = matricula
        self.root.title("Scripted Networks - Editar Perfil")
        self.root.geometry("1750x1150")
        self.root.configure(bg="#A6B5FF") 

        # ======= ENCABEZADO AZUL =======

        header = tk.Frame(self.root, bg="#0033FF", height=80)
        header.pack(fill="x")

        # Botón regresar 
        
        btn_volver = tk.Button(header, text="←", bg="#0033FF", fg="white",
                               font=("Arial", 20), bd=0, activebackground="#0033FF",
                               cursor="hand2", command=self.volver_a_principal)
        btn_volver.place(x=10, y=20)

        # Texto "Perfil" centrado

        tk.Label(header, text="Perfil", bg="#0033FF", fg="white",
                 font=("Georgia", 20)).pack(pady=20)

        # ======= ICONO DE USUARIO =======

        canvas = tk.Canvas(self.root, width=150, height=150, bg="#A6B5FF", highlightthickness=0)
        canvas.pack(pady=20)

        # Dibujar un icono de usuario 
        # Cabeza (círculo)

        canvas.create_oval(40, 20, 110, 90, fill="black")

        # Cuerpo (óvalo)

        canvas.create_oval(25, 80, 125, 140, fill="black")

    
        self.nombre_var = tk.StringVar()
        self.correo_var = tk.StringVar()

        # ======= CAMPOS DE ENTRADA =======

        self.crear_campo("Nombre", self.nombre_var)
        self.crear_campo("Correo Electronico", self.correo_var)

        # ======= BOTÓN GUARDAR =======

        tk.Button(self.root, text="GUARDAR CAMBIOS", bg="#3A4DF5", fg="white",
                  font=("Arial", 12, "bold"), relief="flat", width=25, height=2,
                  cursor="hand2", command=self.actualizar_datos).pack(pady=40)

        # Cargar datos del estudiante
        
        self.cargar_datos_estudiante()

    # Crea campos de entrada

    def crear_campo(self, etiqueta, variable, editable=True):
        frame = tk.Frame(self.root, bg="#A6B5FF")
        frame.pack(pady=10)
        tk.Label(frame, text=etiqueta, bg="#A6B5FF", font=("Arial", 10, "bold")).pack(anchor="w", padx=10)
        entry = tk.Entry(frame, textvariable=variable, width=40, font=("Arial", 12), relief="flat")
        entry.pack(ipady=8, padx=10, pady=5)
        if not editable:
            entry.configure(state='readonly')

    # Cargar datos desde la base de datos

    def cargar_datos_estudiante(self):
        conexion = CConexion.ConexionBaseDeDatos()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT nombre, correo FROM Estudiante WHERE matricula = %s", (self.matricula,))
            resultado = cursor.fetchone()
            if resultado:
                self.nombre_var.set(resultado[0])
                self.correo_var.set(resultado[1])
            conexion.close()

    # Guardar cambios

    def actualizar_datos(self):
        nueva_nombre = self.nombre_var.get()
        nuevo_correo = self.correo_var.get()

        if not nueva_nombre or not nuevo_correo:
            messagebox.showwarning("Campos Vacíos", "Todos los campos deben estar llenos.")
            return

        conexion = CConexion.ConexionBaseDeDatos()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("UPDATE Estudiante SET nombre=%s, correo=%s WHERE matricula=%s",
                               (nueva_nombre, nuevo_correo, self.matricula))
                conexion.commit()
                messagebox.showinfo("Éxito", "Datos actualizados correctamente.")
                self.root.destroy()
                nueva_root = tk.Tk()
                VentanaPrincipal(nueva_root, self.matricula)
                nueva_root.mainloop()
            except Exception as e:
                messagebox.showerror("Error", str(e))
            finally:
                conexion.close()

    # Volver a ventana principal
    
    def volver_a_principal(self):
        self.root.destroy()
        nueva_root = tk.Tk()
        VentanaPrincipal(nueva_root, self.matricula)
        nueva_root.mainloop()


# ====== Ejercicios ======

class VentanaEjercicios:
    def __init__(self, root, volver_callback):
        self.root = root
        self.volver_callback = volver_callback
        self.root.title("Scripted Networks - Ejercicios")
        self.root.configure(bg="#A5B4FC")

        # Barra superior 
        
        encabezado = tk.Frame(self.root, bg="#003CFF", height=60)
        encabezado.pack(fill="x")

        # Botón menú

        boton_menu = tk.Label(encabezado, text="☰", font=("Arial", 22), bg="#003CFF", fg="white", cursor="hand2")
        boton_menu.place(x=10, y=10)

        # Título centrado

        titulo = tk.Label(encabezado, text="Ejercicios", font=("Arial", 18, "bold"), bg="#003CFF", fg="white")
        titulo.pack(pady=10)

        # Contenedor principal

        contenedor = tk.Frame(self.root, bg="#A5B4FC")
        contenedor.pack(expand=True, fill="both", pady=20)

        # Lista de botones de ejercicios

        ejercicios = ["Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]

        for i, nombre in enumerate(ejercicios):
            frame_item = tk.Frame(contenedor, bg="#A5B4FC")
            frame_item.pack(fill="x", pady=5)

            boton = tk.Button(frame_item, text=nombre, font=("Arial", 14),
                              bg="#3B4EFF", fg="white", activebackground="#0024AA",
                              relief="flat", padx=10, pady=5, width=15,
                              command=lambda n=nombre: self.abrir_ejercicio(n))
            boton.pack(pady=5)

            if i < len(ejercicios) - 1:

                # Línea divisoria
                
                separator = tk.Frame(contenedor, height=1, bg="black")
                separator.pack(fill="x", pady=2)

          # Boton Volver a ventana principal

        tk.Button(self.root, text="Volver a pantalla principal", bg="#3B82F6", fg="white", width=15,
                  command=self.volver_callback).pack(pady=20)
        
    # Abrir ejercicio

    def abrir_ejercicio(self, nombre):
    id_ejercicio = int(nombre.split()[-1])  # Extrae el número del ejercicio
    self.root.destroy()
    ejercicio_root = tk.Tk()
    EjercicioIndividual(ejercicio_root, volver_callback=lambda: self.regresar(ejercicio_root), 
                        matricula=app.matricula, idEjercicio=id_ejercicio)
    ejercicio_root.mainloop()

def regresar(self, ventana_actual):
    ventana_actual.destroy()
    nueva_root = tk.Tk()
    VentanaPrincipal(nueva_root, app.matricula)
    nueva_root.mainloop()


        
class EjercicioIndividual:
    def __init__(self, root, volver_callback, matricula, idEjercicio):
        self.root = root
        self.volver_callback = volver_callback
        self.matricula = matricula
        self.idEjercicio = idEjercicio

        self.root.title(f"Ejercicio {idEjercicio}")
        self.root.geometry("800x600")
        self.root.configure(bg="#A5B4FC")

        # Encabezado azul
        encabezado = tk.Frame(self.root, bg="#003CFF", height=60)
        encabezado.pack(fill="x")

        btn_volver = tk.Button(encabezado, text="↩", bg="#003CFF", fg="white", bd=0,
                               font=("Arial", 20), cursor="hand2",
                               activebackground="#003CFF", activeforeground="white",
                               command=self.volver_callback)
        btn_volver.place(x=10, y=10)

        tk.Label(encabezado, text=f"Ejercicio {idEjercicio}", bg="#003CFF", fg="white",
                 font=("Georgia", 18)).pack(pady=10)

        # Contenedor
        contenedor = tk.Frame(self.root, bg="#A5B4FC")
        contenedor.pack(padx=30, pady=20, fill="both", expand=True)

        # Pregunta 1
        tk.Label(contenedor, text="Dada la red 192.168.1.0/24, escribe la dirección IP de broadcast correspondiente.",
                 bg="#A5B4FC", fg="black", font=("Arial", 14), anchor="w", justify="left", wraplength=700).pack(pady=(10, 5), anchor="w")
        self.respuesta1 = tk.Entry(contenedor, font=("Arial", 14), bg="#E5E7EB", relief="flat", width=50)
        self.respuesta1.pack(pady=(0, 15))

        separator1 = tk.Frame(contenedor, bg="black", height=1)
        separator1.pack(fill="x", pady=(0, 15))

        # Pregunta 2
        tk.Label(contenedor, text="Escribe la máscara de subred que corresponde a una red con prefijo /26.",
                 bg="#A5B4FC", fg="black", font=("Arial", 14), anchor="w", justify="left", wraplength=700).pack(pady=(0, 5), anchor="w")
        self.respuesta2 = tk.Entry(contenedor, font=("Arial", 14), bg="#E5E7EB", relief="flat", width=50)
        self.respuesta2.pack(pady=(0, 15))

        separator2 = tk.Frame(contenedor, bg="black", height=1)
        separator2.pack(fill="x", pady=(0, 25))

        # Botón terminar
        boton = tk.Button(self.root, text="TERMINAR EJERCICIO", bg="#1D4ED8", fg="white",
                          font=("Arial", 12, "bold"), width=20, height=2, relief="flat",
                          command=self.terminar_ejercicio)
        boton.pack(pady=10)

    def terminar_ejercicio(self):
        r1 = self.respuesta1.get().strip()
        r2 = self.respuesta2.get().strip()

        if not r1 or not r2:
            messagebox.showwarning("Campos vacíos", "Por favor responde ambas preguntas.")
            return

# ====== INICIO DE LA APLICACIÓN ======

root = tk.Tk()
app = Aplicacion(root)
root.mainloop()