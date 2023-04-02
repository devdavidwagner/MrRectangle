import pygame


# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
RECTANGLE_WIDTH = 60
RECTANGLE_HEIGHT = 80
RECTANGLE_SPEED = 5

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Rectangle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
       
        newRect = pygame.Rect(0, 0, 60, 80)
        stretched_image  = pygame.transform.scale(pygame.image.load('Game\Objects\Sprites\Rectangle.png').convert_alpha(), newRect.size)
        self.image =  stretched_image
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
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


        #print("x" + str(self.rect.x))
        #print("y" + str(self.rect.y))

