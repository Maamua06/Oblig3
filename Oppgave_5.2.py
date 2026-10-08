list_film = [{"name":"Inception","year":2010,"rating":8.7},
             {"name":"Inside Out","year":2015,"rating":8.1},
             {"name":"Con Air","year":1997,"rating":6.9}]

def format_film(list_name):
    for item in list_name:
        print(f"{item["name"]} - {item["year"]} has a rating of {item["rating"]}", "\n")

format_film(list_film)

def average_rating(list_of_films):
    rating_sum = 0
    for film in list_of_films:
        rating_sum += film["rating"]

    average = round(rating_sum / len(list_of_films), 1)

    print(average, "\n")

average_rating(list_film)

def film_year(list_of_films, year):
    new_list_of_films = []

    for film in list_of_films:
        if film["year"] >= year:
            new_list_of_films.append(film)

    print(new_list_of_films)

film_year(list_film, 2010)