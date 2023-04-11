import pygame
from StateManager import StateManager

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
OBJECT_TRAVEL = 500
GRAVITY = 5

DIRECTORY_MOUNTAIN = 'Game\Objects\Backgrounds\Sprites\Mountain.png'
DIRECTORY_TREE = 'Game\Objects\Backgrounds\Sprites\Tree.png'
DIRECTORY_HOUSE = 'Game\Objects\Backgrounds\Sprites\House.png'




class MainMenu():
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.font = pygame.font.SysFont('Arial', 55)
        self.font2 = pygame.font.SysFont('Arial', 36)
        self.font3 = pygame.font.SysFont('Arial', 14)

        self.text_surface = self.font.render("MR.RECTANGLE!", True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (SCREEN_WIDTH/ 2, 100)


        self.text_surface2 = self.font2.render("Press Enter To Play", True, (255, 255, 255))
        self.text_rect2 = self.text_surface2.get_rect()
        self.text_rect2.center = (SCREEN_WIDTH / 2, 540)

        self.text_surface3 = self.font3.render("A new game by David Wagner ©2023", True, (255, 255, 255))
        self.text_rect3 = self.text_surface3.get_rect()
        self.text_rect3.center = (SCREEN_WIDTH/ 2, 180)

        self.colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
        self.color_index = 0

        self.text_surfaces = [self.text_surface2, self.text_surface2, self.text_surface2]
        self.text_rects = [self.text_rect2, self.text_rect2, self.text_rect2]

        for i in range(3):
            self.text_surfaceC = self.font.render("Press Enter To Play", True, self.colors[i])
            self.text_rectC = self.text_surfaceC.get_rect()
            self.text_rectC.center = (SCREEN_WIDTH / 2, 540)
            self.text_surfaces[i] = self.text_surfaceC
            self.text_rects[i] = self.text_rectC


        #images

        self.newRect = pygame.Rect(SCREEN_WIDTH/ 2, 300, 100, 200)
        self.newRect.center = (SCREEN_WIDTH/ 2, 300)
        self.mrRect =  pygame.transform.scale(pygame.image.load('Game\Objects\Sprites\RectangleStillLeft.png').convert_alpha(), self.newRect.size)

    def run(self, stateManager):
        # fill the screen with a color to wipe away anything from last frame
        self.stateManager = StateManager()
        self.stateManager = stateManager
            #main events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    stateManager.updateState()
                    


        self.screen.fill("black")
        self.screen.blit(self.text_surface, self.text_rect)
        self.screen.blit(self.text_surfaces[self.color_index], self.text_rects[self.color_index])
        self.screen.blit(self.text_surface3, self.text_rect3)
        self.screen.blit(self.mrRect, self.newRect)

        self.color_index = (self.color_index + 1) % 3