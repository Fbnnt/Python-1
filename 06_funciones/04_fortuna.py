#Fabian Vargas
# 14-04-2025
def fortuna():
    #del 1 al 8
    numero = int(input("Elige un número del 1 al 8: "))

    # Validar 
    if numero < 1 or numero > 8:
        print("Por favor, elige un número válido entre 1 y 8.")
        return

    # Mostrar el mensaje correspondiente
    if numero == 1:
        print("No persigas la felicidad, créala.")
    elif numero == 2:
        print("Todas las cosas son difíciles antes de ser fáciles.")
    elif numero == 3:
        print("El pájaro madrugador consigue el gusano, pero el segundo ratón se lleva el queso.")
    elif numero == 4:
        print("Alguien en tu vida necesita una carta de tu parte.")
    elif numero == 5:
        print("No solo pienses, ¡actúa!")
    elif numero == 6:
        print("TU corazón es una brújula.")
    elif numero == 7:
        print("La fortuna que buscas está en otra galleta.")
    elif numero == 8:
        print("¡Ayuda! ¡Estoy prisionero en una panadería china!")

fortuna()