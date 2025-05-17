# Fabian Vargas
# 17-05-2025

houses = {"Gryffindor": 0, "Ravenclaw": 0, "Hufflepuff": 0, "Slytherin": 0}

def ask_question(question, options, scores):
    print("\n" + question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        try:
            choice = int(input("\nElige una opción: "))
            if 1 <= choice <= len(options):
                for house, points in scores[choice - 1].items():
                    houses[house] += points
                break
            else:
                print("Entrada incorrecta. Por favor, elige una opción válida.")
        except ValueError:
            print("Entrada incorrecta. Por favor, ingresa un número.")

print("=" * 65)
print(" " * 10, "⭐🎩 Bienvenido al el Sombrero Seleccionador 🎩⭐", " " * 10)
print("=" * 65)

ask_question(
    "P1) ¿Te gusta más el amanecer o el atardecer?",
    ["Amanecer", "Atardecer"],
    [{"Gryffindor": 1, "Ravenclaw": 1}, {"Hufflepuff": 1, "Slytherin": 1}]
)

ask_question(
    "P2) Cuando muera, quiero que la gente me recuerde como:",
    ["El bueno", "El grandioso", "El sabio", "El valiente"],
    [
        {"Hufflepuff": 2},
        {"Slytherin": 2},
        {"Ravenclaw": 2},
        {"Gryffindor": 2}
    ]
)

ask_question(
    "P3) ¿Qué tipo de instrumento complace más a tu oído?",
    ["El violín", "La trompeta", "El piano", "El tambor"],
    [
        {"Slytherin": 4},
        {"Hufflepuff": 4},
        {"Ravenclaw": 4},
        {"Gryffindor": 4}
    ]
)

winning_house = max(houses, key=houses.get)
print("\n" + "-" * 65)
print(f"\nEl Sombrero Seleccionador te ha asignado a: {winning_house} {'🦁' if winning_house == 'Gryffindor' else '🐦‍⬛' if winning_house == 'Ravenclaw' else '🦡' if winning_house == 'Hufflepuff' else '🐍'}")
print("\n" + "-" * 65)
