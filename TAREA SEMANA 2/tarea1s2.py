class Persona:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

    # Método para usar un ítem, que afectará las estadísticas
    def usar_item(self, item):
        item.aplicar_efecto(self)


class Guerrero(Persona):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10"))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Número de arma incorrecta")

    def atributos(self):
        super().atributos()
        print("·Espada:", self.espada)

    def daño(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa


class Mago(Persona):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print("·Libro:", self.libro)

    def daño(self, enemigo):
        return self.inteligencia * self.libro - enemigo.defensa


# Clase para representar ítems que mejoren las estadísticas
class Item:
    def __init__(self, nombre, tipo, incremento_fuerza=0, incremento_inteligencia=0, incremento_defensa=0, incremento_vida=0):
        self.nombre = nombre
        self.tipo = tipo
        self.incremento_fuerza = incremento_fuerza
        self.incremento_inteligencia = incremento_inteligencia
        self.incremento_defensa = incremento_defensa
        self.incremento_vida = incremento_vida

    # El método que aplica los efectos del ítem sobre la persona
    def aplicar_efecto(self, persona):
        persona.fuerza += self.incremento_fuerza
        persona.inteligencia += self.incremento_inteligencia
        persona.defensa += self.incremento_defensa
        persona.vida += self.incremento_vida
        print(f"{persona.nombre} ha usado {self.nombre} y sus estadísticas han mejorado:")
        persona.atributos()


# Ejemplo de combate
def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", jugador_1.nombre, ":", sep="")
        jugador_1.atacar(jugador_2)
        print(">>> Acción de ", jugador_2.nombre, ":", sep="")
        jugador_2.atacar(jugador_1)
        turno += 1
    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")


# Creación de personajes
guerrero = Guerrero("Guts", 20, 10, 4, 100, 4)
mago = Mago("Vanessa", 5, 15, 4, 100, 3)

# Creación de ítems
espada_magica = Item("Espada Mágica", "arma", incremento_fuerza=10)
pocion_de_vida = Item("Poción de Vida", "poción", incremento_vida=50)

# Mostrar atributos antes de usar ítems
guerrero.atributos()
mago.atributos()

# Usar ítem para mejorar estadísticas
guerrero.usar_item(espada_magica)  # El guerrero usa la espada mágica
mago.usar_item(pocion_de_vida)    # El mago usa la poción de vida

# Mostrar atributos después de usar ítems
guerrero.atributos()
mago.atributos()

# Simulación de combate
combate(guerrero, mago)
