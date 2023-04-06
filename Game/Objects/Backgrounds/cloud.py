import pygame

SCREEN_WIDTH = 800

BACKGROUND_SPEEDS = 20
class Cloud(pygame.sprite.Sprite):
    def __init__(self, x , y, screen):
        super().__init__()
        
        self.image =  pygame.image.load('Game\Objects\Backgrounds\Sprites\Clouds.png').convert_alpha()
        #self.image2 =  pygame.image.load('Game\Objects\Backgrounds\Clouds.png').convert_alpha()
        #self.image3 =  pygame.image.load('Game\Objects\Backgrounds\Clouds.png').convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        # self.rect2 = self.image2.get_rect()
        # self.rect2.y = y
        # self.rect2.x = x

        self.screen = screen

        

    def update(self, keys):          
        # Update the background positions
        bg1_x = -pygame.time.get_ticks() / 1000 * BACKGROUND_SPEEDS % SCREEN_WIDTH
        # bg2_x = -pygame.time.get_ticks() / 1000 * BACKGROUND_SPEEDS[1] % SCREEN_WIDTH
        # bg3_x = -pygame.time.get_ticks() / 1000 * BACKGROUND_SPEEDS[2] % SCREEN_WIDTH
        
        # Draw the background
        self.screen.blit(self.image, (bg1_x , 0))
        self.screen.blit(self.image, (bg1_x - SCREEN_WIDTH, 0))
        # self.screen.blit(self.image2, (bg2_x, 0))
        # self.screen.blit(self.image2, (bg2_x - SCREEN_WIDTH, 0))
        # self.screen.blit(self.image3, (bg3_x, 0))
        # self.screen.blit(self.image3, (bg3_x - SCREEN_WIDTH, 0))
        


        