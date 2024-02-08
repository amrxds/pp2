def count(numhead, numlegs):
    rabbits = (numlegs- (numhead*2))/2
    chickens = numhead - rabbits
    print("Rabbits: " + format(rabbits))
    print("Chickens: " + format(chickens))
x = 35
y = 94
count(35, 94)
