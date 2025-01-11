# Sistema de Tienda Virtual

class Producto:
    def __init__(self, nombre, precio, stock):
        """
        Inicializa un producto con nombre, precio y cantidad en stock.
        
        :param nombre: Nombre del producto.
        :param precio: Precio unitario del producto.
        :param stock: Cantidad disponible en inventario.
        """
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, cantidad):
        """Actualiza el stock del producto tras una compra."""
        if self.stock >= cantidad:
            self.stock -= cantidad
            print(f"{cantidad} unidades de {self.nombre} vendidas. Stock restante: {self.stock}")
        else:
            print(f"Stock insuficiente para {self.nombre}. Disponibles: {self.stock}")

class Carrito:
    def __init__(self):
        """Inicializa un carrito vacío para el cliente."""
        self.items = {}

    def agregar_producto(self, producto, cantidad):
        """
        Agrega un producto al carrito.
        
        :param producto: Instancia de la clase Producto.
        :param cantidad: Cantidad del producto a agregar.
        """
        if producto.stock >= cantidad:
            if producto.nombre in self.items:
                self.items[producto.nombre]['cantidad'] += cantidad
            else:
                self.items[producto.nombre] = {'producto': producto, 'cantidad': cantidad}
            print(f"{cantidad} unidades de {producto.nombre} agregadas al carrito.")
        else:
            print(f"No se puede agregar {cantidad} unidades de {producto.nombre}. Stock insuficiente.")

    def mostrar_carrito(self):
        """Muestra los productos y cantidades en el carrito."""
        print("Carrito de compras:")
        for item in self.items.values():
            producto = item['producto']
            cantidad = item['cantidad']
            print(f"- {producto.nombre}: {cantidad} unidades x ${producto.precio} = ${cantidad * producto.precio}")

    def procesar_compra(self):
        """Procesa la compra de los productos en el carrito."""
        total = 0
        for item in self.items.values():
            producto = item['producto']
            cantidad = item['cantidad']
            producto.actualizar_stock(cantidad)
            total += producto.precio * cantidad
        self.items.clear()
        print(f"Compra procesada con éxito. Total a pagar: ${total}")

# Ejemplo de uso
def sistema_tienda():
    producto1 = Producto("Laptop", 800, 10)
    producto2 = Producto("Mouse", 25, 50)

    carrito = Carrito()
    carrito.agregar_producto(producto1, 2)
    carrito.agregar_producto(producto2, 3)
    carrito.mostrar_carrito()
    carrito.procesar_compra()

# Ejecución de los sistemas
if __name__ == "__main__":
    print("--- Sistema de Reservas de Hotel ---")
    sistema_reservas()
    print("\n--- Sistema de Tienda Virtual ---")
    sistema_tienda()