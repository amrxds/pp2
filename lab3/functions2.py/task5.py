from movies import movies

def avarage():
    x = input()
    total = 0
    number = 0 
    for i in movies:
        if i["category"] == x:
            total = total + i["imdb"]
            number += 1

    avarage = total / number

    print(avarage)

avarage()
