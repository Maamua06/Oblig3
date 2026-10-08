# Eksisterende filmliste
filmer = [
    {"name": "Inception", "year": 2010, "rating": 8.7},
    {"name": "Inside Out", "year": 2015, "rating": 8.1},
    {"name": "Con Air", "year": 1997, "rating": 6.9}
]

# ==========================================
# A) Funksjon for å skrive filmer til fil
# ==========================================
def skriv_filmer_til_fil(filmliste, filnavn):
    # Modus "w" overskriver filen hvis den finnes fra før
    with open(filnavn, "w", encoding="utf-8") as file:
        for film in filmliste:
            linje = f"{film['name']} - {film['year']} has a rating of {film['rating']}\n"
            file.write(linje)

# ==========================================
# B) Funksjon for å lese fra fil og skrive ut
# ==========================================
def les_og_skriv_ut_fil(filnavn):
    with open(filnavn, "r", encoding="utf-8") as file:
        for linje in file:
            print(linje.strip())  # .strip() fjerner ekstra linjeskift (\n)


# ==========================================
# Testing av funksjonene
# ==========================================

filnavn = "movies.txt"

# A) Skriver filmene til filen "movies.txt"
skriv_filmer_til_fil(filmer, filnavn)
print(f"Filmene har blitt skrevet til '{filnavn}'.\n")

# B) Leser filen og skriver ut innholdet til terminalen
print(f"Leser innholdet fra '{filnavn}':")
les_og_skriv_ut_fil(filnavn)