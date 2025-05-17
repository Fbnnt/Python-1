#Fabian Vargas
# 26-04-2025
menu = [
    "1. Pizza Margherita",
    "2. Spaghetti Carbonara",
    "3. Lasaña",
    "4. Risotto de hongos",
    "5. Ensalada César",
    "6. Tiramisu",
    "7. Espresso",
    "8. Agua con gas",
    ]
def obtener_articulo(n: int):
    print(menu[n-1])

def bienvenida():
    print("Bienvenido a Auto Servicio Italiano")
    print("Por favor, elija una opción del menú:")

    for item in menu:
        print(item)
    
    n = int(input("Ingrese el número del artículo que desea: "))
    while n < 1 or n > len(menu):
        print("Número inválido. Por favor, elija un número del menú.")
    n = int(input("Ingrese el número del artículo que desea: "))
    print("Usted ha elegido el artículo número:", n)
    obtener_articulo(n)

bienvenida()
