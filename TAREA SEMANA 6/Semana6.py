# -*- coding: utf-8 -*-

# Clase base: Persona
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo protegido (encapsulación)
        self._edad = edad

    def presentarse(self):
        return f"Hola, me llamo {self._nombre} y tengo {self._edad} años."

# Clase derivada: Estudiante
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self._carrera = carrera

    # Sobrescritura de método (Polimorfismo)
    def presentarse(self):
        return f"Hola, me llamo {self._nombre}, tengo {self._edad} años y estudio {self._carrera}."

    def estudiar(self):
        return f"{self._nombre} está estudiando {self._carrera}."

# Clase derivada: Profesor
class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self._materia = materia

    # Sobrescritura de método (Polimorfismo)
    def presentarse(self):
        return f"Hola, me llamo {self._nombre}, tengo {self._edad} años y enseño {self._materia}."

    def enseñar(self):
        return f"{self._nombre} está enseñando {self._materia}."

# Programa principal
if __name__ == "__main__":
    # Crear instancias
    estudiante = Estudiante("Ana", 20, "Ingeniería de Software")
    profesor = Profesor("Luis", 45, "Programación en Python")

    print(estudiante.presentarse())
    print(estudiante.estudiar())  # Método específico de Estudiante

    print(profesor.presentarse())
    print(profesor.enseñar())  # Método específico de Profesor

    personas = [estudiante, profesor]
    for persona in personas:
        print(persona.presentarse())  # Llamada polimórfica
