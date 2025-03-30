import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        # Lista para almacenar tareas y su estado (texto, completada)
        self.tasks = []

        # Entrada de nueva tarea
        self.task_entry = tk.Entry(root, font=("Arial", 14))
        self.task_entry.pack(pady=10, padx=20, fill=tk.X)
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        # Botones
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)

        self.add_button = tk.Button(self.button_frame, text="Añadir Tarea", width=15, command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=5)

        self.complete_button = tk.Button(self.button_frame, text="Marcar como Completada", width=20,
                                         command=self.mark_completed)
        self.complete_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Eliminar Tarea", width=15, command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=("Arial", 12), activestyle='none')
        self.task_listbox.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        self.task_listbox.bind("<Double-Button-1>", lambda event: self.mark_completed())

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text == "":
            messagebox.showwarning("Entrada Vacía", "Por favor, escribe una tarea.")
            return

        self.tasks.append((task_text, False))  # False indica que no está completada
        self.update_task_list()
        self.task_entry.delete(0, tk.END)

    def mark_completed(self):
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showinfo("Sin selección", "Selecciona una tarea para marcar como completada.")
            return

        index = selected[0]
        task_text, completed = self.tasks[index]
        self.tasks[index] = (task_text, not completed)  # Alterna el estado
        self.update_task_list()

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showinfo("Sin selección", "Selecciona una tarea para eliminar.")
            return

        index = selected[0]
        del self.tasks[index]
        self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task_text, completed in self.tasks:
            display_text = f"✔ {task_text}" if completed else task_text
            self.task_listbox.insert(tk.END, display_text)
            if completed:
                self.task_listbox.itemconfig(tk.END, fg="gray")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
