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
done = False

hit_box_width = screen_width / 10
hit_box_height = screen_height / 10
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
    
pygame.draw.rect(screen, highlight_colors["red"], hitboxes["red"])
pygame.draw.rect(screen, highlight_colors["blue"], hitboxes["blue"])
pygame.display.flip()
pygame.time.delay(1000)

done = False # a flag variable to determine when the program is done
player_bet = [] # a list for the user's guess


#main loop?
while not done:
    for event in pygame.event.get():
        #rectangles and hitboxes
        

        
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if hitboxes["red"].collidepoint(event.pos):
                player_bet.append("red")
            elif hitboxes["blue"].collidepoint(event.pos):
                player_bet.append("blue")
            else:
                done = True
            
            #Darts 
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

            #Displaying results after darts done
            font = pygame.font.Font(None, 48)
            
            if len(player1) > len(player2):
                text = font.render("Red wins", True, "white")
                if player_bet[0] == "red":
                    bet = font.render("You win the bet!", True, "white")
                else:
                    bet = font.render("You lose the bet :(", True, "white")
            elif len(player1) < len(player2):
                text = font.render("Blue wins", True, "white")
                if player_bet[0] == "blue":
                    bet = font.render("You win the bet!", True, "white")
                else:
                    bet = font.render("You lose the bet :(", True, "white")
            elif len(player1) == len(player2):
                text = font.render("Tie", True, "white")
                bet = font.render("You lose the bet :(", True, "white")
            
            screen.blit(text, (screen_width/2, screen_height/2)) # where <x> and<y> are coordinates on screen
            screen.blit(bet, (screen_width/2, screen_height/2+50))
            pygame.display.flip()
            pygame.time.wait(1000)

            done = True


