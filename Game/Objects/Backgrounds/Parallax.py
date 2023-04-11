import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BACKGROUND_SPEEDS = 20
class Parallax(pygame.sprite.Sprite):
    def __init__(self, x , y, screen):
        super().__init__()
        
        self.image =  pygame.image.load('Game\Objects\Backgrounds\Sprites\Clouds.png').convert_alpha()
        self.path =  pygame.image.load('Game\Objects\Backgrounds\Sprites\Path.png').convert_alpha()
        #self.image2 =  pygame.image.load('Game\Objects\Backgrounds\Clouds.png').convert_alpha()
        #self.image3 =  pygame.image.load('Game\Objects\Backgrounds\Clouds.png').convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        
        self.rectPath = self.image.get_rect()
        self.rectPath.y = y
        self.rectPath.x = x

        # self.rect2 = self.image2.get_rect()
        # self.rect2.y = y
        # self.rect2.x = x
        self.bg1_x = 0
        self.bg2_x = 0

        self.screen = screen
        


    def update(self, dx):          
        self.bg1_x += dx * 0.4
        self.bg2_x += dx * 0.1

        self.screen.blit(self.image, (self.bg1_x , 0))
        self.screen.blit(self.image, (self.bg1_x - SCREEN_WIDTH, 0))

        self.screen.blit(self.path, (self.bg2_x , 0))
        self.screen.blit(self.path, (self.bg2_x - SCREEN_WIDTH, 0))



    # def draw(self):
    #     self.screen.blit(self.image, (self.bg1_x , 0))
    #     self.screen.blit(self.image, (self.bg1_x - SCREEN_WIDTH, 0))

    #     self.screen.blit(self.path, (self.bg2_x , 0))
    #     self.screen.blit(self.path, (self.bg2_x - SCREEN_WIDTH, 0))



    


        