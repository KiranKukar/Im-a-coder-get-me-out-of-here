import pygame

class Player(object):
    def __init__(self,x,y,width,height):
        #starting position of sprite
        self.x = x
        self.y = y
        #dimensions of sprite
        self.width = width
        self.height = height
        self.vel = 5
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0
        self.isJump = False
        self.jumpCount = 5
        self.char = pygame.image.load('./img/idle_0.png')
        self.walkRight = [pygame.image.load('./img/run_0.png'), pygame.image.load('./img/run_1.png'), pygame.image.load('./img/run_2.png'), pygame.image.load('./img/run_3.png'), pygame.image.load('./img/run_4.png'), pygame.image.load('./img/run_5.png')]
        self.walkLeft = [pygame.image.load('./img/left_run_0.png'), pygame.image.load('./img/left_run_1.png'), pygame.image.load('./img/left_run_2.png'), pygame.image.load('./img/left_run_3.png'), pygame.image.load('./img/left_run_4.png'), pygame.image.load('./img/left_run_5.png')]
        self.idle = [pygame.image.load('./img/idle_0.png'), pygame.image.load('./img/idle_1.png'), pygame.image.load('./img/idle_2.png'), pygame.image.load('./img/idle_3.png')]


    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            win.blit(self.walkLeft[self.walkCount//6], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(self.walkRight[self.walkCount//6], (self.x,self.y))
            self.walkCount +=1
        elif self.up:
            win.blit(self.walkRight[self.walkCount//6], (self.x,self.y))
            self.walkCount +=1
        elif self.down:
            win.blit(self.walkRight[self.walkCount//6], (self.x,self.y))
            self.walkCount +=1
        else:
            win.blit(self.idle[self.walkCount//20], (self.x,self.y))
            self.walkCount +=1
