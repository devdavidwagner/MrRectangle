import pygame
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Floor(pygame.sprite.Sprite):
    def __init__(self, x , y, screen):
        super().__init__()
        
        self.image =  pygame.image.load('Game\Objects\Backgrounds\Sprites\Floor.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        self.screen= screen
        


 
    def updatePosition(self, dx):          
        self.rect.x -= dx / 1.5
      
    def updatePositionExact(self, position):          
        self.rect.x = position
        
    def is_collided_with(self, sprite):
        return self.rect.colliderect(sprite.rect)