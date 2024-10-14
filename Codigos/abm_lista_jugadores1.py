import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import re

def cargar_imagen(label):
    archivo = filedialog.askopenfilename(filetypes=[("Imagenes", "*.png;*.jpg;*.jpeg")])
    if archivo:
        img = Image.open(archivo)
        img = img.resize((100, 100), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        label.config(image=img)
        label.image = img

def validar_campos():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    dni = entry_dni.get()
    domicilio = entry_domicilio.get()
    telefono = entry_telefono.get()

    if not re.match("^[A-Za-z]+$", nombre):
        messagebox.showerror("Error", "Por favor, escriba su nombre como está en el DNI")
        return False
    if not re.match("^[A-Za-z]+$", apellido):
        messagebox.showerror("Error", "Por favor, escriba su apellido como está en el DNI")
        return False
    if not re.match("^[0-9]+$", dni):
        messagebox.showerror("Error", "Por favor, solo números en el DNI")
        return False
    if not re.match("^[A-Za-z0-9 ]+$", domicilio):
        messagebox.showerror("Error", "Por favor, escriba su domicilio como está en el DNI")
        return False
    if not re.match("^[0-9]+$", telefono):
        messagebox.showerror("Error", "Por favor, escriba su teléfono como está en el DNI")
        return False

    return True

root = tk.Tk()
root.title("Alta/Modificación de Jugadores")
root.geometry("600x400")
root.configure(bg="#3b3b3b")
root.resizable(False, False)

header = tk.Frame(root, bg="#ff7f00", height=50)
header.pack(fill=tk.X)

tk.Label(header, text="Ve el Socio/presidenta", bg="#ff7f00", font=("Arial", 12)).pack(side=tk.LEFT, padx=10)

frame = tk.Frame(root, bg="#3b3b3b")
frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

# Campos: Nombre, Apellido, DNI, Domicilio, Teléfono
tk.Label(frame, text="Nombre", bg="#3b3b3b", fg="white").grid(row=0, column=0, sticky="e", padx=10, pady=5)
entry_nombre = tk.Entry(frame, width=30)
entry_nombre.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Apellido", bg="#3b3b3b", fg="white").grid(row=1, column=0, sticky="e", padx=10, pady=5)
entry_apellido = tk.Entry(frame, width=30)
entry_apellido.grid(row=1, column=1, pady=5)

tk.Label(frame, text="D.N.I", bg="#3b3b3b", fg="white").grid(row=2, column=0, sticky="e", padx=10, pady=5)
entry_dni = tk.Entry(frame, width=30)
entry_dni.grid(row=2, column=1, pady=5)

tk.Label(frame, text="Domicilio", bg="#3b3b3b", fg="white").grid(row=3, column=0, sticky="e", padx=10, pady=5)
entry_domicilio = tk.Entry(frame, width=30)
entry_domicilio.grid(row=3, column=1, pady=5)

tk.Label(frame, text="Teléfono", bg="#3b3b3b", fg="white").grid(row=4, column=0, sticky="e", padx=10, pady=5)
entry_telefono = tk.Entry(frame, width=30)
entry_telefono.grid(row=4, column=1, pady=5)

tk.Label(frame, text="Sexo", bg="#3b3b3b", fg="white").grid(row=5, column=0, sticky="e", padx=10, pady=5)
sexo_combo = ttk.Combobox(frame, values=["Masculino", "Femenino"], width=28)
sexo_combo.grid(row=5, column=1, pady=5)

tk.Label(frame, text="Localidad", bg="#3b3b3b", fg="white").grid(row=6, column=0, sticky="e", padx=10, pady=5)
localidad_combo = ttk.Combobox(frame, values=["Localidad 1", "Localidad 2", "Localidad 3"], width=28)
localidad_combo.grid(row=6, column=1, pady=5)

tk.Label(frame, text="Club", bg="#3b3b3b", fg="white").grid(row=7, column=0, sticky="e", padx=10, pady=5)
club_combo = ttk.Combobox(frame, values=["Club A", "Club B", "Club C"], width=28)
club_combo.grid(row=7, column=1, pady=5)

guardar_btn = tk.Button(frame, text="Guardar", bg="green", fg="white", width=10, command=validar_campos)
guardar_btn.grid(row=9, column=1, pady=20)

root.mainloop()
