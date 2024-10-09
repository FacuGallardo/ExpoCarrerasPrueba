import tkinter as tk
from tkinter import messagebox
import mysql.connector

def agregar_persona():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    dni = entry_dni.get()
    carrera = combo_carrera.get()
    
    if not nombre or not apellido or not dni or not carrera:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return
    
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        query = "INSERT INTO personas (nombre, apellido, dni, id_carreras) VALUES (%s, %s, %s, (SELECT id_carreras FROM carreras WHERE nombre=%s))"
        valores = (nombre, apellido, dni, carrera)
        cursor.execute(query, valores)
        conexion.commit()
        messagebox.showinfo("Éxito", "Persona agregada correctamente")
    except Error as e:
        messagebox.showerror("Error", f"Error al agregar la persona: {e}")
    finally:
        cursor.close()
        conexion.close()

root = tk.Tk()
root.title("Gestión de Personas")

tk.Label(root, text="Nombre:").grid(row=0, column=0)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1)

tk.Label(root, text="Apellido:").grid(row=1, column=0)
entry_apellido = tk.Entry(root)
entry_apellido.grid(row=1, column=1)

tk.Label(root, text="DNI:").grid(row=2, column=0)
entry_dni = tk.Entry(root)
entry_dni.grid(row=2, column=1)

tk.Label(root, text="Carrera:").grid(row=3, column=0)
combo_carrera = tk.Entry(root)  # Cambia esto por un ComboBox si tienes las carreras cargadas
combo_carrera.grid(row=3, column=1)

btn_agregar = tk.Button(root, text="Agregar Persona", command=agregar_persona)
btn_agregar.grid(row=4, column=1)

root.mainloop()
