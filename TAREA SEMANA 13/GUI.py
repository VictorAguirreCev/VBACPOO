import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas Diarias")
root.geometry("400x400")

# Función para agregar una tarea
def agregar_tarea():
    tarea = entry_tarea.get()
    if tarea != "":
        listbox_tareas.insert(tk.END, tarea)  # Agregar la tarea a la lista
        entry_tarea.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

# Función para marcar una tarea como completada
def marcar_completada():
    try:
        tarea_seleccionada = listbox_tareas.curselection()  # Obtener la tarea seleccionada
        tarea = listbox_tareas.get(tarea_seleccionada)  # Obtener el texto de la tarea
        listbox_tareas.delete(tarea_seleccionada)  # Eliminar la tarea de la lista
        listbox_tareas.insert(tk.END, tarea + " (Completada)")  # Agregarla como completada
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")

# Función para eliminar una tarea
def eliminar_tarea():
    try:
        tarea_seleccionada = listbox_tareas.curselection()  # Obtener la tarea seleccionada
        listbox_tareas.delete(tarea_seleccionada)  # Eliminar la tarea seleccionada
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")

# Función para limpiar la lista de tareas
def limpiar_lista():
    listbox_tareas.delete(0, tk.END)

# Etiquetas y componentes GUI
label_instrucciones = tk.Label(root, text="Ingrese una tarea y haga clic en Agregar:")
label_instrucciones.pack(pady=10)

entry_tarea = tk.Entry(root, width=40)
entry_tarea.pack(pady=5)

button_agregar = tk.Button(root, text="Agregar Tarea", command=agregar_tarea)
button_agregar.pack(pady=5)

button_marcar_completada = tk.Button(root, text="Marcar como Completada", command=marcar_completada)
button_marcar_completada.pack(pady=5)

button_eliminar = tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea)
button_eliminar.pack(pady=5)

button_limpiar = tk.Button(root, text="Limpiar Lista", command=limpiar_lista)
button_limpiar.pack(pady=5)

# Lista para mostrar las tareas
listbox_tareas = tk.Listbox(root, height=10, width=40)
listbox_tareas.pack(pady=10)

# Iniciar la aplicación
root.mainloop()
