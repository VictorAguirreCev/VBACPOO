import tkinter as tk
from tkinter import messagebox

# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_info(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        if any(p.id_producto == id_producto for p in self.productos):
            messagebox.showerror("Error", "El ID del producto ya existe.")
            return
        nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        messagebox.showinfo("Éxito", "Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                self.productos.remove(producto)
                messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
                return
        messagebox.showerror("Error", "Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
                return
        messagebox.showerror("Error", "Producto no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [p.get_info() for p in self.productos if nombre.lower() in p.nombre.lower()]
        if resultados:
            messagebox.showinfo("Resultados", "\n".join(resultados))
        else:
            messagebox.showerror("Error", "No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        if not self.productos:
            messagebox.showinfo("Inventario", "Inventario vacío.")
        else:
            inventario_texto = "\n".join(p.get_info() for p in self.productos)
            messagebox.showinfo("Inventario", inventario_texto)

# Interfaz Gráfica
class App:
    def __init__(self, root):
        self.inventario = Inventario()
        self.root = root
        self.root.title("Gestión de Inventarios - Le Alcanza")
        
        tk.Label(root, text="ID del producto:").pack()
        self.id_entry = tk.Entry(root)
        self.id_entry.pack()
        
        tk.Label(root, text="Nombre del producto:").pack()
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.pack()
        
        tk.Label(root, text="Cantidad:").pack()
        self.cantidad_entry = tk.Entry(root)
        self.cantidad_entry.pack()
        
        tk.Label(root, text="Precio:").pack()
        self.precio_entry = tk.Entry(root)
        self.precio_entry.pack()
        
        tk.Button(root, text="Agregar Producto", command=self.agregar_producto).pack()
        tk.Button(root, text="Eliminar Producto", command=self.eliminar_producto).pack()
        tk.Button(root, text="Actualizar Producto", command=self.actualizar_producto).pack()
        tk.Button(root, text="Buscar Producto", command=self.buscar_producto).pack()
        tk.Button(root, text="Mostrar Inventario", command=self.mostrar_inventario).pack()

    def agregar_producto(self):
        self.inventario.agregar_producto(self.id_entry.get(), self.nombre_entry.get(), int(self.cantidad_entry.get()), float(self.precio_entry.get()))

    def eliminar_producto(self):
        self.inventario.eliminar_producto(self.id_entry.get())
    
    def actualizar_producto(self):
        cantidad = self.cantidad_entry.get()
        precio = self.precio_entry.get()
        cantidad = int(cantidad) if cantidad else None
        precio = float(precio) if precio else None
        self.inventario.actualizar_producto(self.id_entry.get(), cantidad, precio)
    
    def buscar_producto(self):
        self.inventario.buscar_producto(self.nombre_entry.get())
    
    def mostrar_inventario(self):
        self.inventario.mostrar_inventario()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
