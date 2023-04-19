import pygame

#creating sprites

class Snowman(pygame.sprite.Sprite): #inheriting the sprite class that someone else wrote
    def __init__(self, x, y, img = "assets/snowman.png") -> None:
        super().__init__()
        
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        