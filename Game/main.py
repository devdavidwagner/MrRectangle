# Example file showing a basic pygame "game loop"
import pygame
from Sprites.Rectangle import Rectangle

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mr. Rectangle")
clock = pygame.time.Clock()
running = True



# Create sprites
all_sprites = pygame.sprite.Group()
rectangle = Rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
all_sprites.add(rectangle)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")


    # Get keyboard input
    keys = pygame.key.get_pressed()

    # RENDER YOUR GAME HERE
      # Update game state
    all_sprites.update(keys)

    # Draw game objects
    screen.fill("WHITE")
    all_sprites.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
    

pygame.quit()

