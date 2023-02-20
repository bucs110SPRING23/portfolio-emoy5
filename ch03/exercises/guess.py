import random

thenumber = random.randrange(1,11)
guess = int(input("Give me a number from 1-10"))

for guessesleft in range(2):
    if guess == thenumber:
        print("Correct!")
        guessesleft = 1
    elif guess >= thenumber:
        print("Too high")
        guess = int(input("Guess again"))
    elif guess <= thenumber:
        print("Too low")
        guess = int(input("Guess again"))

if guess != thenumber:
    print("Still wrong. The correct number was ", thenumber)
else:
    print("Correct!")