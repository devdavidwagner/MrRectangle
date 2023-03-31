# Example file showing a basic pygame "game loop"
import pygame
from Objects.rectangle import Rectangle
from Objects.triangleEnemy import Triangle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# pygame setup
pygame.init()

pygame.display.set_caption("Mr. Rectangle")
clock = pygame.time.Clock()
running = True


# Load the background image
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background_image  = pygame.transform.scale(pygame.image.load("Game/Objects/Sprites/Background.png").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
background_image.convert_alpha()



# Create sprites
all_sprites = pygame.sprite.Group()
rectangle = Rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
all_sprites.add(rectangle)
triangle = Triangle(SCREEN_WIDTH/4, SCREEN_HEIGHT/4)
all_sprites.add(triangle)

tdx = 5 
tdy = 5
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
    screen.blit(background_image, (0, 0))


    # Get keyboard input
    keys = pygame.key.get_pressed()

    # Move the Rectangle sprite based on the arrow keys
    dx = 0
    dy = 0
    if keys[pygame.K_a]:
        dx = -5
    elif keys[pygame.K_d]:
        dx = 5
    if keys[pygame.K_w]:
        dy = -5
    elif keys[pygame.K_s]:
        dy = 5
    rectangle.updatePosition(dx, dy)

    #ENEMIES AI
    tdx += 0.05
    tdy += 0.05
    triangle.updatePosition(tdx, tdy)

    # RENDER YOUR GAME HERE
      # Update game state
    all_sprites.update(keys)

    # Draw game objects
    #screen.fill("WHITE")
    all_sprites.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
    

pygame.quit()

