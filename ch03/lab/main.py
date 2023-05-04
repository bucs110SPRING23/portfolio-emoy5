import pygame
import random
import math
pygame.init()

screen = pygame.display.set_mode(size=(1000,1000))
screen.fill("black")
screen_width, screen_height = pygame.display.get_window_size()

# Part A
pygame.draw.circle(screen, "orange", (screen_width/2, screen_height/2), screen_width/2)
pygame.draw.line(screen, "black", (0,screen_height/2), (screen_width,screen_height/2))
pygame.draw.line(screen, "black", (screen_width/2,0), (screen_width/2,screen_height))

# Part B
for _ in range(10):
    rand_x = random.randrange(0,screen_width)
    rand_y = random.randrange(0,screen_height)
    distance_from_center = math.hypot(rand_x-screen_width/2, rand_y-screen_height/2) #the distance formula
    is_in_circle = distance_from_center <= screen_width/2 #screen width

    if is_in_circle:
        color = "white"
    else:
        color = "red"

    pygame.draw.circle(screen, color, (rand_x, rand_y), 10)
    pygame.display.flip()
    pygame.time.wait(1000)