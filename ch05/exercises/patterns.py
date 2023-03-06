#Part 1
def star_pyramid(x):
    for _ in range(x+1):
        print("*" * _ )

star_pyramid(int(input("Enter a number to determine the height of your pyramid: ")))

#Part 2
def rstar_pyramid(x):
    for _ in range(x+1):
        print("*" * x)
        x -=1

rstar_pyramid(int(input("Enter a number to determine the height of your pyramid: ")))
