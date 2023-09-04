# Initialiserer en variabel for å holde summen av tallene
total_sum = 0

# Ber brukeren om å skrive inn fem tall og legger dem til total_sum
for i in range(5):
    try:
        num = float(input(f"Skriv inn tall {i+1}: "))
        total_sum += num
    except ValueError:
        print("Ugyldig inndata. Vennligst skriv inn et gyldig tall.")

# Beregner gjennomsnittet
average = total_sum / 5

# Skriver ut gjennomsnittet
print(f"Gjennomsnittet av tallene er: {average}")
