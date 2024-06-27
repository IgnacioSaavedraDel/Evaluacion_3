import csv
from datetime import datetime
import os

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

# validar datos
def validar_patente(patente):
    return len(patente) == 6

def validar_marca_modelo(nombre):
    return len(nombre) >= 3

def validar_año(año):
    return año > 1980

def validar_valor(valor):
    return valor >= 500000

# guardar los datos del vehículo
def guardar_vehiculo(vehiculos):
    pass

# buscar un vehículo por su patente
def buscar_vehiculo(vehiculos):
    pass

# listar todos los vehículos
def listar_vehiculos(vehiculos):
    pass

# imprimir contrato de compraventa
def imprimir_contrato(vehiculos):
    pass

# guardar los datos en un archivo CSV
def guardar_datos_csv(vehiculos):
    pass

# Cargar datos desde el archivo CSV
def cargar_datos_csv():
    pass

# menú
def menu():
    vehiculos = cargar_datos_csv()
    while True:
        print("\nMenú de opciones:")
        print("1. Guardar")
        print("2. Buscar")
        print("3. Listar")
        print("4. Imprimir contrato")
        print("5. Salir")
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                guardar_vehiculo(vehiculos)
            elif opcion == 2:
                buscar_vehiculo(vehiculos)
            elif opcion == 3:
                listar_vehiculos(vehiculos)
            elif opcion == 4:
                imprimir_contrato(vehiculos)
            elif opcion == 5:
                print("Saliendo de la aplicación...")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
        except ValueError as e:
            print(f"Error: {e}. Por favor ingrese valores numéricos válidos.")

# arracna menu
if __name__ == "__main__":
    clearscreen()
    menu()