import random


def skriv_ut_tilfeldig_tall():
    # random.randrange(start, stop) stopper FØR stop-verdien.
    # Dette gir tall fra og med 1 til og med 99:
    tall = random.randrange(1, 100)

    print("*********")
    print(f"***{tall}***")
    print("*********")


# Kaller funksjonen tre ganger
skriv_ut_tilfeldig_tall()
skriv_ut_tilfeldig_tall()
skriv_ut_tilfeldig_tall()

# Alternativt kan du bruke en for-løkke hvis du vil kalle den mange ganger:
# for _ in range(3):
#     skriv_ut_tilfeldig_tall()