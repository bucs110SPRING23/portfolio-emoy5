import turtle
import random

#function
'''def is_in_screen(w, t):
    x = turtle.xcor()
    y = turtle.ycor()
    x_range = window.window_width()/2
    y_range = window.window_height()/2

    if abs(x) > x_range or abs(y) > y_range:
        is_in_screen = False
'''

window = turtle.Screen()
turtle = turtle.Turtle()

distance = 50
angle = 90
is_in_screen = True

while is_in_screen:
    coinflip = random.randint(0,1)
    
    if coinflip == 0:
        turtle.left(angle)
    elif coinflip == 1:
        turtle.right(angle)
    turtle.forward(distance)

    x = turtle.xcor()
    y = turtle.ycor()
    x_range = window.window_width()/2
    y_range = window.window_height()/2

    if abs(x) > x_range or abs(y) > y_range:
        is_in_screen = False

window.exitonclick()
