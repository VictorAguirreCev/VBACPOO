import os
import subprocess
from tabulate import tabulate
from colorama import Fore, Style, init

# Inicializa colorama para Windows
init(autoreset=True)

# Definir las opciones del menú
dashboard_opciones = {
    '1': ('TAREA SEMANA 2', 'Tareas/Tarea_Semana_2.py'),
    '2': ('TAREA SEMANA 3', 'Tareas/Tarea_Semana_3.py'),
    '3': ('TAREA SEMANA 5', 'Tareas/Tarea_Semana_5.py'),
    '4': ('TAREA SEMANA 6', 'Tareas/Tarea_Semana_6.py'),
    '5': ('TAREA SEMANA 7', 'Tareas/Tarea_Semana_7.py'),
    '6': ('TAREA SEMANA 8', 'Tareas/Tarea_Semana_8.py')
}


# Función para mostrar el menú en formato tabla
def mostrar_menu():
    print(Fore.CYAN + "\n******** DASHBOARD INTERACTIVO ********")
    tabla = [[key, val[0]] for key, val in dashboard_opciones.items()]
    print(tabulate(tabla, headers=["Opción", "Descripción"], tablefmt="fancy_grid"))
    print(Fore.RED + "0 - Salir")


# Función para mostrar el código del script seleccionado
def mostrar_codigo(ruta_script):
    try:
        with open(ruta_script, 'r') as archivo:
            print(Fore.YELLOW + f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
            registrar_log(f"Código mostrado: {ruta_script}")
    except FileNotFoundError:
        print(Fore.RED + "Error: El archivo no se encontró.")
    except Exception as e:
        print(Fore.RED + f"Ocurrió un error al leer el archivo: {e}")


# Función para ejecutar el script seleccionado
def ejecutar_script(ruta_script):
    try:
        print(Fore.GREEN + f"Ejecutando {ruta_script}...\n")
        subprocess.run(["python", ruta_script], check=True)
        registrar_log(f"Ejecutado: {ruta_script}")
    except Exception as e:
        print(Fore.RED + f"Error al ejecutar el script: {e}")


# Función para registrar las acciones en un log
def registrar_log(mensaje):
    with open("log.txt", "a") as log:
        log.write(mensaje + "\n")


# Bucle principal del menú
if __name__ == "__main__":
    ruta_base = os.path.dirname(__file__)
    while True:
        mostrar_menu()
        opcion = input(Fore.BLUE + "\nSelecciona una opción: ")

        if opcion == '0':
            print(Fore.MAGENTA + "Saliendo del Dashboard... ¡Hasta luego!")
            break
        elif opcion in dashboard_opciones:
            descripcion, ruta_relativa = dashboard_opciones[opcion]
            ruta_completa = os.path.join(ruta_base, ruta_relativa)

            print(Fore.YELLOW + f"\nHas seleccionado: {descripcion}")
            accion = input("¿Qué deseas hacer? (1 - Ver Código, 2 - Ejecutar): ")

            if accion == '1':
                mostrar_codigo(ruta_completa)
            elif accion == '2':
                ejecutar_script(ruta_completa)
            else:
                print(Fore.RED + "Opción no válida.")
        else:
            print(Fore.RED + "Opción inválida, intenta de nuevo.")