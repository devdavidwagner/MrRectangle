import pygame
from Objects.rectangle import Rectangle
from Objects.triangleEnemy import Triangle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Game():
    def __init__(self):
        super().__init__()

        self.keys =  pygame.key.get_pressed()
        # Load the background image
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background_image  = pygame.transform.scale(pygame.image.load("Game/Objects/Sprites/Background.png").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background_image.convert_alpha()

        

        # Create sprites
        self.all_sprites = pygame.sprite.Group()
        self.rectangle = Rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT - 30)
        self.all_sprites.add(self.rectangle)
        self.triangle = Triangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.all_sprites.add(self.triangle)

        self.tdx = 0.5 
        self.tdy = 0.5
        
            
        
 
    def run(self, screen, clock):
        position = "R"
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
        
            screen.blit(self.background_image, (0,0))
            
            # Move the Rectangle sprite based on the arrow keys
            dx = 0
            dy = 0 
            if self.keys[pygame.K_a]:
                dx = -7
                self.rectangle.updateSprite("L")
                position = "L"
            elif self.keys[pygame.K_d]:
                dx = 7
                self.rectangle.updateSprite("R")
                position = "R"
            else:
                self.rectangle.updateSprite(position,True)
        
                
            self.rectangle.updatePosition(dx, dy) 

            #ENEMIES AI
            self.triangle.updatePosition(self.tdx, self.tdy)

            # RENDER YOUR GAME HERE
            # Update game state
            self.all_sprites.update(self.keys)

            # Draw game objects
            #screen.fill("WHITE")
            self.all_sprites.draw(screen)

            self.keys = pygame.key.get_pressed()

            clock.tick(60)  # limits FPS to 60
            # flip() the display to put your work on screen
            pygame.display.flip()
            

        






