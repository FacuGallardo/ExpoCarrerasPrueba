import tkinter as tk
from tkinter import messagebox

def validar_dni(dni):
    if not dni.isdigit():
        messagebox.showwarning("Error", "Únicamente números en DNI Bobo")
        return False
    return True

def validar_nombre(nombre):
    if not nombre.isalpha():
        messagebox.showwarning("Error", "Nombres van letras únicamente bobo")
        return False
    return True

def validar_telefono(telefono):
    if not telefono.isdigit():
        messagebox.showwarning("Error", "Teléfono va números únicamente bobo")
        return False
    return True

def validar_domicilio(domicilio):
    if not all(c.isalnum() or c.isspace() for c in domicilio):
        messagebox.showwarning("Error", "Domicilio va letras y números únicamente bobo")
        return False
    return True

def validar_ciudad(ciudad):
    if not ciudad.isalpha():
        messagebox.showwarning("Error", "Ciudad va letras únicamente bobo")
        return False
    return True

def validar_carrera(carrera):
    if not carrera.isalpha():
        messagebox.showwarning("Error", "Carrera va letras únicamente bobo")
        return False
    return True
