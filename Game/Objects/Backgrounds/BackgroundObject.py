import pygame
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class BackgroundObject(pygame.sprite.Sprite):
    def __init__(self, x , y, directory):
        super().__init__()  

        self.image =  pygame.image.load(directory).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    
 
    def updatePosition(self, dx):          
        self.rect.x -= dx 
      
    def updatePositionExact(self, position):          
        self.rect.x = position
        
        