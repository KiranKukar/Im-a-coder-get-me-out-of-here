from site import setcopyright
import pygame   
pygame.init()

win = pygame.display.set_mode((1260, 700))

pygame.display.set_caption("I'm a Coder, Get Me Out of Here!")

walkRight = [pygame.image.load('./img/run_0.png'), pygame.image.load('./img/run_1.png'), pygame.image.load('./img/run_2.png'), pygame.image.load('./img/run_3.png'), pygame.image.load('./img/run_4.png'), pygame.image.load('./img/run_5.png')]
walkLeft = [pygame.image.load('./img/run_0_left.png'), pygame.image.load('./img/run_1_left.png'), pygame.image.load('./img/run_2_left.png'), pygame.image.load('./img/run_3_left.png'), pygame.image.load('./img/run_4_left.png'), pygame.image.load('./img/run_5_left.png')]
bg = pygame.image.load('./img/spy_wallpaper.jpeg')
char = [pygame.image.load('./img/idle_0.png')]#, pygame.image.load('./img/idle_1.png'), pygame.image.load('./img/idle_2.png'), pygame.image.load('./img/idle_3.png')]

#self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)
##built in method to flip the images

clock = pygame.time.Clock()

class player(object):
    def __init__(self,x,y,width,height):
        #starting position of sprite
        self.x = x
        self.y = y
        #dimensions of sprite
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0
        self.jumpCount = 10


# x=300
# y=300

# #dimensions of sprite
# width=120
# height=87
# vel=5

# left = False
# right = False
# up = False
# down = False
# walkCount = 0

# isJump = False
# jumpCount = 10

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft[self.walkCount//6], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//6], (self.x,self.y))
            self.walkCount +=1
        elif self.up:
            win.blit(walkRight[self.walkCount//6], (self.x,self.y))
            self.walkCount +=1
        elif self.down:
            win.blit(walkRight[self.walkCount//6], (self.x,self.y))
            self.walkCount +=1
        else:
            win.blit(char[self.walkCount//4], (self.x,self.y))

def redrawGameWindow():
    # global walkCount
    win.blit(bg, (0,0))
    spy.draw(win)

    # if walkCount + 1 >= 27:
    #     walkCount = 0

    # if left:
    #     win.blit(walkLeft[walkCount//6], (x,y))
    #     walkCount += 1
    # elif right:
    #     win.blit(walkRight[walkCount//6], (x,y))
    #     walkCount +=1
    # elif up:
    #     win.blit(walkRight[walkCount//6], (x,y))
    #     walkCount +=1
    # elif down:
    #     win.blit(walkRight[walkCount//6], (x,y))
    #     walkCount +=1
    # else:
    #     win.blit(char[walkCount//4], (x,y))
    
    pygame.display.update()

#mainloop
spy = player(200, 410, 64,64)
run = True
while run:
#   clock.tick(27)
#   #pygame.time.delay(100)
#   #check for event
  for event in pygame.event.get():
#     #loops through events
    if event.type == pygame.QUIT:
#       #if you hit big red button in corner to close window, then 
      run=False

  keys = pygame.key.get_pressed()


  if keys[pygame.K_LEFT] and spy.x > spy.vel:
        spy.x -= spy.vel
        spy.left = True
        spy.right = False
  elif keys[pygame.K_RIGHT] and spy.x < 500 - spy.width - spy.vel:
        spy.x += spy.vel
        spy.right = True
        spy.left = False
  elif keys[pygame.K_UP] and spy.y > spy.vel:
        spy.y -= spy.vel
        spy.right = True
        spy.left = False
  elif keys[pygame.K_DOWN] and spy.y < 600 - spy.height - spy.vel:
        spy.y += spy.vel
        spy.right = True
        spy.left = False

  #       if keys[pygame.K_UP] and y > vel:
  #   y -= vel
  # if keys[pygame.K_DOWN] and y < 600 - height - vel:
  #   #600 is the height limit - can change it based on size of window so sprite is limited to the boundaries of the window
  #   y += vel
  else:
        spy.right = False
        spy.left = False
        spy.walkCount = 0
        
  if not(spy.isJump):
        if keys[pygame.K_SPACE]:
            spy.isJump = True
            spy.right = False
            spy.left = False
            spy.walkCount = 0
  else:
        if spy.jumpCount >= -10:
            neg = 1
            if spy.jumpCount < 0:
                neg = -1
            spy.y -= (spy.jumpCount ** 2) * 0.5 * neg
            spy.jumpCount -= 1
        else:
            spy.isJump = False
            spy.jumpCount = 10

  
  # if keys[pygame.K_LEFT] and x > vel:
  #   x -= vel
  #   #vel changes speed of movement
  #   left = True
  #   right = False
  # elif keys[pygame.K_RIGHT] and x < 1240 - width - vel:
  #   #character not allowed to move off right of screen
  #   #1240 is the width limit - can change it based on size of window so sprite is limited to the boundaries of the window
  #   #width is the width of the character
  #   #the position of the character will not be allowed to move past the border now set the width of the character from the edge
  #   x += vel
  #   right = True
  #   left = False
  # else:
  #   right = False
  #   left = False
  #   walkCount = 0

  # if keys[pygame.K_UP] and y > vel:
  #   y -= vel
  # if keys[pygame.K_DOWN] and y < 600 - height - vel:
  #   #600 is the height limit - can change it based on size of window so sprite is limited to the boundaries of the window
  #   y += vel
  
  win.fill((0, 0, 0))
  #this will fill the background with black so you don't see a trail of red rectangles

#   #pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
#   #pygame.display.update()

        
  # if not(isJump):
  #       if keys[pygame.K_SPACE]:
  #           isJump = True
  #           right = False
  #           left = False
  #           walkCount = 0
  # else:
  #       if jumpCount >= -10:
  #           neg = 1
  #           if jumpCount < 0:
  #               neg = -1
  #           y -= (jumpCount ** 2) * 0.5 * neg
  #           jumpCount -= 1
  #       else:
  #           isJump = False
  #           jumpCount = 10
            
  redrawGameWindow()

pygame.quit()