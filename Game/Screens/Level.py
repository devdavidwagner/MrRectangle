import pygame
from Objects.Rectangle import Rectangle
from Objects.Backgrounds.Floor import Floor
from Objects.Backgrounds.Parallax import Parallax as Para
from Objects.Backgrounds.BackgroundObject import BackgroundObject as BG

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
OBJECT_TRAVEL = 500
GRAVITY = 5

DIRECTORY_MOUNTAIN = 'Game\Objects\Backgrounds\Sprites\Mountain.png'
DIRECTORY_TREE = 'Game\Objects\Backgrounds\Sprites\Tree.png'
DIRECTORY_HOUSE = 'Game\Objects\Backgrounds\Sprites\House.png'

class Level():
    def __init__(self):
        super().__init__()
        
        self.keys =  pygame.key.get_pressed()
        # Load the background image
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.para = Para(0, 10, self.screen)
        self.background_image  = pygame.transform.scale(pygame.image.load("Game\Objects\Backgrounds\Sprites\BG1_Sky.png").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background_image.convert_alpha()
    
        # Create sprites 
        self.all_sprites = pygame.sprite.Group()

        self.objects = [[BG(800, 220, DIRECTORY_MOUNTAIN), 800], [BG(400, 220, DIRECTORY_MOUNTAIN), 400, 600], [BG(650, 220, DIRECTORY_MOUNTAIN), 600], [BG(550, 220, DIRECTORY_MOUNTAIN), 550]
                          , [BG(2000, 220, DIRECTORY_MOUNTAIN), 2000], [BG(500, 400, DIRECTORY_TREE), 2000] , [BG(600, 400, DIRECTORY_TREE), 2000], [BG(300, 300, DIRECTORY_HOUSE), 2000]]
        
                
        for BackgroundObject in self.objects:
                self.all_sprites.add(BackgroundObject[0])
        

        self.rectangle = Rectangle(100, SCREEN_HEIGHT - 100)
        self.all_sprites.add(self.rectangle)


        self.tdx = 0.5 
        self.tdy = 0.5
        
        self.floor = Floor(0, SCREEN_HEIGHT - 30,self.screen)
        self.floorAhead = Floor(SCREEN_WIDTH, SCREEN_HEIGHT - 30,self.screen)
        self.all_sprites.add(self.floor)
        self.all_sprites.add(self.floorAhead)
     
        self.distanceTraveled = 0
        self.distanceOfPlayer = 0

        self.running = False
      

        
            
    
    def run(self, screen, clock):
        position = "R"
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
        
            screen.blit(self.background_image, (0,0))

       
            # Move the Rectangle sprite based on the arrow keys
            dx = 0
            dy = 0 
            
            if self.keys[pygame.K_a]:
                dx = -7
                self.distanceOfPlayer -= 1
                self.rectangle.updateSprite("L")
                self.floor.updatePosition(dx)
                self.floorAhead.updatePosition(dx)
                self.para.update(dx)
                print(self.distanceOfPlayer)
                for BackgroundObject in self.objects:                     
                      if self.distanceTraveled > OBJECT_TRAVEL:
                         BackgroundObject[0].updatePosition(dx)
                         self.distanceTraveled +=1
                      else:
                         BackgroundObject[0].updatePosition(dx)
                         self.distanceTraveled -=1
                      

                position = "L"
            elif self.keys[pygame.K_d]:
                dx = 7
                self.distanceOfPlayer += 1
                self.rectangle.updateSprite("R")
                self.floor.updatePosition(dx)
                self.floorAhead.updatePosition(dx)
                self.para.update(dx)

                print(self.distanceOfPlayer)
                for BackgroundObject in self.objects:         
                    if self.distanceTraveled < OBJECT_TRAVEL:          
                        BackgroundObject[0].updatePosition(dx)
                        self.distanceTraveled +=1
                    else:
                        BackgroundObject[0].updatePosition(dx)
                        self.distanceTraveled -=1

                position = "R"
            else:
                self.rectangle.updateSprite(position,True)
                
            self.para.update(dx)

            if self.distanceOfPlayer < 300:
                if self.floor.rect.right  < 0:
                    self.floorAhead.updatePositionExact(0)
                    self.floor.updatePositionExact(SCREEN_WIDTH)   

                if self.floorAhead.rect.right < 0:
                    self.floor.updatePositionExact(0)
                    self.floorAhead.updatePositionExact(SCREEN_WIDTH)

                if self.floor.rect.left  > SCREEN_WIDTH:
                    self.floorAhead.updatePositionExact(SCREEN_WIDTH)
                    self.floor.updatePositionExact(0)


                if self.floorAhead.rect.left > SCREEN_WIDTH:
                    self.floor.updatePositionExact(SCREEN_WIDTH)
                    self.floorAhead.updatePositionExact(0)
            

        
            if self.floor.is_collided_with(self.rectangle):
                self.rectangle.rect.bottom = self.floor.rect.top
            elif self.rectangle.rect.x > self.floor.rect.right and self.rectangle.rect.x > self.floorAhead.rect.right:
                self.rectangle.rect.y += GRAVITY
                
            self.rectangle.updatePosition(dx, dy) 

            #ENEMIES AI
            #self.triangle.updatePosition(self.tdx, self.tdy)

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
            

        






