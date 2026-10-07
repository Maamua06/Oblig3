list_film = [{"name":"Inception","year":2010,"rating":8.7},
             {"name":"Inside Out","year":2015,"rating":8.1},
             {"name":"Con Air","year":1997,"rating":6.9}]

def add_film(list_name,name, year ,rating=5.0):
    list_name.append({"name":name, "year":year, "rating":rating})


add_film(list_film,"The Godfather", 1972, 9.2)
add_film(list_film, "The Shawshank Redemption", 1994, 9.3)
add_film(list_film, "Interstellar", 2014, 8.7)
add_film(list_film, "The dictator", 2012)

print(list_film)