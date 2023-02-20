#Simon Says
import pygame
import random
pygame.init()
screen = pygame.display.set_mode()
colors = ["red", "green", "blue", "yellow"]
random.shuffle(colors)

for color in colors:
    screen.fill(color)
    pygame.display.flip()
    pygame.time.wait(1000)

    screen.fill("black")
    pygame.display.flip()
    pygame.time.wait(250)

message = """"
    Simon says:
    UP: RED
    DOWN: BLUE
    LEFT: GREEN
    RIGHT: YELLOW
    
    click on the window, enter sequence, then press enter"""
#always respond to events in one place in the program
response = input(message)

#events in python
user_sequence = []

for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            screen.fill("red")
            user_sequence.append("red")
        if event.key == pygame.K_DOWN:
            screen.fill("blue")
            user_sequence.append("blue")
        if event.key == pygame.K_LEFT:
            screen.fill("green")
            user_sequence.append("green")
        if event.key == pygame.K_RIGHT:
            screen.fill("yellow")
            user_sequence.append("yellow")
print("user sequence: ", user_sequence)
print("colors", colors)

if user_sequence == colors:
    print("You win!")
else:
    print("Were you paying attention?")