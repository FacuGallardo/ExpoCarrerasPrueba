import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='tu_usuario',
            password='tu_contraseña',
            database='isaui'
        )
        return conexion
    except Error as e:
        messagebox.showerror("Error de conexión", str(e))

def agregar_persona():
    apellido = entry_apellido.get()
    nombre = entry_nombre.get()
    dni = entry_dni.get()
    telefono = entry_telefono.get()
    correo = entry_correo.get()
    domicilio = entry_domicilio.get()
    ciudad = entry_ciudad.get()
    instagram = entry_instagram.get()
    carrera = combo_carreras.get()

    if validar_dni(dni) and validar_nombre(nombre) and validar_telefono(telefono) and validar_domicilio(domicilio) and validar_ciudad(ciudad) and validar_carrera(carrera):
        try:
            conexion = conectar_bd()
            cursor = conexion.cursor()
            query = "INSERT INTO personas (apellido, nombre, dni, telefono, correo, domicilio, ciudad, instagram, id_carreras) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, (SELECT id_carreras FROM carreras WHERE nombre = %s))"
            cursor.execute(query, (apellido, nombre, dni, telefono, correo, domicilio, ciudad, instagram, carrera))
            conexion.commit()
            messagebox.showinfo("Éxito", "Persona agregada correctamente")
        except Error as e:
            messagebox.showerror("Error", str(e))
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

def limpiar_campos():
    entry_apellido.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_dni.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    entry_correo.delete(0, tk.END)
    entry_domicilio.delete(0, tk.END)
    entry_ciudad.delete(0, tk.END)
    entry_instagram.delete(0, tk.END)
    combo_carreras.set('')

def validar_dni(dni):
    if not dni.isdigit():
        messagebox.showwarning("Error", "Únicamente números en DNI Bobo")
        limpiar_campos()
        return False
    return True

def validar_nombre(nombre):
    if not nombre.isalpha():
        messagebox.showwarning("Error", "Nombres van letras únicamente bobo")
        limpiar_campos()
        return False
    return True

def validar_telefono(telefono):
    if not telefono.isdigit():
        messagebox.showwarning("Error", "Teléfono va números únicamente bobo")
        limpiar_campos()
        return False
    return True

def validar_domicilio(domicilio):
    if not all(c.isalnum() or c.isspace() for c in domicilio):
        messagebox.showwarning("Error", "Domicilio va letras y números únicamente bobo")
        limpiar_campos()
        return False
    return True

def validar_ciudad(ciudad):
    if not ciudad.isalpha():
        messagebox.showwarning("Error", "Ciudad va letras únicamente bobo")
        limpiar_campos()
        return False
    return True

def validar_carrera(carrera):
    if not carrera.isalpha():
        messagebox.showwarning("Error", "Carrera va letras únicamente bobo")
        limpiar_campos()
        return False
    return True

root = tk.Tk()
root.title("Registro de Personas")
root.geometry("400x500")
root.configure(bg="#5F9EA0")
root.resizable(False, False)

label_apellido = tk.Label(root, text="Apellido", bg="#5F9EA0")
label_apellido.pack()
entry_apellido = tk.Entry(root)
entry_apellido.pack()

label_nombre = tk.Label(root, text="Nombre", bg="#5F9EA0")
label_nombre.pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

label_dni = tk.Label(root, text="DNI", bg="#5F9EA0")
label_dni.pack()
entry_dni = tk.Entry(root)
entry_dni.pack()

label_telefono = tk.Label(root, text="Teléfono", bg="#5F9EA0")
label_telefono.pack()
entry_telefono = tk.Entry(root)
entry_telefono.pack()

label_correo = tk.Label(root, text="Correo", bg="#5F9EA0")
label_correo.pack()
entry_correo = tk.Entry(root)
entry_correo.pack()

label_domicilio = tk.Label(root, text="Domicilio", bg="#5F9EA0")
label_domicilio.pack()
entry_domicilio = tk.Entry(root)
entry_domicilio.pack()

label_ciudad = tk.Label(root, text="Ciudad", bg="#5F9EA0")
label_ciudad.pack()
entry_ciudad = tk.Entry(root)
entry_ciudad.pack()

label_instagram = tk.Label(root, text="Instagram", bg="#5F9EA0")
label_instagram.pack()
entry_instagram = tk.Entry(root)
entry_instagram.pack()

label_carrera = tk.Label(root, text="Carrera", bg="#5F9EA0")
label_carrera.pack()
combo_carreras = tk.StringVar(root)
combo_carreras.set("Seleccione una carrera")
carreras = ["Software", "Enfermería", "Diseño de Espacios", "Guía de Trekking", "Guía de Turismo", "Turismo y Hotelería"]
dropdown_carreras = tk.OptionMenu(root, combo_carreras, *carreras)
dropdown_carreras.pack()

button_agregar = tk.Button(root, text="Agregar Persona", command=agregar_persona, bg="#00008B", fg="white")
button_agregar.pack()

button_limpiar = tk.Button(root, text="Limpiar Campos", command=limpiar_campos, bg="#00008B", fg="white")
button_limpiar.pack()

root.mainloop()
