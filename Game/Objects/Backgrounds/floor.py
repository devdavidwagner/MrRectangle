import pygame

class Floor(pygame.sprite.Sprite):
    def __init__(self, x , y):
        super().__init__()
        
        self.image =  pygame.image.load('Game\Objects\Backgrounds\Floor.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x