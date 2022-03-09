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




SCALE = 2
WIN_WIDTH = 336 * SCALE
WIN_HEIGHT = 336 * SCALE
BG = (185, 237, 214)
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("I'm a Coder, Get Me Out of Here!")

# Popup GUI
popup = Popup(WIN_WIDTH, WIN_HEIGHT)
questions = Questions(popup, WIN_WIDTH, WIN_HEIGHT)
popup_open = False

# Map Tiling
sprite_sheet_image = pygame.image.load('dungeon_sheet.png').convert_alpha()
sprite_sheet = spriteSheet.SpriteSheet(sprite_sheet_image)

map = TileMap('map21x21.csv', sprite_sheet, SCALE)


clock = pygame.time.Clock()   #Used to manage how fast the screen updates

# Timer for Popup Manager GUI
time_delta = clock.tick(60)/1000.0




def laptopCollision():
  if pygame.sprite.spritecollideany(spy, map.laptop1):
    print('laptop 1 collision')
    # set up a question
  if pygame.sprite.spritecollideany(spy, map.laptop2):
    print('laptop 2 collision')
    # set up a question
  if pygame.sprite.spritecollideany(spy, map.laptop3):
    print('laptop 3 collision')
    # set up a question
  if pygame.sprite.spritecollideany(spy, map.laptop4):
    print('laptop 4 collision')
    # set up a question
  if pygame.sprite.spritecollideany(spy, map.laptop5):
    print('laptop 5 collision')
    # set up a question
  if pygame.sprite.spritecollideany(spy, map.laptop6):
    print('laptop 6 collision')
    # set up a question

def update(spy, keys):
  global canCollide, blocked
  if pygame.sprite.spritecollideany(spy, map.laptop_group) and keys[pygame.K_a]:
    laptopCollision()
  else:
    if pygame.sprite.spritecollideany(spy, map.tile_group) and canCollide:
        if keys[pygame.K_UP]:
            blocked = 'up'
            spy.rect.move_ip(0, spy.vel)
        if keys[pygame.K_DOWN]:
            blocked = 'down'
            spy.rect.move_ip(0, -spy.vel)
        if keys[pygame.K_LEFT]:
            blocked = 'left'
            spy.rect.move_ip(spy.vel, 0)
        if keys[pygame.K_RIGHT]:
            blocked = 'right'
            spy.rect.move_ip(-spy.vel, 0)
        canCollide = False
    else:
        canCollide = True
        if keys[pygame.K_LEFT] and not blocked == 'left': 
                spy.rect.move_ip(-spy.vel, 0)
                spy.left = True
                spy.right = False
        elif keys[pygame.K_RIGHT] and not blocked == 'right':
                spy.rect.move_ip(spy.vel, 0)
                spy.right = True
                spy.left = False
        elif keys[pygame.K_UP] and not blocked == 'up':
                spy.rect.move_ip(0, -spy.vel)
                spy.right = True
                spy.left = False
        elif keys[pygame.K_DOWN] and not blocked == 'down':
                spy.rect.move_ip(0, spy.vel)
                spy.right = True
                spy.left = False
        else:
                spy.right = False
                spy.left = False
                # spy.walkCount = 0
        blocked = ''
    

def redrawGameWindow():
    map.draw_map(win)
    spy.draw(win)
    popup.manager.draw_ui(win)
    
    
    pygame.display.update()


#mainloop
spy = Player(250, 350, 17, 17)

canCollide = True
blocked = ''

run = True
while run:
  win.fill(BG)
  # clock.tick(27)

#EVENT PROCESSING LOOP
  for event in pygame.event.get():   #This event processing loop will loop through a list of any keyboard or mouse events.
    if event.type == pygame.QUIT:   #Checks if the red button in the corner of the window is clicked
      run=False   #Ends the game loop

    # if event.type == questions.question_textbox.
    #   questions.question_textbox.hide()

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
  
  update(spy, keys)

#   if keys[pygame.K_LEFT] and popup_open == False:   #vel changes speed of movement
#         spy.x -= spy.vel
#         spy.left = True
#         spy.right = False
#         questions.question_ui.hide_all()
#   elif keys[pygame.K_RIGHT] and popup_open == False:
#         #character not allowed to move off right of screen
#         #1240 is the width limit - can change it based on size of window so sprite is limited to the boundaries of the window
#         #width is the width of the character
#         #the position of the character will not be allowed to move past the border now set the width of the character from the edge
#         spy.x += spy.vel
#         spy.right = True
#         spy.left = False
#         questions.question_ui.hide_all()
#   elif keys[pygame.K_UP] and popup_open == False:
#         spy.y -= spy.vel
#         spy.right = True
#         spy.left = False
#         questions.question_ui.hide_all()
#   elif keys[pygame.K_DOWN] and popup_open == False:   #700 is the height limit - can change it based on size of window so sprite is limited to the boundaries of the window
#         spy.y += spy.vel
#         spy.right = True
#         spy.left = False
#         questions.question_ui.hide_all()
#   elif keys[pygame.K_a]:
#         print('pressed a')
#   elif keys[pygame.K_b]:
#         print('pressed b')

#   elif keys[pygame.K_1]:
#     questions.load_question(questions.q1.question_info)
#     if questions.q1.question_info.answered == "no":
#       popup_open = True
    
#   elif keys[pygame.K_2]:
#     questions.question_ui.hide_all()
#     popup_open = False

#   elif keys[pygame.K_ESCAPE]:
#         break
#   else:
#         spy.right = False
#         spy.left = False

  

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
