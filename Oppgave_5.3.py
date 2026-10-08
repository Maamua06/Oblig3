import json

list_film = [{"name":"Inception","year":2010,"rating":8.7},
             {"name":"Inside Out","year":2015,"rating":8.1},
             {"name":"Con Air","year":1997,"rating":6.9}]

def format_film(list_name, file_name):
    new_list = []
    for item in list_name:
        new_list.append(f"{item["name"]} - {item["year"]} has a rating of {item["rating"]}")

    with open(file_name,"w") as input_file:
        for film in new_list:
            input_file.write(film)
            input_file.write("\n")

format_film(list_film, "movies.txt")

def read_file(file_name):
    with open(file_name, "r") as output_file:
        print(output_file.read())

read_file("movies.txt")