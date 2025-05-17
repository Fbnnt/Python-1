# Fabian Vargas
#17-05-2025


calificacion = int(input("Ingresa tu calificación (0-100): "))

if calificacion >= 90:
    print("Excelente, tienes una A.")
elif calificacion >= 80:
    print("Muy bien, tienes una B.")
elif calificacion >= 70:
    print("Bien, tienes una C.")
elif calificacion >= 60:
    print("Pasaste, tienes una D.")
else:
    print("Reprobaste, tienes una F.")

