#First Game: by Matthew Nicholson
#Date last modified: 4/17/19 at 6:26 PM

import pygame
import os
pygame.init()

screen_width = 1920 #width and height are standard resolution sizes for HD
screen_height = 1080
win = pygame.display.set_mode((screen_width, screen_height)) #sets the dimensions of the screen

pygame.display.set_caption("First Game")

bg = pygame.transform.scale((pygame.image.load('background.png')), (screen_width * 2, screen_height * 2)) #loads the background

idle = pygame.image.load(os.path.join('Protagonist animation', 'adventurer-idle-00.png'))

clock = pygame.time.Clock()

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x #the players horizontal position
        self.y = y #the players vertical position
        self.width = width #the players horizontal size
        self.height = height #the players vertical size
        self.vel = 25 #the speed of the player when moving
        self.isJump = False #set to true if the player presses the jump button
        self.jumpCount = 10 
        self.left = False #set to true if player is moving left
        self.right = False #set to true if the player is moving right
        self.idle = True #set to false if the player moves or jumps or attacks
        self.didAttack = False #set to true if the player uses the attack button
        self.attackDone = False #set to true if the attack animation finishes
        self.walkCount = 0
        self.idleCount = 0
        self.jumpIter = 0
        self.attackIter = 0

        #from self.walkRight to self.leftAttack,
        #these are all of the sprite animations
        #for the player, each as a list that is
        #iterated through the main loop
        self.walkRight = [pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-run-00.png'))), (self.width, self.height)),
                         pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-run-01.png'))), (self.width, self.height)),
                         pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-run-02.png'))), (self.width, self.height)),
                         pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-run-03.png'))), (self.width, self.height)),
                         pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-run-04.png'))), (self.width, self.height)),
                         pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-run-05.png'))), (self.width, self.height))]

        self.walkLeft = [pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-run-00.png'))), True, False)), (self.width, self.height)),
                        pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-run-01.png'))), True, False)), (self.width, self.height)),
                        pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-run-02.png'))), True, False)), (self.width, self.height)),
                        pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-run-03.png'))), True, False)), (self.width, self.height)),
                        pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-run-04.png'))), True, False)), (self.width, self.height)),
                        pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-run-05.png'))), True, False)), (self.width, self.height))]
        
        self.rightIdle = [pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-idle-00.png'))), (self.width, self.height)),
                          pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-idle-01.png'))), (self.width, self.height)),
                          pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-idle-02.png'))), (self.width, self.height)),
                          pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-idle-2-00.png'))), (self.width, self.height)),
                          pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-idle-2-01.png'))), (self.width, self.height)),
                          pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-idle-2-02.png'))), (self.width, self.height)),
                          pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-idle-2-03.png'))), (self.width, self.height)),
                          pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-idle-03.png'))), (self.width, self.height))]
        
        self.leftIdle = [pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-idle-00.png'))), True, False)), (self.width, self.height)),
                         pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-idle-01.png'))), True, False)), (self.width, self.height)),
                         pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-idle-02.png'))), True, False)), (self.width, self.height)),
                         pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-idle-2-00.png'))), True, False)), (self.width, self.height)),
                         pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-idle-2-01.png'))), True, False)), (self.width, self.height)),
                         pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-idle-2-02.png'))), True, False)), (self.width, self.height)),
                         pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-idle-2-03.png'))), True, False)), (self.width, self.height)),
                         pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-idle-03.png'))), True, False)), (self.width, self.height))]

        self.rightJump = [pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-jump-00.png'))), (self.width, self.height)),
                          pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-jump-01.png'))), (self.width, self.height)),
                          pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-jump-02.png'))), (self.width, self.height)),
                          pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-jump-02.png'))), (self.width, self.height)),
                          pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-jump-03.png'))), (self.width, self.height)),
                          pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-jump-03.png'))), (self.width, self.height)),
                          pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-fall-00.png'))), (self.width, self.height)),
                          pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-fall-00.png'))), (self.width, self.height)),
                          pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-fall-01.png'))), (self.width, self.height)),
                          pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-fall-01.png'))), (self.width, self.height))]

        self.leftJump = [pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-jump-00.png'))), True, False)), (self.width, self.height)),
                          pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-jump-01.png'))), True, False)), (self.width, self.height)),
                          pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-jump-02.png'))), True, False)), (self.width, self.height)),
                          pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-jump-02.png'))), True, False)), (self.width, self.height)),
                          pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-jump-03.png'))), True, False)), (self.width, self.height)),
                          pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-jump-03.png'))), True, False)), (self.width, self.height)),
                          pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-fall-00.png'))), True, False)), (self.width, self.height)),
                          pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-fall-00.png'))), True, False)), (self.width, self.height)),
                          pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-fall-01.png'))), True, False)), (self.width, self.height)),
                          pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-fall-01.png'))), True, False)), (self.width, self.height))]

        self.rightAttack = [pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-attack1-00.png'))), (self.width, self.height)),
                            pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-attack1-01.png'))), (self.width, self.height)),
                            pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-attack1-02.png'))), (self.width, self.height)),
                            pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-attack1-03.png'))), (self.width, self.height)),
                            pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-attack1-04.png'))), (self.width, self.height)),
                            pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-attack2-00.png'))), (self.width, self.height)),
                            pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-attack2-01.png'))), (self.width, self.height)),
                            pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-items-02.png'))), (self.width, self.height)),
                            pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-items-01.png'))), (self.width, self.height)),
                            pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-items-00.png'))), (self.width, self.height)),
                            pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-idle-2-00.png'))), (self.width, self.height)),
                            pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-idle-2-01.png'))), (self.width, self.height)),
                            pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-idle-2-02.png'))), (self.width, self.height)),
                            pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-idle-2-03.png'))), (self.width, self.height)),
                            pygame.transform.scale((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-idle-03.png'))), (self.width, self.height))]

        self.leftAttack = [pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-attack1-00.png'))), True, False)), (self.width, self.height)),
                                    pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-attack1-01.png'))), True, False)), (self.width, self.height)),
                                    pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-attack1-02.png'))), True, False)), (self.width, self.height)),
                                    pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-attack1-03.png'))), True, False)), (self.width, self.height)),
                                    pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-attack1-04.png'))), True, False)), (self.width, self.height)),
                                    pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-attack2-00.png'))), True, False)), (self.width, self.height)),
                                    pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-attack2-01.png'))), True, False)), (self.width, self.height)),
                                    pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-items-02.png'))), True, False)), (self.width, self.height)),
                                    pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-items-01.png'))), True, False)), (self.width, self.height)),
                                    pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-items-00.png'))), True, False)), (self.width, self.height)),
                                    pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-idle-2-00.png'))), True, False)), (self.width, self.height)),
                                    pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-idle-2-01.png'))), True, False)), (self.width, self.height)),
                                    pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-idle-2-02.png'))), True, False)), (self.width, self.height)),
                                    pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-idle-2-03.png'))), True, False)), (self.width, self.height)),
                                    pygame.transform.scale((pygame.transform.flip((pygame.image.load(os.path.join('Protagonist animation', 'adventurer-idle-03.png'))), True, False)), (self.width, self.height))]
        
    def draw(self, win):
        if self.walkCount + 1 >= 24:
            self.walkCount = 0
        if self.idleCount + 1 >= 64:
            self.idleCount = 0
        if self.jumpIter + 1 >= 40:
            self.jumpIter = 0
        if self.attackIter + 1 >= 30:
            self.attackDone = True
            self.attackIter = 0
            self.idleCount = 0
            self.walkCount = 0
        if not(self.idle):
            if self.left:
                if self.isJump:
                    win.blit(self.leftJump[self.jumpIter//4], (self.x,self.y))
                    self.jumpIter += 1
                else:
                    if self.didAttack and not(self.attackDone):
                        win.blit(self.leftAttack[self.attackIter//2], (self.x,self.y))
                        self.attackIter += 1
                    else:
                        win.blit(self.walkLeft[self.walkCount//4], (self.x,self.y))
                        self.walkCount += 1
                
            elif self.right:
                if self.isJump:
                    win.blit(self.rightJump[self.jumpIter//4], (self.x,self.y))
                    self.jumpIter += 1
                else:
                    if self.didAttack and not(self.attackDone):
                        win.blit(self.rightAttack[self.attackIter//2], (self.x,self.y))
                        self.attackIter += 1
                    else:
                        win.blit(self.walkRight[self.walkCount//4], (self.x,self.y))
                        self.walkCount += 1
        else:
            if self.didAttack and not(self.attackDone):
                if self.left:
                    win.blit(self.leftAttack[self.attackIter//2], (self.x,self.y))
                    self.attackIter += 1
                else: #self.right
                    win.blit(self.rightAttack[self.attackIter//2], (self.x,self.y))
                    self.attackIter += 1
            elif self.isJump:
                if self.left:
                    win.blit(self.leftJump[self.jumpIter//4], (self.x,self.y))
                    self.jumpIter += 1
                else: #self.right
                    win.blit(self.rightJump[self.jumpIter//4], (self.x,self.y))
                    self.jumpIter += 1
            elif self.left:
                win.blit(self.leftIdle[self.idleCount//8], (self.x,self.y))
                self.idleCount += 1        
            else: #self.right
                win.blit(self.rightIdle[self.idleCount//8], (self.x,self.y))
                self.idleCount += 1

class enemy(object):
    def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.idle = pygame.transform.scale((pygame.image.load(os.path.join('Slime animation', 'slime-idle-0.png'))), (self.width, self.height))
    def draw (self, win):
        win.blit(self.idle, (self.x,self.y))
        
def redrawGameWindow():
    win.blit(bg,(0,-1000))
    man.draw(win)
    slime.draw(win)
    pygame.display.update()

#main loop
man = player(20, 800, 300, 222)
slime = enemy(1400, 875, 192, 150) 
run = True
while run:
    clock.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
   
    if keys[pygame.K_LEFT] and man.x > man.vel:
        if man.didAttack and not(man.attackDone):
            man.walkCount = 0
        else:
            man.x -= man.vel 
            man.left = True
            man.right = False
            man.idle = False
    elif keys[pygame.K_RIGHT] and man.x < screen_width - man.width - man.vel:
        if man.didAttack and not(man.attackDone):
            man.walkCount = 0
        else:
            man.x += man.vel
            man.right = True
            man.left = False
            man.idle = False
    else:
        man.idle = True
        man.walkCount = 0
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True       
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
    if not(man.didAttack):
        if keys[pygame.K_SPACE]:
            man.didAttack = True
            man.attackDone = False
    else:
        if man.attackDone:
            man.didAttack = False
            
    redrawGameWindow()
pygame.quit()
