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
    patente = input("Ingrese la patente (6 caracteres): ")
    if not validar_patente(patente):
        print("Patente inválida. Debe tener 6 caracteres.")
        return

    marca = input("Ingrese la marca (mínimo 3 caracteres): ")
    if not validar_marca_modelo(marca):
        print("Marca inválida. Debe tener al menos 3 caracteres.")
        return

    modelo = input("Ingrese el modelo (mínimo 3 caracteres): ")
    if not validar_marca_modelo(modelo):
        print("Modelo inválido. Debe tener al menos 3 caracteres.")
        return

    try:
        año = int(input("Ingrese el año del vehículo (debe ser mayor a 1980): "))
        if not validar_año(año):
            print("Año inválido. Debe ser mayor a 1980.")
            return
    except ValueError:
        print("Año inválido. Debe ser un número entero.")
        return

    try:
        valor = int(input("Ingrese el valor del vehículo (mínimo 500.000): "))
        if not validar_valor(valor):
            print("Valor inválido. Debe ser mayor o igual a 500.000.")
            return
    except ValueError:
        print("Valor inválido. Debe ser un número entero.")
        return

    vehiculos[patente] = {
        "marca": marca,
        "modelo": modelo,
        "año": año,
        "valor": valor,
        "vendido": False
    }
    print("Vehículo guardado exitosamente.")
    guardar_datos_csv(vehiculos)

# buscar un vehículo por su patente
def buscar_vehiculo(vehiculos):
    patente = input("Ingrese la patente del vehículo que desea buscar: ")
    if patente in vehiculos:
        vehiculo = vehiculos[patente]
        print(f"Patente: {patente}")
        print(f"Marca: {vehiculo['marca']}")
        print(f"Modelo: {vehiculo['modelo']}")
        print(f"Año: {vehiculo['año']}")
        print(f"Valor: {vehiculo['valor']}")
        print(f"Estado: {'Vendido' if vehiculo['vendido'] else 'Disponible'}")
        años_desde_fabricacion = datetime.now().year - vehiculo['año']
        print(f"Años desde fabricación: {años_desde_fabricacion}")
    else:
        print("Vehículo no encontrado.")

# listar todos los vehículos
def listar_vehiculos(vehiculos):
    if vehiculos:
        for patente, vehiculo in vehiculos.items():
            print(f"Patente: {patente} - Marca: {vehiculo['marca']} - Modelo: {vehiculo['modelo']} - Año: {vehiculo['año']} - Valor: {vehiculo['valor']} - Estado: {'Vendido' if vehiculo['vendido'] else 'Disponible'}")
    else:
        print("No hay vehículos registrados.")

# imprimir contrato de compraventa
def imprimir_contrato(vehiculos):
    patente = input("Ingrese la patente del vehículo que desea vender: ")
    if patente in vehiculos and not vehiculos[patente]['vendido']:
        vehiculo = vehiculos[patente]
        numero_contrato = datetime.now().strftime("%Y%m%d%H%M%S")
        print(f"Número de contrato: {numero_contrato}")
        print(f"Patente: {patente}")
        print(f"Marca: {vehiculo['marca']}")
        print(f"Modelo: {vehiculo['modelo']}")
        print(f"Año: {vehiculo['año']}")
        print(f"Valor: {vehiculo['valor']}")
        confirmar = input("¿Desea confirmar la venta del vehículo? (si/no): ")
        if confirmar.lower() == "si":
            vehiculo['vendido'] = True
            print("El vehículo ha sido vendido.")
            guardar_datos_csv(vehiculos)
        else:
            print("Venta cancelada.")
    elif patente not in vehiculos:
        print("Vehículo no encontrado.")
    else:
        print("El vehículo ya ha sido vendido.")

# guardar los datos en un archivo CSV
def guardar_datos_csv(vehiculos):
    try:
        with open('vehiculos.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Patente", "Marca", "Modelo", "Año", "Valor", "Vendido"])
            for patente, vehiculo in vehiculos.items():
                writer.writerow([patente, vehiculo["marca"], vehiculo["modelo"], vehiculo["año"], vehiculo["valor"], vehiculo["vendido"]])
        print("Datos guardados en 'vehiculos.csv' con éxito.")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

# Cargar datos desde el archivo CSV
def cargar_datos_csv():
    vehiculos = {}
    try:
        with open('vehiculos.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                vehiculos[row["Patente"]] = {
                    "marca": row["Marca"],
                    "modelo": row["Modelo"],
                    "año": int(row["Año"]),
                    "valor": int(row["Valor"]),
                    "vendido": row["Vendido"] == "True"
                }
    except FileNotFoundError:
        pass
    return vehiculos

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