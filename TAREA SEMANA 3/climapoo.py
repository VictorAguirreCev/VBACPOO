class Clima:
    def __init__(self):
        self.temperaturas = []  # Atributo para almacenar las temperaturas diarias

    # Método para ingresar las temperaturas diarias
    def ingresar_temperaturas(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            self.temperaturas.append(temp)

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

# Clase principal para gestionar el clima semanal
class ClimaSemanal:
    def __init__(self):
        self.clima = Clima()  # Instanciamos la clase Clima

    # Método para calcular y mostrar el promedio semanal
    def mostrar_promedio(self):
        self.clima.ingresar_temperaturas()  # Pedir las temperaturas
        promedio = self.clima.calcular_promedio()  # Calcular el promedio
        print(f"El promedio semanal del clima es: {promedio:.2f}°C")

# Llamada a la clase para ejecutar el programa
if __name__ == "__main__":
    clima_semanal = ClimaSemanal()  # Creamos una instancia de ClimaSemanal
    clima_semanal.mostrar_promedio()  # Mostrar el promedio semanal
