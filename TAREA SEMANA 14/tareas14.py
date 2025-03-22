import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import datetime

class AgendaPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("700x400")
        self.root.resizable(False, False)

        # -------- Frame para visualización de eventos --------
        self.frame_eventos = ttk.Frame(self.root, padding="10")
        self.frame_eventos.pack(fill='both', expand=True)

        self.tree = ttk.Treeview(self.frame_eventos, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.column("Fecha", width=100, anchor="center")
        self.tree.column("Hora", width=80, anchor="center")
        self.tree.column("Descripción", width=400)
        self.tree.pack(fill='both', expand=True, pady=10)

        # -------- Frame para entrada de datos --------
        self.frame_entrada = ttk.Frame(self.root, padding="10")
        self.frame_entrada.pack(fill='x')

        # Etiqueta y campo de entrada para fecha con DatePicker
        ttk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.fecha_entry = DateEntry(self.frame_entrada, date_pattern='yyyy-mm-dd', width=12)
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        # Etiqueta y campo de entrada para hora
        ttk.Label(self.frame_entrada, text="Hora (HH:MM):").grid(row=0, column=2, padx=5, pady=5)
        self.hora_entry = ttk.Entry(self.frame_entrada, width=10)
        self.hora_entry.grid(row=0, column=3, padx=5, pady=5)

        # Etiqueta y campo de entrada para descripción
        ttk.Label(self.frame_entrada, text="Descripción:").grid(row=0, column=4, padx=5, pady=5)
        self.descripcion_entry = ttk.Entry(self.frame_entrada, width=30)
        self.descripcion_entry.grid(row=0, column=5, padx=5, pady=5)

        # -------- Frame para botones --------
        self.frame_botones = ttk.Frame(self.root, padding="10")
        self.frame_botones.pack(fill='x')

        ttk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento).pack(side='left', padx=10)
        ttk.Button(self.frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).pack(side='left', padx=10)
        ttk.Button(self.frame_botones, text="Salir", command=self.root.quit).pack(side='right', padx=10)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        # Validar que todos los campos estén completos
        if not fecha or not hora or not descripcion:
            messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos.")
            return

        # Validar formato de hora
        try:
            datetime.datetime.strptime(hora, "%H:%M")
        except ValueError:
            messagebox.showerror("Formato incorrecto", "La hora debe estar en formato HH:MM.")
            return

        # Insertar en Treeview
        self.tree.insert('', 'end', values=(fecha, hora, descripcion))
        self.limpiar_campos()

    def eliminar_evento(self):
        item = self.tree.selection()
        if not item:
            messagebox.showwarning("Ningún evento seleccionado", "Selecciona un evento para eliminar.")
            return

        respuesta = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de que deseas eliminar este evento?")
        if respuesta:
            self.tree.delete(item)

    def limpiar_campos(self):
        self.hora_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)
        self.fecha_entry.set_date(datetime.date.today())

# -------- Inicialización de la aplicación --------
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()
