from movies import movies

def avarage():
    total = 0
    for i in movies:
        total = total + i["imdb"]
    avarage = total / len(movies)

    print(round(avarage, 1))

avarage()
