# ==========================================
# A) Opprett en liste med filmer
# ==========================================
filmer = [
    {"name": "Inception", "year": 2010, "rating": 8.7},
    {"name": "Inside Out", "year": 2015, "rating": 8.1},
    {"name": "Con Air", "year": 1997, "rating": 6.9}
]

# ==========================================
# B) Opprett funksjon for å legge til film
# C) Modifiser funksjonen med default-rating = 5.0
# ==========================================
def legg_til_film(filmliste, name, year, rating=5.0):
    ny_film = {
        "name": name,
        "year": year,
        "rating": rating
    }
    filmliste.append(ny_film)

# B) Legg til 3 valgfrie filmer (med spesifisert rating)
legg_til_film(filmer, "The Shawshank Redemption", 1994, 9.3)
legg_til_film(filmer, "The Godfather", 1972, 9.2)
legg_til_film(filmer, "Interstellar", 2014, 8.7)

# C) Test at default-rating (5.0) fungerer ved å utelate rating-argumentet
legg_til_film(filmer, "En ukjent film", 2024)

# Utskrift for å kontrollere resultatet
print("Oppdatert filmliste:")
for film in filmer:
    print(f"- {film['name']} ({film['year']}) - Rating: {film['rating']}")