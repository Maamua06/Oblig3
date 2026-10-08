# Eksisterende filmliste fra forrige oppgave
filmer = [
    {"name": "Inception", "year": 2010, "rating": 8.7},
    {"name": "Inside Out", "year": 2015, "rating": 8.1},
    {"name": "Con Air", "year": 1997, "rating": 6.9}
]


# ==========================================
# A) Funksjon for å printe ut alle filmer
# ==========================================
def print_filmer(filmliste):
    for film in filmliste:
        print(f"{film['name']} - {film['year']} has a rating of {film['rating']}")


# ==========================================
# B) Funksjon for å regne ut gjennomsnittsrating
# ==========================================
def regn_ut_gjennomsnitt_rating(filmliste):
    if not filmliste:  # Sjekker om listen er tom for å unngå deling på 0
        return 0.0

    total_rating = sum(film["rating"] for film in filmliste)
    gjennomsnitt = total_rating / len(filmliste)
    return round(gjennomsnitt, 1)


# ==========================================
# C) Funksjon for å filtrere filmer fra og med et årstall
# ==========================================
def hent_filmer_fra_aar(filmliste, fra_aar):
    filtrert_liste = []
    for film in filmliste:
        if film["year"] >= fra_aar:
            filtrert_liste.append(film)
    return filtrert_liste


# ==========================================
# Testing av funksjonene
# ==========================================

print("--- Oppgave A: Alle filmer ---")
print_filmer(filmer)

print("\n--- Oppgave B: Gjennomsnittsrating ---")
snitt = regn_ut_gjennomsnitt_rating(filmer)
print(f"Gjennomsnittsrating for alle filmer: {snitt}")

print("\n--- Oppgave C: Filmer fra og med 2010 ---")
nyere_filmer = hent_filmer_fra_aar(filmer, 2010)
print_filmer(nyere_filmer)