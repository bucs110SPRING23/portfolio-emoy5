#Part 1
def star_pyramid(x):
    for i in range(x+1):
        print("*" * i )


#Part 2
def rstar_pyramid(x):
    for i in range(x+1):
        print("*" * x)
        x -=1

'''
def rstar_pyramid(stars):
    for i in range(stars, 0, -1)
        print("*" * i )
'''

stars = int(input("Enter a number to determine the height of your pyramid: "))
star_pyramid(stars)
rstar_pyramid(stars)
