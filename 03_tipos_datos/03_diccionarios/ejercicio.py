# Fabian Vargas
#22-04-2025

texto = input("Ingresa un texto: ")
palabras = texto.split()
frecuencia_palabras = {}
for palabra in palabras:
    palabra = palabra.lower()
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1
print("Frecuencia de palabras:")
for palabra, frecuencia in frecuencia_palabras.items():
    print(f"{palabra}: {frecuencia}")
