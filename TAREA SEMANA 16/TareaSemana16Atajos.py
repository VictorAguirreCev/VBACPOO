import tkinter as tk
from tkinter import messagebox, simpledialog, font

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f0f0")

        # Fuente personalizada para tareas
        self.task_font = font.Font(family="Helvetica", size=12)

        # Campo de entrada
        self.entry = tk.Entry(self.root, font=self.task_font, width=30)
        self.entry.pack(pady=10)
        self.entry.focus_set()

        # Botones
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=5)

        self.add_button = tk.Button(button_frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=5)

        self.complete_button = tk.Button(button_frame, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(button_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, font=self.task_font, width=45, height=10)
        self.task_listbox.pack(pady=10)

        # Vincular atajos de teclado
        self.root.bind("<Return>", lambda event: self.add_task())
        self.root.bind("<c>", lambda event: self.complete_task())
        self.root.bind("<C>", lambda event: self.complete_task())
        self.root.bind("<Delete>", lambda event: self.delete_task())
        self.root.bind("<d>", lambda event: self.delete_task())
        self.root.bind("<D>", lambda event: self.delete_task())
        self.root.bind("<Escape>", lambda event: self.root.quit())

        # Tareas y su estado (True = completada)
        self.tasks = []

    def add_task(self):
        task_text = self.entry.get().strip()
        if task_text:
            self.tasks.append((task_text, False))  # (texto, estado)
            self.entry.delete(0, tk.END)
            self.update_task_list()
        else:
            messagebox.showwarning("Advertencia", "Escriba una tarea antes de añadir.")

    def complete_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            task_text, _ = self.tasks[index]
            self.tasks[index] = (task_text, True)
            self.update_task_list()
        else:
            messagebox.showinfo("Información", "Seleccione una tarea para marcar como completada.")

    def delete_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            del self.tasks[index]
            self.update_task_list()
        else:
            messagebox.showinfo("Información", "Seleccione una tarea para eliminar.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task_text, is_completed in self.tasks:
            display_text = f"✔️ {task_text}" if is_completed else task_text
            self.task_listbox.insert(tk.END, display_text)
            if is_completed:
                self.task_listbox.itemconfig(tk.END, fg="gray", font=self.task_font.copy().configure(overstrike=1))
            else:
                self.task_listbox.itemconfig(tk.END, fg="black", font=self.task_font.copy().configure(overstrike=0))

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
