import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BACKGROUND_SPEEDS = 20
class Parallax(pygame.sprite.Sprite):
    def __init__(self, x , y, screen):
        super().__init__()
        
        self.cloud =  pygame.image.load('Game\Objects\Backgrounds\Sprites\Clouds.png').convert_alpha()
        self.path =  pygame.image.load('Game\Objects\Backgrounds\Sprites\Path.png').convert_alpha()
        self.tree =  pygame.image.load('Game\Objects\Backgrounds\Sprites\Tree_BG.png').convert_alpha()


        self.bg1_x = 0
        self.bg2_x = 0
        self.bg3_x = 0
        self.screen = screen
        


    def update(self, dx):      
        if dx != 0:
            self.bg1_x += 2 * 0.04
            self.bg2_x += dx * 0.23
            self.bg3_x += dx * 0.2
        else:
            self.bg1_x += 2 * 0.04
            self.bg2_x += dx * 0.23
            self.bg3_x += dx * 0.2

        self.screen.blit(self.cloud, (self.bg1_x , 0))
        self.screen.blit(self.cloud, (self.bg1_x - SCREEN_WIDTH, 0))
        self.screen.blit(self.cloud, (self.bg1_x + SCREEN_WIDTH, 0))

        self.screen.blit(self.path, (self.bg2_x , 0))
        self.screen.blit(self.path, (self.bg2_x - SCREEN_WIDTH, 0))
        self.screen.blit(self.path, (self.bg2_x + SCREEN_WIDTH, 0))

        self.screen.blit(self.tree, (self.bg3_x , 0))
        self.screen.blit(self.tree, (self.bg3_x - SCREEN_WIDTH, 0))
        self.screen.blit(self.tree, (self.bg3_x + SCREEN_WIDTH, 0))

        if self.bg1_x > SCREEN_WIDTH:
            self.bg1_x = 0
 

        if self.bg2_x > SCREEN_WIDTH:
            self.bg2_x = 0 

            
        if self.bg3_x > SCREEN_WIDTH:
            self.bg3_x = 0 

        if self.bg1_x < 0 -SCREEN_WIDTH:
            self.bg1_x = 0
 

        if self.bg2_x < 0 -SCREEN_WIDTH:
            self.bg2_x = 0 

            
        if self.bg3_x < 0 -SCREEN_WIDTH:
            self.bg3_x = -0 


        



    # def draw(self):
    #     self.screen.blit(self.image, (self.bg1_x , 0))
    #     self.screen.blit(self.image, (self.bg1_x - SCREEN_WIDTH, 0))

    #     self.screen.blit(self.path, (self.bg2_x , 0))
    #     self.screen.blit(self.path, (self.bg2_x - SCREEN_WIDTH, 0))



    


        