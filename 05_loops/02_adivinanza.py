#Fabian Vargas 
#07-04-2025
Adivinanza = 0

while adivinanza != 6:
    adivinanza = int(input('Adivina el número: '))

adivinanza = 0
intentos = 0

while adivinanza != 6 and intentos > 5:
    adivinanza = int(input('Adivina el número: '))
    intentos += 1
if adivinanza != 6:
    print("Te quedaste sin intentos")