import turtle #1. import modules
import random
#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
x1 = random.randrange(1,101)
x2 = random.randrange(1,101)
#Race 1
michelangelo.forward(x1)
leonardo.forward(x2)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

#Race 2

for i in range(11):
    mikex = random.randrange(1, 101)
    leox = random.randrange(1, 101)
    michelangelo.forward(mikex)
    leonardo.forward(leox)

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
window.exitonclick()

# PART B - complete part B here
import pygame
import math
pygame.init()
screen = pygame.display.set_mode()
dimensions = screen.get_size()
screen.fill("black") 

points = []
num_sides = [3, 4, 6, 20, 100, 360]
#not really sure what it meant for the num_sides to be an int
xpos = dimensions[0]/2
ypos = dimensions[1]/2
side_length = 100

for c in range(0,7):
    for i in range(num_sides[c]):
        angle = 360/num_sides[c]
        radians = math.radians(angle * i)
        x = xpos + side_length * math.cos(radians)
        y = ypos + side_length * math.sin(radians)
        points.append((x, y))
    screen.fill("black")
    pygame.draw.polygon(screen, "gray", points)
    pygame.display.flip()
    pygame.time.wait(2000)
    points = []