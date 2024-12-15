# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal
def main():
    temperaturas = ingresar_temperaturas()  # Se ingresan las temperaturas
    promedio = calcular_promedio(temperaturas)  # Se calcula el promedio semanal
    print(f"El promedio semanal del clima es: {promedio:.2f}°C")

# Llamada a la función principal
if __name__ == "__main__":
    main()
