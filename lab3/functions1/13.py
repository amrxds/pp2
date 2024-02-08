import random
def play():
    numberX = random.randint(1, 20)

    
    name = input('Hello! What is your name?\n')
    attempt  = int(input(f"Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.\n"))
    attempts = 1
    while 1:
        if attempt  == numberX:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break
        else:
            if attempt  < numberX:
                attempt  = int(input("Your guess is too low.\nTake a guess.\n"))
            else:
                attempt  = int(input("Your guess is too big.\nTake a guess.\n"))
                
        attempts+=1
    
play()