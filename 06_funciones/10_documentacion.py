#Fabian Vargas
# 26-04-2025

def saludar():
    print("Hola, bienvenido a la clase de Python!")

saludar()

def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(f"La suma es: {resultado}")

def saludar_persona(nombre="Estudiante"):
    print(f"Hola, {nombre}!")

saludar_persona("Fabian")
saludar_persona()

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b else None
    return suma, resta, multiplicacion, division

suma, resta, multiplicacion, division = operaciones_basicas(10, 2)
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}")
