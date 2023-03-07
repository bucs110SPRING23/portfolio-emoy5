import pygame
import random
import math
pygame.init()

screen = pygame.display.set_mode(size=(1000,1000))
screen.fill("black")
screen_width, screen_height = pygame.display.get_window_size()

pygame.draw.circle(screen, "orange", (screen_width/2, screen_height/2), screen_width/2)
pygame.draw.line(screen, "black", (0,screen_height/2), (screen_width,screen_height/2))
pygame.draw.line(screen, "black", (screen_width/2,0), (screen_width/2,screen_height))

player1 = []
player2 = []

pygame.display.flip()
pygame.time.wait(500)

#main loop?
while not done:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:

            #rectangles and hitboxes
            hit_box_width = screen_width / 2
            hit_box_height = screen_height / 2

            hitboxes = {
                "red": pygame.Rect(0, 0, hit_box_width, hit_box_height),
                "blue": pygame.Rect(0, 0, hit_box_width, hit_box_height),
            }

            hitboxes["blue"].topleft = hitboxes["red"].topright

            # Define main colors
            main_colors = {
            "red": (100, 0, 0),
            "blue": (0, 0, 100),
            }

            # Define highlight colors
            highlight_colors = {
            "red": (255, 0, 0),
            "blue": (0, 0, 255),
            }

            font = pygame.font.Font(None, 48)

            for _ in range(10):
                #wasn't sure how to alternate red and blue...
                #for player 1
                rand_x = random.randrange(0,screen_width)
                rand_y = random.randrange(0,screen_height)
                distance_from_center = math.hypot(rand_x-screen_width/2, rand_y-screen_height/2) #the distance formula
                is_in_circle = distance_from_center <= screen_width/2 #screen width
                
                if is_in_circle:
                    color = "red"
                    player1.append(1)
                else:
                    color = "pink"
                pygame.draw.circle(screen, color, (rand_x, rand_y), 10)
                pygame.display.flip()
                pygame.time.wait(500)

                #for player 2
                rand_x2 = random.randrange(0,screen_width)
                rand_y2 = random.randrange(0,screen_height)
                distance_from_center2 = math.hypot(rand_x2-screen_width/2, rand_y2-screen_height/2) #the distance formula
                is_in_circle2 = distance_from_center2 <= screen_width/2 #screen width
                
                if is_in_circle2:
                    color = "blue"
                    player2.append(1)
                else:
                    color = "light blue"
                
                pygame.draw.circle(screen, color, (rand_x2, rand_y2), 10)
                pygame.display.flip()
                pygame.time.wait(1000)

            font = pygame.font.Font(None, 48)
            if len(player1) > len(player2):
                text = font.render("Red wins", True, "white")
            elif len(player1) < len(player2):
                text = font.render("Blue wins", True, "white")
            elif len(player1) == len(player2):
                text = font.render("Tie", True, "white")
            screen.blit(text, (screen_width/2, screen_height/2)) # where <x> and<y> are coordinates on screen
            pygame.display.flip()
            pygame.time.wait(1000)
    else:
