import tkinter as tk
from tkinter import messagebox

# Lista simulada de jugadores (Nombre, Apellido, Equipo, Posición)
jugadores = [
    {'nombre': 'Juan', 'apellido': 'Pérez', 'equipo': 'A', 'posición': 'Portero'},
    {'nombre': 'Carlos', 'apellido': 'Gómez', 'equipo': 'B', 'posición': 'Defensa'},
    {'nombre': 'Luis', 'apellido': 'Martínez', 'equipo': 'C', 'posición': 'Delantero'}
]

# Función para listar jugadores en el Listbox
def listar_jugadores():
    lista.delete(0, tk.END)
    for i, jugador in enumerate(jugadores):
        lista.insert(tk.END, f"{i+1}. {jugador['nombre']} {jugador['apellido']} - {jugador['equipo']} - {jugador['posición']}")

# Función para modificar un jugador
def modificar_jugador():
    seleccion = lista.curselection()
    if not seleccion:
        messagebox.showwarning("Advertencia", "Por favor, selecciona un jugador.")
        return

    idx = seleccion[0]
    jugador = jugadores[idx]

    # Mostrar una nueva ventana para modificar el jugador
    ventana_modificar = tk.Toplevel()
    ventana_modificar.title("Modificar Jugador")

    tk.Label(ventana_modificar, text="Nombre:").grid(row=0, column=0)
    tk.Label(ventana_modificar, text="Apellido:").grid(row=1, column=0)
    tk.Label(ventana_modificar, text="Equipo:").grid(row=2, column=0)
    tk.Label(ventana_modificar, text="Posición:").grid(row=3, column=0)

    # Crear campos de texto con los valores actuales del jugador
    entry_nombre = tk.Entry(ventana_modificar)
    entry_nombre.grid(row=0, column=1)
    entry_nombre.insert(0, jugador['nombre'])

    entry_apellido = tk.Entry(ventana_modificar)
    entry_apellido.grid(row=1, column=1)
    entry_apellido.insert(0, jugador['apellido'])

    entry_equipo = tk.Entry(ventana_modificar)
    entry_equipo.grid(row=2, column=1)
    entry_equipo.insert(0, jugador['equipo'])

    entry_posicion = tk.Entry(ventana_modificar)
    entry_posicion.grid(row=3, column=1)
    entry_posicion.insert(0, jugador['posición'])

    # Función para guardar los cambios
    def guardar_cambios():
        jugadores[idx]['nombre'] = entry_nombre.get()
        jugadores[idx]['apellido'] = entry_apellido.get()
        jugadores[idx]['equipo'] = entry_equipo.get()
        jugadores[idx]['posición'] = entry_posicion.get()

        listar_jugadores()  # Actualizar la lista
        ventana_modificar.destroy()  # Cerrar la ventana de modificación
        messagebox.showinfo("Éxito", "Jugador modificado correctamente.")

    tk.Button(ventana_modificar, text="Guardar", command=guardar_cambios).grid(row=4, column=1)

# Crear la ventana principal
root = tk.Tk()
root.title("ABM Jugadores - Liga Handball Punilla")

# Crear Listbox para mostrar jugadores
lista = tk.Listbox(root, width=50, height=10)
lista.grid(row=0, column=0, padx=10, pady=10)
listar_jugadores()

# Botón para modificar jugador
btn_modificar = tk.Button(root, text="Modificar Jugador", command=modificar_jugador)
btn_modificar.grid(row=1, column=0, padx=10, pady=10)

# Ejecutar la aplicación
root.mainloop()
