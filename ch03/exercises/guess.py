import random

thenumber = random.randrange(1,11)
guess = int(input("Give me a number from 1-10"))

for guessesleft in range(3):
    if guess == thenumber:
        print("Correct!")
        break #guessesleft = 1 <- what i had in the beginning. I tried to break the loop, but didn't know the notation
    elif guess >= thenumber:
        print("Too high")
        guess = int(input("Guess again: "))
    elif guess <= thenumber:
        print("Too low")
        guess = int(input("Guess again: "))

if guess != thenumber:
    print("Still wrong. The correct number was ", thenumber)

''' 
num = random.randint(1,10) or random.randrange(1,11)

guess = -1

for i in range(3):
    if guess != num: 
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == num:
            print("You guessed it! My number was", num)
            break or return
        elif guess < num:
            print("Too low!")
        elif guess > num:
            print("Too high!")

'''