import random

while True:
    user_input = input("Vil du rulle terningen? (Ja/Nei): ").lower()
    
    if user_input == "ja":
        num = random.randint(1, 6)
        print(f"Ditt terningkast er: {num}")
    elif user_input == "nei":
        break
    else:
        print("Vennligst svar med 'Ja' eller 'Nei'.")
