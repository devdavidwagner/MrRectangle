import pygame
from Screens.Level import Level

global SCREEN_WIDTH 
global SCREEN_HEIGHT 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()

pygame.display.set_caption("Mr. Rectangle")
clock = pygame.time.Clock() 
running = True
runningMain = True
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
gaming = False


# Set up the font

font = pygame.font.SysFont('Arial', 55)
font2 = pygame.font.SysFont('Arial', 36)
font3 = pygame.font.SysFont('Arial', 14)

text_surface = font.render("MR.RECTANGLE!", True, (255, 255, 255))
text_rect = text_surface.get_rect()
text_rect.center = (SCREEN_WIDTH/ 2, 100)


text_surface2 = font2.render("Press Enter To Play", True, (255, 255, 255))
text_rect2 = text_surface2.get_rect()
text_rect2.center = (SCREEN_WIDTH / 2, 540)

text_surface3 = font3.render("A new game by David Wagner ©2023", True, (255, 255, 255))
text_rect3 = text_surface3.get_rect()
text_rect3.center = (SCREEN_WIDTH/ 2, 180)

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
color_index = 0

text_surfaces = [text_surface2, text_surface2, text_surface2]
text_rects = [text_rect2, text_rect2, text_rect2]

for i in range(3):
    text_surfaceC = font.render("Press Enter To Play", True, colors[i])
    text_rectC = text_surfaceC.get_rect()
    text_rectC.center = (SCREEN_WIDTH / 2, 540)
    text_surfaces[i] = text_surfaceC
    text_rects[i] = text_rectC


#images

newRect = pygame.Rect(SCREEN_WIDTH/ 2, 300, 100, 200)
newRect.center = (SCREEN_WIDTH/ 2, 300)
mrRect =  pygame.transform.scale(pygame.image.load('Game\Objects\Sprites\RectangleStillLeft.png').convert_alpha(), newRect.size)


# Set the end event to restart the audio file when it ends
pygame.mixer.music.set_endevent(pygame.USEREVENT)
pygame.mixer.music.load("Game\Audio\Themes\MrRectangleMainTheme.mp3")
#pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.2)

while runningMain:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            runningMain = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                runningMain = False
            if event.key == pygame.K_RETURN:
                gaming = True
                runningMain = False
        if event.type == pygame.USEREVENT:
           # pygame.mixer.music.play()
            print("event triggered")

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    screen.blit(text_surface, text_rect)
    screen.blit(text_surfaces[color_index], text_rects[color_index])
    screen.blit(text_surface3, text_rect3)
    screen.blit(mrRect, newRect)
    # Get keyboard input
    keys = pygame.key.get_pressed()
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
    

    pygame.time.wait(250)
    # Increment the color index and wrap around if necessary
    color_index = (color_index + 1) % 3

if gaming and running:
    level1 = Level()
    level1.run(screen, clock)
    

pygame.quit()