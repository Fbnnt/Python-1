#Fabian vargas
#31-03-2025
# Programa de la bola 8 mágica
# Este programa simula una bola 8 mágica que responde a preguntas de sí o no.
import random

# Lista de posibles respuestas
respuestas = [
    "Sí, definitivamente",
    "Es cierto",
    "Sin duda",
    "No lo creo",
    "Mi respuesta es no",
    "Mis fuentes dicen que no",
    "Mejor no decirte ahora",
    "Pregunta de nuevo más tarde",
    "No puedo predecirlo ahora"
]

pregunta = input("Pregunta: ")

respuesta = random.choice(respuestas)

print(f"Respuesta: {respuesta}")