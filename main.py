from tkinter import TRUE
import pygame
from tiles import *
import spriteSheet
pygame.init()

player_img = pygame.image.load('./img/run_0.png')
player_rect = player_img.get_rect()

SCALE = 2
BG = (211, 211, 211)
win = pygame.display.set_mode((320 * SCALE, 320 * SCALE))


# Map stuff here!
sprite_sheet_image = pygame.image.load('dungeon_sheet.png').convert_alpha()
sprite_sheet = spriteSheet.SpriteSheet(sprite_sheet_image)


map = TileMap('map.csv', 'map.tmx', sprite_sheet, SCALE)
player_rect.x, player_rect.y = map.start_x, map.start_y

pygame.display.set_caption("I'm a Coder, Get Me Out of Here!")

walkRight = [pygame.image.load('./img/run_0.png'), pygame.image.load('./img/run_1.png'), pygame.image.load('./img/run_2.png'), pygame.image.load('./img/run_3.png'), pygame.image.load('./img/run_4.png'), pygame.image.load('./img/run_5.png')]
walkLeft = [pygame.image.load('./img/run_0.png'), pygame.image.load('./img/run_1.png'), pygame.image.load('./img/run_2.png'), pygame.image.load('./img/run_3.png'), pygame.image.load('./img/run_4.png'), pygame.image.load('./img/run_5.png')]
# bg = pygame.image.load('./hacker.jpeg')
char = pygame.image.load('./img/idle_0.png')

clock = pygame.time.Clock()

#starting position of sprite
x=300
y=300

#dimensions of sprite
width=120
height=87
vel=5

left = False
right = False
up = False
down = False
walkCount = 0

isJump = False
jumpCount = 3

def redrawGameWindow():
    global walkCount
    # win.blit(bg, (0,0))
    map.draw_map(win)

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//5], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//5], (x,y))
        walkCount +=1
    elif up:
        win.blit(walkRight[walkCount//5], (x,y))
        walkCount +=1
    elif down:
        win.blit(walkRight[walkCount//5], (x,y))
        walkCount +=1
    else:
        win.blit(char, (x,y))

    
    pygame.display.update()

#mainloop
run = True
while run:
  win.fill(BG)
#   clock.tick(27)
#   #pygame.time.delay(100)
#   #check for event
  for event in pygame.event.get():
#     #loops through events
    if event.type == pygame.QUIT:
#       #if you hit big red button in corner to close window, then 
      run=False

  keys = pygame.key.get_pressed()
  
  if keys[pygame.K_LEFT] and x > vel:
    x -= vel
    #vel changes speed of movement
    left = True
    right = False
  elif keys[pygame.K_RIGHT] and x < 1240 - width - vel:
    #character not allowed to move off right of screen
    #1240 is the width limit - can change it based on size of window so sprite is limited to the boundaries of the window
    #width is the width of the character
    #the position of the character will not be allowed to move past the border now set the width of the character from the edge
    x += vel
    right = True
    left = False
  elif keys[pygame.K_UP] and x < 1240 - width - vel:
    up = True
    right = False
    left = False
  elif keys[pygame.K_DOWN] and x < 1240 - width - vel:
    down = True
    right = True
    left = False
  else:
    right = False
    left = False
    up = False
    down = False

  if keys[pygame.K_UP] and y > vel:
    y -= vel
  if keys[pygame.K_DOWN] and y < 600 - height - vel:
    #600 is the height limit - can change it based on size of window so sprite is limited to the boundaries of the window
    y += vel
  
  # win.fill((0, 0, 0))
  #this will fill the background with black so you don't see a trail of red rectangles

#   #pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
#   #pygame.display.update()

        
  if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
  else:
        if jumpCount >= -3:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 3
            
  redrawGameWindow()

pygame.quit()