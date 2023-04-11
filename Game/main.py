import pygame
from Screens.Level import Level
from Screens.MainMenu import MainMenu
from StateManager import StateManager

global SCREEN_WIDTH 
global SCREEN_HEIGHT 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
pygame.init()
pygame.display.set_caption("Mr. Rectangle")
clock = pygame.time.Clock() 
runningMain = True

stateManager = StateManager()
level1 = Level()
menu = MainMenu()

while runningMain:

  

    #menu
    if stateManager.currentState == stateManager.states[0]:
        # Get keyboard input
        keys = pygame.key.get_pressed()
        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60
        menu.run(keys, stateManager)
    #game
    if stateManager.currentState == stateManager.states[1]:
        level1.run()
    




    

pygame.quit()