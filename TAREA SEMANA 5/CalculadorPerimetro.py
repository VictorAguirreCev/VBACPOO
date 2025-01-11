# Programa para calcular el área y el perímetro de un rectángulo.
# Descripción: Este programa solicita las dimensiones de un rectángulo al usuario, valida los datos de entrada,
#              y calcula el área y el perímetro, mostrando los resultados en pantalla.

def calcular_area(base: float, altura: float) -> float:
    """Calcula el área de un rectángulo."""
    return base * altura


def calcular_perimetro(base: float, altura: float) -> float:
    """Calcula el perímetro de un rectángulo."""
    return 2 * (base + altura)


def dimensiones_validas(base: float, altura: float) -> bool:
    """Verifica si las dimensiones ingresadas son mayores que cero."""
    return base > 0 and altura > 0


def main():
    print("Calculadora de área y perímetro de un rectángulo")
    try:
        base = float(input("Ingresa la base del rectángulo: "))
        altura = float(input("Ingresa la altura del rectángulo: "))

        if dimensiones_validas(base, altura):
            area = calcular_area(base, altura)
            perimetro = calcular_perimetro(base, altura)
            print(f"\nResultados:")
            print(f"Área: {area:.2f}")
            print(f"Perímetro: {perimetro:.2f}")
        else:
            print("Error: Las dimensiones deben ser mayores que cero.")
    except ValueError:
        print("Error: Por favor, ingresa valores numéricos válidos.")


if __name__ == "__main__":
    main()
