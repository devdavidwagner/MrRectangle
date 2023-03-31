import pygame


# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
RECTANGLE_WIDTH = 80
RECTANGLE_HEIGHT = 100
RECTANGLE_SPEED = 5

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Rectangle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('Game\Sprites\Rectangle.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= RECTANGLE_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += RECTANGLE_SPEED
        if keys[pygame.K_UP]:
            self.rect.y -= RECTANGLE_SPEED
        if keys[pygame.K_DOWN]:
            self.rect.y += RECTANGLE_SPEED

