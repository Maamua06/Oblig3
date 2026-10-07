# Eksempel på en dictionary med eksisterende studentdata
student = {
    "fornavn": "Ola",
    "etternavn": "Nordmann",
    "favorittkurs": "Programmering 1"
}

# 1. Skriv ut studentens fullstendige navn
print(f"Fullstendig navn: {student['fornavn']} {student['etternavn']}")

# 2. Programmatisk endre studentens favorittkurs til å inkludere emnekoden
student["favorittkurs"] = "ITF10219 Programmering 1"

# 3. Programmatisk legg til en alder for studenten i dictionarien
student["alder"] = 21

# Sjekk at dictionarien er oppdatert
print("Oppdatert student-dictionary:", student)