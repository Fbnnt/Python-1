# Fabian Vargas
#17-05-2025
respuesta = input("¿Estas cansado? (y/n): ").strip().lower()

cansado = respuesta == "y"

if not cansado:
    print("No te preocupes, sigue así")
else: 
    print("Estás cansado, te recomiendo descansar")
