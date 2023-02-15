import pygame
pygame.init()
screen = pygame.display.set_mode()
screen.fill("white")

""" pygame.draw.circle(screen, "black", [500,750], 252)
pygame.display.flip()
pygame.draw.circle(screen, "white", [500,750], 250)
pygame.display.flip()

pygame.draw.circle(screen, "black", [500,450], 152)
pygame.display.flip()
pygame.draw.circle(screen, "white", [500,450], 150)
pygame.display.flip()

pygame.draw.circle(screen, "black", [500,250], 102)
pygame.display.flip()
pygame.draw.circle(screen, "white", [500,250], 100)
pygame.display.flip() """


##extra notes
dimensions = screen.get_size() 
#[width, height]
#when I want to use the dimension in the draw circle thing, write it as dimension[0] <- the index for width
#color: "red" or [r,g,b] => [0-225, 0-225, 0-225]

starting_point = [dimensions[0]//2, dimensions[1]-300]
radius = 250
#using loops
for _ in range(3):
    pygame.draw.circle(screen, "black", starting_point, radius+3)
    pygame.draw.circle(screen, "white", starting_point, radius)
    starting_point[1] = starting_point[1] - radius
    radius = radius//2
    starting_point[1] = starting_point[1] - radius

pygame.display.flip()
pygame.time.wait(2000)