# Sistema de Reservas de Hotel

class Habitacion:
    def __init__(self, numero, capacidad, precio):
        """
        Inicializa una habitación con su número, capacidad, precio y estado de disponibilidad.
        
        :param numero: Número identificador de la habitación.
        :param capacidad: Número máximo de huéspedes que pueden ocupar la habitación.
        :param precio: Precio por noche de la habitación.
        """
        self.numero = numero
        self.capacidad = capacidad
        self.precio = precio
        self.disponible = True

    def reservar(self):
        """Reserva la habitación si está disponible."""
        if self.disponible:
            self.disponible = False
            print(f"Habitación {self.numero} reservada con éxito.")
        else:
            print(f"La habitación {self.numero} no está disponible.")

    def cancelar_reserva(self):
        """Cancela la reserva de la habitación si no está disponible."""
        if not self.disponible:
            self.disponible = True
            print(f"Reserva de la habitación {self.numero} cancelada.")
        else:
            print(f"La habitación {self.numero} ya está disponible.")

class Cliente:
    def __init__(self, nombre, telefono):
        """
        Inicializa un cliente con su nombre y número de teléfono.
        
        :param nombre: Nombre completo del cliente.
        :param telefono: Número de teléfono del cliente.
        """
        self.nombre = nombre
        self.telefono = telefono

    def realizar_reserva(self, habitacion):
        """Permite al cliente intentar reservar una habitación."""
        print(f"{self.nombre} está intentando reservar la habitación {habitacion.numero}.")
        habitacion.reservar()

    def cancelar_reserva(self, habitacion):
        """Permite al cliente cancelar la reserva de una habitación."""
        print(f"{self.nombre} está intentando cancelar la reserva de la habitación {habitacion.numero}.")
        habitacion.cancelar_reserva()

# Ejemplo de uso
def sistema_reservas():
    habitacion1 = Habitacion(101, 2, 50)
    cliente1 = Cliente("Juan Pérez", "123456789")

    cliente1.realizar_reserva(habitacion1)
    cliente1.realizar_reserva(habitacion1)  # Intento de doble reserva
    cliente1.cancelar_reserva(habitacion1)
    cliente1.cancelar_reserva(habitacion1)  # Intento de doble cancelación