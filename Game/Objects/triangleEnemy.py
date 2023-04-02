import pygame
import random


# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TRIANGLE_WIDTH = 50
TRIANGLE_HEIGHT = 50
TRIANGLE_SPEED = 10

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

flipPos = 0
class Triangle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('Game\Objects\Sprites\Triangle.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.flipPos = flipPos
    
    def updatePosition(self, dx, dy):
        # Move the sprite
         

        if self.flipPos == 1:
            self.rect.x += dx
            self.rect.y += dy
        elif self.flipPos == 2:
            self.rect.x -= dx
            self.rect.y -= dy
        elif self.flipPos == 3:
            self.rect.x -= dx
            self.rect.y += dy
        elif self.flipPos == 4:
            self.rect.x += dx
            self.rect.y -= dy
        else:
            self.rect.x += dx
            self.rect.y += dy

        #+x +y = Down-Right 1
        #-x +y = Down-Left 2
        #+x -y = Up-Right 3 
        #-x -y = Up-Left 4


        # Check if the sprite is going off the screen
        if self.rect.left < 0 + 30:
            self.flipPos = random.choice([1,3])
        elif self.rect.right > SCREEN_WIDTH - 30:
            self.flipPos = random.choice([2,4])
        if self.rect.top < 0 + 20:
            self.flipPos = random.choice([1,2])
        elif self.rect.bottom > SCREEN_HEIGHT - 20: 
            self.flipPos = random.choice([3,4])

        
        print(str(self.flipPos))
