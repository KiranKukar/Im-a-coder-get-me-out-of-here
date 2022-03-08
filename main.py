from tkinter import TRUE
import pygame
import spriteSheet
import pygame_gui
import time

from tiles import *
from player import *
from popup import *
from question_info import *
from question import *

pygame.init()

player_img = pygame.image.load('./img/run_0.png')
player_rect = player_img.get_rect()

SCALE = 2
WIN_WIDTH = 336 * SCALE
WIN_HEIGHT = 336 * SCALE
BG = (185, 237, 214)
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# Popup GUI
popup = Popup(WIN_WIDTH, WIN_HEIGHT)
questions = Questions(popup, WIN_WIDTH, WIN_HEIGHT)

# Map Tiling
sprite_sheet_image = pygame.image.load('dungeon_sheet.png').convert_alpha()
sprite_sheet = spriteSheet.SpriteSheet(sprite_sheet_image)


map = TileMap('map21x21.csv', sprite_sheet, SCALE)
player_rect.x, player_rect.y = map.start_x, map.start_y

#self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)
##built in method to flip the images

clock = pygame.time.Clock()   #Used to manage how fast the screen updates

# Timer for Popup Manager GUI
time_delta = clock.tick(60)/1000.0

def redrawGameWindow():
    # global walkCount
    map.draw_map(win)
    # win.blit(map, (0,0))   #This will draw our background image at (0,0)
                          #In pygame the top left corner of the screen is (0,0) and the bottom right is (width, height). This means to move up we subtract from the y of our character and to move down we add to the y.
    spy.draw(win)
    popup.manager.draw_ui(win)
    
    pygame.display.update()

spy = Player(304, 550, 64, 64)
run = True
while run:
  win.fill(BG)
  # clock.tick(27)

#EVENT PROCESSING LOOP
  for event in pygame.event.get():   #This event processing loop will loop through a list of any keyboard or mouse events.
    if event.type == pygame.QUIT:   #Checks if the red button in the corner of the window is clicked
      run=False   #Ends the game loop

    if event.type == pygame_gui.UI_BUTTON_PRESSED:
      for button in questions.answer_buttons:    
        if event.ui_element == button:
          if button.text == questions.loaded_question_info.correct_answer:
            questions.question_answered('correctly')
          else:
            questions.question_answered('incorrectly')
          popup_open = False

  popup.manager.process_events(event)
  popup.manager.update(time_delta)
  
  

  keys = pygame.key.get_pressed()   #This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.

  if keys[pygame.K_LEFT] and popup_open == False:   #vel changes speed of movement
        spy.x -= spy.vel
        spy.left = True
        spy.right = False
        questions.question_ui.hide_all()
  elif keys[pygame.K_RIGHT] and popup_open == False:
        #character not allowed to move off right of screen
        #1240 is the width limit - can change it based on size of window so sprite is limited to the boundaries of the window
        #width is the width of the character
        #the position of the character will not be allowed to move past the border now set the width of the character from the edge
        spy.x += spy.vel
        spy.right = True
        spy.left = False
        questions.question_ui.hide_all()
  elif keys[pygame.K_UP] and popup_open == False:
        spy.y -= spy.vel
        spy.right = True
        spy.left = False
        questions.question_ui.hide_all()
  elif keys[pygame.K_DOWN] and popup_open == False:   #700 is the height limit - can change it based on size of window so sprite is limited to the boundaries of the window
        spy.y += spy.vel
        spy.right = True
        spy.left = False
        questions.question_ui.hide_all()
  elif keys[pygame.K_a]:
        print('pressed a')
  elif keys[pygame.K_b]:
        print('pressed b')

  elif keys[pygame.K_1]:
    questions.load_question(questions.q1.question_info)
    popup_open = True
  elif keys[pygame.K_2]:
    questions.question_ui.hide_all()
    popup_open = False



  elif keys[pygame.K_ESCAPE]:
        break
  else:
        spy.right = False
        spy.left = False
        
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
            
  redrawGameWindow()

pygame.quit()   #If we exit the loop this will execute and close our game
