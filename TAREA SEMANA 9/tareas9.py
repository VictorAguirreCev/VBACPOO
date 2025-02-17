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
            print("Error: El ID del producto ya existe.")
            return
        nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                self.productos.remove(producto)
                print("Producto eliminado correctamente.")
                return
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                print("Producto actualizado correctamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [p.get_info() for p in self.productos if nombre.lower() in p.nombre.lower()]
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
            for producto in self.productos:
                print(producto.get_info())


# Menú de la consola
def menu():
    inventario = Inventario()
    while True:
        print("\n--- Sistema de Gestión de Inventarios - Le Alcanza ---")
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
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(id_producto, nombre, cantidad, precio)
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco si no se cambia): ")
            precio = input("Nuevo precio (dejar en blanco si no se cambia): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
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
