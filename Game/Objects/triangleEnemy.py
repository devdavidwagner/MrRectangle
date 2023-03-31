import pygame


# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TRIANGLE_WIDTH = 50
TRIANGLE_HEIGHT = 50
TRIANGLE_SPEED = 10

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Triangle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('Game\Objects\Sprites\Triangle.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def updatePosition(self, dx, dy):
        # Move the sprite
        self.rect.x += dx
        self.rect.y += dy

        # Check if the sprite is going off the screen
        if self.rect.left < 0 + 30:
            self.rect.left = 0  + 30
        elif self.rect.right > SCREEN_WIDTH - 30:
            self.rect.right = SCREEN_WIDTH - 30
        if self.rect.top < 0 + 20:
            self.rect.top = 0 + 20
        elif self.rect.bottom > SCREEN_HEIGHT - 20:
            self.rect.bottom = SCREEN_HEIGHT - 20

 

