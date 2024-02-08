import random

from movies import movies

def muv():
    x = random.choice(movies)

    if x["imdb"] >= 5.5:
        return True
    else:
        return False
    
print(muv())
