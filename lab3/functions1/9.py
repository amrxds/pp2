import math

def Volume(r):
    volume = (4/3) * math.pi * r**3
    print(volume)

radius = int(input())

Volume(radius)