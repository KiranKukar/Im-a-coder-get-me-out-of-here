from tkinter import TRUE
import pygame
from pygame.locals import *
from tiles import *
import spriteSheet
pygame.init()

player_img = pygame.image.load('./img/run_0.png')
player_rect = player_img.get_rect()

SCALE = 2 
BG = (185, 237, 214)
win = pygame.display.set_mode((336 * SCALE, 336 * SCALE))
win_rect = win.get_rect()


# Map stuff here
sprite_sheet_image = pygame.image.load('dungeon_sheet.png').convert_alpha()
sprite_sheet = spriteSheet.SpriteSheet(sprite_sheet_image)


map = TileMap('map21x21.csv', sprite_sheet, SCALE)
player_rect.x, player_rect.y = map.start_x, map.start_y

char = pygame.image.load('./img/idle_0.png')
walkRight = [pygame.image.load('./img/run_0.png'), pygame.image.load('./img/run_1.png'), pygame.image.load('./img/run_2.png'), pygame.image.load('./img/run_3.png'), pygame.image.load('./img/run_4.png'), pygame.image.load('./img/run_5.png')]
walkLeft = [pygame.image.load('./img/left_run_0.png'), pygame.image.load('./img/left_run_1.png'), pygame.image.load('./img/left_run_2.png'), pygame.image.load('./img/left_run_3.png'), pygame.image.load('./img/left_run_4.png'), pygame.image.load('./img/left_run_5.png')]
idle = [pygame.image.load('./img/idle_0.png'), pygame.image.load('./img/idle_1.png'), pygame.image.load('./img/idle_2.png'), pygame.image.load('./img/idle_3.png')]

#self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)
##built in method to flip the images

clock = pygame.time.Clock()

class player(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
      pygame.sprite.Sprite.__init__(self)
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
      self.rect = player_img.get_rect()
     


    

# x=300
# y=300

# #dimensions of sprite
# width=120
# height=87
# vel=5

    def draw(self, win):
      # if there is a collision
        # do the collision movement
      # elif
        #do this below
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
            win.blit(idle[self.walkCount//20], (self.x,self.y))
            self.walkCount +=1

def redrawGameWindow():
    # global walkCount
    map.draw_map(win)
    # win.blit(map, (0,0))   #This will draw our background image at (0,0)
                          #In pygame the top left corner of the screen is (0,0) and the bottom right is (width, height). This means to move up we subtract from the y of our character and to move down we add to the y.
    # spy.rect, collision_types = move(player_rect, player_movement, map.tiles_rects)

    spy.draw(win)

    
    pygame.display.update()



def collision_test(rect, tiles): # rect of player and list of tiles
  hit_list = []
  for tile in tiles:
    if rect.colliderect(tile):
      hit_list.append(tile)
  return hit_list



def move(rect, movement, tile): #rect of player, movement of player, put tile - should it be tiles?
  collision_types = { 'top': False, 'bottom': False, 'right': False, 'left': False }
  rect.x += movement[0] # check the moevemt is how it's in our codes
  hit_list = collision_test(rect, tile)
  for hit_tile in hit_list:
    tile_rect = Rect(hit_tile)
    print(hit_tile)
    print(f'hit_list {hit_list}')
    if movement[0] <= tile_rect.left:
      print(spy.left)
      print(tile_rect.left)
      spy.x = tile_rect.left
      collision_types['right'] = True
      # print(collision_types['right'], hit_tile)

    if movement[0] <= tile_rect.right:
      spy.x = tile_rect.right
      collision_types['left'] = True
      # print(collision_types['left'], hit_tile)
  rect.y += movement[1]
  hit_list = collision_test(rect, tile)
  for hit_tile in hit_list:
    tile_rect = Rect(hit_tile)
    if movement[1] >= tile_rect.top:
      spy.y = tile_rect.top - spy.height
      collision_types['bottom'] = True
      # print(collision_types['bottom'], hit_tile)

    if movement[1] <= tile_rect.bottom:
      spy.y = tile_rect.bottom
      collision_types['top'] = True
      # print(collision_types['top'], hit_tile)
  return rect, collision_types

#mainloop
spy = player(300, 410, 64,64)
run = True

while run:
  win.fill(BG)
#   clock.tick(27)
#   #pygame.time.delay(100)   #This will delay the game the given amount of milliseconds. In our casee 0.1 seconds will be the delay
#   #check for event
  for event in pygame.event.get():   #This will loop through a list of any keyboard or mouse events.
    if event.type == pygame.QUIT:   #Checks if the red button in the corner of the window is clicked
#       #if you hit big red button in corner to close window, then game will end also
      run=False   #Ends the game loop

  keys = pygame.key.get_pressed()   #This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.

  player_movement = [spy.x, spy.y]
  player_rect = spy.rect
  spy.rect, collision_types = move(player_rect, player_movement, map.tiles_rects)

  if keys[pygame.K_LEFT] and collision_types['left'] == False:   #vel changes speed of movement
        spy.x -= spy.vel # sets locatioin of spy - and does the same below
        spy.left = True
        spy.right = False
        

  elif keys[pygame.K_RIGHT] and collision_types['right'] == False:
        #character not allowed to move off right of screen
        #1240 is the width limit - can change it based on size of window so sprite is limited to the boundaries of the window
        #width is the width of the character
        #the position of the character will not be allowed to move past the border now set the width of the character from the edge
        spy.x += spy.vel
        
        spy.right = True
        spy.left = False
        

  elif keys[pygame.K_UP] and collision_types['top'] == False:
        spy.y -= spy.vel
        
        spy.right = True
        spy.left = False
       

  elif keys[pygame.K_DOWN] and collision_types['bottom'] == False:   #700 is the height limit - can change it based on size of window so sprite is limited to the boundaries of the window
        spy.y += spy.vel
        
        spy.right = True
        spy.left = False

  else:
        spy.right = False
        spy.left = False
        spy.up = False
        spy.down = False
  

  if not(spy.isJump):
        if keys[pygame.K_SPACE]:
            spy.isJump = True
            spy.right = False
            spy.left = False
            spy.walkCount = 0
  else:
        if spy.jumpCount >= -5:
            neg = 1
            if spy.jumpCount < 0:
                neg = -1
            spy.y -= (spy.jumpCount ** 2) * 0.5 * neg
            spy.jumpCount -= 1
        else:
            spy.isJump = False
            spy.jumpCount = 5
  
  #this will fill the background with black so you don't see a trail of red rectangles

#   #pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))   #This takes: window/surface, color, rect
#   #pygame.display.update()   #This updates the screen so we can see our rectangle
            
  redrawGameWindow()

pygame.quit()   #If we exit the loop this will execute and close our game