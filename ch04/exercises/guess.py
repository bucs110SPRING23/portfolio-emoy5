import random
num = random.randrange(1,1001)

guess = -1
tries = []

while guess != num:
    if guess != num: 
        guess = int(input("Guess a number between 1 and 1000: "))
        if guess == num:
            tries.append(1)
            print("You guessed it! My number was", num, ". It took you", len(tries), "tries.")
            break 
        elif guess < num:
            tries.append(1)
            print("Too low!")
        elif guess > num:
            tries.append(1)
            print("Too high!")

if guess != num:
    print("Still wrong. The correct number was", num, ". You took", len(tries), "tries.")

'''
for loops - set number of iterations or iterating over a collection

while loops - if the condition is true, continue, if false, stop or skip
   - must declare a variable beforehand (called the iterating variable)
   - while loops maintain the state of the iterating variable -> this is the one that requires the i+=1
   - getting out of an infinite loop -> control C

for loops can be recreated w while loops, but not all while loops can be recreated into for loops like ^^

EX
sum = 0
while sum != 'q': or just go while TRUE:
    value = input("number: ")
    if value.isdigit():
        #checks to see if the entered thing is an integer
        sum += value
    elif value == 'q':
        print("Done")
        sum = value
'''
