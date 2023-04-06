import pygame


# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
RECTANGLE_WIDTH = 60
RECTANGLE_HEIGHT = 80
RECTANGLE_SPEED = 5
MAX_JUMP_HEIGHT = 100
GRAVITY = 5

INIT_JUMP_SPEED = 1

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
jumpState = False
attackState = False
class Rectangle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
       
        newRect = pygame.Rect(0, 0, 60, 80)
        self.imageStillLeft =  pygame.transform.scale(pygame.image.load('Game\Objects\Sprites\RectangleStillLeft.png').convert_alpha(), newRect.size)
        self.imageStillRight =  pygame.transform.scale(pygame.image.load('Game\Objects\Sprites\RectangleStillRight.png').convert_alpha(), newRect.size)

        self.image = self.imageStillRight
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.jumpState = jumpState
        self.attackState = attackState
        self.jumpSpeed = INIT_JUMP_SPEED
        self.heightJumped = 0
        self.attackTime = 0
        self.fallingState = False
        self.prevPos = ""

        #prep other sprites
        self.imageMoveRight =  pygame.transform.scale(pygame.image.load('Game\Objects\Sprites\RectangleMoveRight.png').convert_alpha(), newRect.size)
        self.imageMoveRight.convert_alpha()

        self.imageMoveLeft =  pygame.transform.scale(pygame.image.load('Game\Objects\Sprites\RectangleMoveLeft.png').convert_alpha(), newRect.size)
        self.imageMoveLeft.convert_alpha()

        self.imageJumpRight =  pygame.transform.scale(pygame.image.load('Game\Objects\Sprites\RectangleJumpingRight.png').convert_alpha(), newRect.size)
        self.imageJumpRight.convert_alpha()

        self.imageJumpLeft =  pygame.transform.scale(pygame.image.load('Game\Objects\Sprites\RectangleJumpingLeft.png').convert_alpha(), newRect.size)
        self.imageJumpLeft.convert_alpha()


        self.imageStillRightAttack =  pygame.transform.scale(pygame.image.load('Game\Objects\Sprites\RectangleStillRightAttacking1.png').convert_alpha(), newRect.size)
        self.imageStillRightAttack.convert_alpha()

        self.imageStillRightAttack2 =  pygame.transform.scale(pygame.image.load('Game\Objects\Sprites\RectangleStillRightAttacking2.png').convert_alpha(), newRect.size)
        self.imageStillRightAttack2.convert_alpha()

        self.imageStillRightAttack3 =  pygame.transform.scale(pygame.image.load('Game\Objects\Sprites\RectangleStillRightAttacking3.png').convert_alpha(), newRect.size)
        self.imageStillRightAttack3.convert_alpha()

        self.imageStillRightAttack4 =  pygame.transform.scale(pygame.image.load('Game\Objects\Sprites\RectangleStillRightAttacking4.png').convert_alpha(), newRect.size)
        self.imageStillRightAttack4.convert_alpha()



    def update(self, keys) :
        if keys[pygame.K_SPACE] :
            self.jumpState = True
        if keys[pygame.K_l] :
            self.attackState = True

        if self.attackState == True :
            self.attackState += 1

        if self.jumpState == True :
            self.jumpSpeed *= 1.2
            self.heightJumped += self.jumpSpeed
            self.rect.y -= self.jumpSpeed

        if self.fallingState == True :
            self.rect.y += GRAVITY
            self.jumpSpeed = INIT_JUMP_SPEED

        if self.jumpState == True and self.heightJumped > MAX_JUMP_HEIGHT :
            self.jumpState = False
            self.fallingState = True

        if self.fallingState == True  and self.rect.bottom > SCREEN_HEIGHT - 30 :
            self.fallingState = False
            self.heightJumped = 0

        #print("FALLING = " + str(self.fallingState))
        #print("JUMPING =" + str(self.jumpState))    
    def updateSprite(self, position = "", still = False):


        if self.attackState == True :
            if self.attackTime > 0 and self.attackTime < 10:
                self.image = self.imageStillRightAttack
            elif self.attackTime > 10 and self.attackTime < 20:
                self.image = self.imageStillRightAttack2
            elif self.attackTime > 20 and self.attackTime < 30:
                self.image = self.imageStillRightAttack3
            elif self.attackTime > 30 and self.attackTime < 40:
                self.image = self.imageStillRightAttack4
            elif self.attackTime > 40:
                self.image = self.imageMoveRight
                self.attackState = False
        else:
            if position == "L" and not still and not self.jumpState:
                self.image = self.imageMoveLeft
            elif position == "R" and not still and not self.jumpState:
                self.image = self.imageMoveRight
            elif still and not self.jumpState:
                if self.prevPos == "L":
                    self.image = self.imageStillLeft
                elif self.prevPos == "R":
                    self.image = self.imageStillRight
                else :
                    self.image = self.imageStillRight
            elif self.jumpState:
                if position == "L":
                    self.image = self.imageJumpLeft
                elif position == "R":
                    self.image = self.imageJumpRight
                else :
                    self.image = self.imageStillRight




        self.prevPos = position
        # print("RECTANGLE POS: " + position)
        # print("PREVIOUS POS: " + self.prevPos)
        # print("STILL " + str(still))


    def updatePosition(self, dx, dy):
        # Move the sprite
        self.rect.x += dx
        self.rect.y += dy

        # Check if the sprite is going off the screen
        if self.rect.left < 0 + SCREEN_WIDTH /2 - self.rect.width :
            self.rect.left = SCREEN_WIDTH / 2 - self.rect.width
        elif self.rect.right > SCREEN_WIDTH /2 + self.rect.width :
            self.rect.right = SCREEN_WIDTH / 2 + self.rect.width
        if self.rect.top < 0 + 30:
            self.rect.top = 0 + 30
        elif self.rect.bottom > SCREEN_HEIGHT - 30:
            self.rect.bottom = SCREEN_HEIGHT - 30


        #print("x" + str(self.rect.x))
        #print("y" + str(self.rect.y))

