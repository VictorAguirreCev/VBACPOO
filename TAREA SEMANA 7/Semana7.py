# Clase para gestionar reservas en una biblioteca
class ReservaBiblioteca:
    # Constructor: inicializa los atributos del objeto
    def __init__(self, usuario, libro):
        self.usuario = usuario
        self.libro = libro
        print(f"Reserva creada: {self.usuario} ha reservado el libro '{self.libro}'.")

    # Destructor: se ejecuta al eliminar el objeto
    def __del__(self):
        print(f"Reserva eliminada: {self.usuario} ha devuelto el libro '{self.libro}'.")

# Clase para gestionar la biblioteca
class Biblioteca:
    def __init__(self):
        self.reservas = []  # Lista para almacenar reservas
        print("Sistema de gestión de reservas iniciado.")

    def crear_reserva(self, usuario, libro):
        reserva = ReservaBiblioteca(usuario, libro)
        self.reservas.append(reserva)

    def mostrar_reservas(self):
        if not self.reservas:
            print("No hay reservas activas.")
        else:
            print("Reservas activas:")
            for reserva in self.reservas:
                print(f"- Usuario: {reserva.usuario}, Libro: {reserva.libro}")

    def eliminar_reserva(self, usuario, libro):
        for reserva in self.reservas:
            if reserva.usuario == usuario and reserva.libro == libro:
                self.reservas.remove(reserva)
                del reserva  # Activar el destructor
                print(f"Reserva eliminada: {usuario} devolvió el libro '{libro}'.")
                return
        print(f"No se encontró la reserva del libro '{libro}' para el usuario '{usuario}'.")

    def __del__(self):
        print("Sistema de gestión de reservas cerrado.")



# Ejemplo de uso del programa
if __name__ == "__main__":
    # Crear instancia de la biblioteca
    biblioteca = Biblioteca()

    # Crear reservas
    biblioteca.crear_reserva("Juan Pérez", "El Principito")
    biblioteca.crear_reserva("Ana Gómez", "Cien años de soledad")

    # Mostrar reservas activas
    biblioteca.mostrar_reservas()

    # Eliminar una reserva
    biblioteca.eliminar_reserva("Juan Pérez", "El Principito")

    # Mostrar reservas después de eliminar una
    biblioteca.mostrar_reservas()
