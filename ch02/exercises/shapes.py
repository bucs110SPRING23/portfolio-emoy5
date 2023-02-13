import pygame
pygame.init()
screen = pygame.display.set_mode()
screen.fill("white")

pygame.draw.circle(screen, "black", [500,750], 252)
pygame.display.flip()
pygame.draw.circle(screen, "white", [500,750], 250)
pygame.display.flip()

pygame.draw.circle(screen, "black", [500,500], 152)
pygame.display.flip()
pygame.draw.circle(screen, "white", [500,500], 150)
pygame.display.flip()

pygame.draw.circle(screen, "black", [500,350], 102)
pygame.display.flip()
pygame.draw.circle(screen, "white", [500,350], 100)
pygame.display.flip()

pygame.time.wait(2000)