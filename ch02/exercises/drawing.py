import turtle
window = turtle.Screen()

sides = int(input("Enter a number for the number of sides of a shape"))
length = int(input("Enter a number to create the length of the sides of the shape"))

angle = (360/sides)

pen = turtle.Turtle()
pen.color("orange")

for i in range(sides):
    pen.forward(length)
    pen.right(angle)
	
window.exitonclick()