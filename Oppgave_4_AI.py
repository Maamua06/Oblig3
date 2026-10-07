# 1. Definerer funksjonen med tre parametere og returverdi
def regn_ut_volum(lengde, bredde, hoyde):
    volum = lengde * bredde * hoyde
    return volum

# 2. Kaller funksjonen med tre ulike sett av verdier og skriver ut resultatene

# Eksempel 1:
volum1 = regn_ut_volum(2, 3, 4)
print(f"Volum (2, 3, 4): {volum1}")

# Eksempel 2:
volum2 = regn_ut_volum(5, 5, 5)
print(f"Volum (5, 5, 5): {volum2}")

# Eksempel 3: Du kan også kalle funksjonen direkte inne i print()
print(f"Volum (10, 2.5, 4): {regn_ut_volum(10, 2.5, 4)}")