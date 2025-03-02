import os
import json

# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_info(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

    def to_dict(self):
        return {"id_producto": self.id_producto, "nombre": self.nombre, "cantidad": self.cantidad, "precio": self.precio}

    @staticmethod
    def from_dict(data):
        return Producto(data["id_producto"], data["nombre"], data["cantidad"], data["precio"])

# Clase Inventario
class Inventario:
    FILE_NAME = "inventario.json"

    def __init__(self):
        self.productos = {}
        self.cargar_inventario()

    def guardar_inventario(self):
        try:
            with open(self.FILE_NAME, "w") as file:
                json.dump({id_p: p.to_dict() for id_p, p in self.productos.items()}, file, indent=4)
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def cargar_inventario(self):
        if not os.path.exists(self.FILE_NAME):
            return
        try:
            with open(self.FILE_NAME, "r") as file:
                data = json.load(file)
                self.productos = {id_p: Producto.from_dict(p) for id_p, p in data.items()}
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        if id_producto in self.productos:
            print("Error: El ID del producto ya existe.")
            return
        self.productos[id_producto] = Producto(id_producto, nombre, cantidad, precio)
        self.guardar_inventario()
        print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_inventario()
            print("Producto eliminado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
            self.guardar_inventario()
            print("Producto actualizado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [p.get_info() for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if resultados:
            print("Productos encontrados:")
            for res in resultados:
                print(res)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            print("Inventario actual:")
            for producto in self.productos.values():
                print(producto.get_info())

# Menú de la consola
def menu():
    inventario = Inventario()
    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.agregar_producto(id_producto, nombre, cantidad, precio)
            except ValueError:
                print("Error: Ingrese valores numéricos válidos para cantidad y precio.")
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco si no se cambia): ")
            precio = input("Nuevo precio (dejar en blanco si no se cambia): ")
            try:
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                inventario.actualizar_producto(id_producto, cantidad, precio)
            except ValueError:
                print("Error: Ingrese valores numéricos válidos para cantidad y precio.")
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == "5":
            inventario.mostrar_inventario()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    menu()
