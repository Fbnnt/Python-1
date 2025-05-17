# Fabian Vargas
#17-05-2025

altura = int(input("Ingrese su altura en cm: "))
creditos = int(input("Ingrese la cantidad de créditos que tiene: "))

if altura >= 137 and creditos >= 10:
    print("¡Disfruta el viaje!")
elif creditos >= 10:
    print("No eres lo suficientemente alto para viajar.")
elif altura >= 137:
    print("No tiene suficientes créditos.")
else:
    print("No has cumplido ninguno de los requisitos.")