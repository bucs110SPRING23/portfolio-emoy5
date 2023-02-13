import pygame
pygame.init()
screen = pygame.display.set_mode()
screen.fill("white")

pygame.draw.circle(screen, "black", [500,750], 252)
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
pygame.display.flip()

pygame.time.wait(2000)