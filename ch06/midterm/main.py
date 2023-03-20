import turtle
import pygame
pygame.init()

def create_face(size):
    """
    This function creates a yellow circle -> face
    args: (int) radius of the face
    return: None
    """
    window = turtle.Screen()
    turtle_face = turtle.Turtle()
    turtle_face.dot(size, "yellow")
    turtle_face.penup()
    turtle_face.goto(0,-200)
    turtle_face.pendown()
    turtle_face.circle(size/2)
    turtle_face.ht()
    return 2*size/5 #use of return in smile function
    
def add_smile(size): 
    """
    This function creates a smile on the smiley face
    args: (int) size of face determines smile size
    return: None
    """
    window = turtle.Screen()
    turtle_smile = turtle.Turtle()
    turtle_smile.penup()
    turtle_smile.goto(0,-30)
    turtle_smile.pendown()
    turtle_smile.dot(create_face(size), "black")
    turtle_smile.penup()
    turtle_smile.goto(0,20)
    turtle_smile.pendown()
    turtle_smile.dot(3*size/5, "yellow")
    turtle_smile.ht()

def add_eyes():
    """
    This function creates 2 eyes
    args: None
    return: None
    """
    window = turtle.Screen()
    turtle_eyes = turtle.Turtle()
    turtle_eyes.pensize(5)
    turtle_eyes.penup()
    turtle_eyes.goto(-60,40)
    turtle_eyes.pendown()
    turtle_eyes.goto(-60,0)
    turtle_eyes.penup()
    turtle_eyes.goto(60,40)
    turtle_eyes.pendown()
    turtle_eyes.goto(60,0)
    turtle_eyes.ht()
    turtle_eyes.penup()
    turtle_eyes.goto(100,35)
    return turtle_eyes.pos()
    

def create_sunglasses(size):
    """
    This function creates sunglasses to go on a face
    args: (int) radius of sunglasses lens
    return: none
    """
    #lenses
    window = turtle.Screen()
    turtle_sun = turtle.Turtle()
    turtle_sun.penup()
    turtle_sun.goto(add_eyes())
    turtle_sun.pos()
    turtle_sun.pendown()
    turtle_sun.dot(size*1.85, "black")
    turtle_sun.penup()
    turtle_sun.goto(-turtle_sun.xcor(),turtle_sun.ycor())
    turtle_sun.pos()
    turtle_sun.pendown()
    turtle_sun.dot(size*1.75, "black")
    #bridge
    turtle_sun.pensize(5)
    turtle_sun.goto(-20,turtle_sun.ycor())
    turtle_sun.goto(20,turtle_sun.ycor())
    turtle_sun.ht()

def no_sunglasses():
    """
    Displays a disappointed message for the user that said no to sunglasses
    args: None
    return: None
    """
    screen = pygame.display.set_mode()
    width, height = screen.get_size()
    screen.fill("white")
    font = pygame.font.Font(None, 30)
    sunglassless = font.render("I can't believe you didn't want sunglasses :( ", True, "red")
    screen.blit(sunglassless, (width/2, height/2))
    pygame.display.flip()

def main():
    size = 400
    add_smile(size) #create_face is called in add_smile 
    add_eyes()
    
    not_answered = True
    while not_answered == True:
        add_sunglasses = input("Want to add sunglasses? Type yes or no exactly. ")
        
        if add_sunglasses == "yes":
            create_sunglasses(100)
            not_answered = False
        elif add_sunglasses == "no":
            no_sunglasses()
            not_answered = False
        else:
            not_answered = True
    
    turtle.exitonclick()
main()
