from tkinter import TRUE
import pygame
import spriteSheet
import pygame_gui

import menu
from map import *
from player import *
from popup import *
from question_info import *
from question import *

pygame.init()

MODE = 'easy' # type easy or hard
SCALE = 2
WIN_WIDTH = 336 * SCALE
WIN_HEIGHT = 336 * SCALE
BG = (185, 237, 214)
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("I'm a Coder, Get Me Out of Here!")

#Game music
# music = pygame.mixer.music.load('./sounds/MissionImpossibleTheme.mp3')
# pygame.mixer.music.play(-1)
# pygame.mixer.music.set_volume(0.1)

# question_sound = pygame.mixer.Sound('./sounds/mixkit-game-level-music-689.wav')
# question_sound.play()   #add this after the action you want it to play


# Popup GUI
popup = Popup(WIN_WIDTH, WIN_HEIGHT)
questions = Questions(popup, WIN_WIDTH, WIN_HEIGHT, MODE)
popup_open = True

# Map Tiling
sprite_sheet_image = pygame.image.load('dungeon_sheet.png').convert_alpha()
sprite_sheet = spriteSheet.SpriteSheet(sprite_sheet_image)


map_instance = Map(sprite_sheet, SCALE)

# Clock to manage how fast the screen updates
clock = pygame.time.Clock()   

# Collision functions
def laptopCollision():
  global popup_open
  if pygame.sprite.spritecollideany(spy, map.laptop1):
    print('laptop 1 collision')
    questions.load_question(questions.q1.question_info)
    if questions.q1.question_info.answered == "no":
      popup_open = True
  if pygame.sprite.spritecollideany(spy, map.laptop2):
    print('laptop 2 collision')
    questions.load_question(questions.q2.question_info)
    if questions.q2.question_info.answered == "no":
      popup_open = True
  if pygame.sprite.spritecollideany(spy, map.laptop3):
    print('laptop 3 collision')
    questions.load_question(questions.q3.question_info)
    if questions.q3.question_info.answered == "no":
      popup_open = True
  if pygame.sprite.spritecollideany(spy, map.laptop4):
    print('laptop 4 collision')
    questions.load_question(questions.q4.question_info)
    if questions.q4.question_info.answered == "no":
      popup_open = True
  if pygame.sprite.spritecollideany(spy, map.laptop5):
    print('laptop 5 collision')
    questions.load_question(questions.q5.question_info)
    if questions.q5.question_info.answered == "no":
      popup_open = True
  if pygame.sprite.spritecollideany(spy, map.laptop6):
    print('laptop 6 collision')
    questions.load_question(questions.q6.question_info)
    if questions.q6.question_info.answered == "no":
      popup_open = True


def exitdoorCollision():
  global popup_open, run
  if pygame.sprite.spritecollideany(spy, map.exit_door):
    print('exit door collision')
    if map_instance.end == True:
      run = False
      print('1')
    else:
      questions.load_passcode()
      popup_open = True
      print('2')
  return run

# Keys (with collision block)
def update(spy, keys):
  global canCollide, blocked, popup_open
  if pygame.sprite.spritecollideany(spy, map.laptop_group) and keys[pygame.K_SPACE] and popup_open == False:
    laptopCollision()
  if pygame.sprite.spritecollideany(spy, map.exit_door) and keys[pygame.K_SPACE] and popup_open == False:
    exitdoorCollision()
  else:
    if pygame.sprite.spritecollideany(spy, map.tile_group) and canCollide:
        if keys[pygame.K_UP] and spy.rect.y < 620 and popup_open == False:
            blocked = 'up'
            spy.rect.move_ip(0, spy.vel+5)
            questions.question_ui.hide_all()
        if keys[pygame.K_DOWN] and spy.rect.y > 50 and popup_open == False:
            blocked = 'down'
            spy.rect.move_ip(0, -spy.vel-5)
            questions.question_ui.hide_all()
        if keys[pygame.K_LEFT] and spy.rect.x < 620 and popup_open == False:
            blocked = 'left'
            spy.rect.move_ip(spy.vel+5, 0)
            questions.question_ui.hide_all()
        if keys[pygame.K_RIGHT] and spy.rect.x > 30 and popup_open == False:
            blocked = 'right'
            spy.rect.move_ip(-spy.vel-5, 0)
            questions.question_ui.hide_all()
        canCollide = False
    else:
        canCollide = True
        if keys[pygame.K_LEFT] and not blocked == 'left' and spy.rect.x > 30 and popup_open == False: 
                spy.rect.move_ip(-spy.vel, 0)
                spy.left = True
                spy.right = False
                questions.question_ui.hide_all()
        elif keys[pygame.K_RIGHT] and not blocked == 'right' and spy.rect.x < 620 and popup_open == False:
                spy.rect.move_ip(spy.vel, 0)
                spy.right = True
                spy.left = False
                questions.question_ui.hide_all()
        elif keys[pygame.K_UP] and not blocked == 'up' and spy.rect.y > 50 and popup_open == False:
                spy.rect.move_ip(0, -spy.vel)
                spy.right = True
                spy.left = False
                questions.question_ui.hide_all()
        elif keys[pygame.K_DOWN] and not blocked == 'down' and spy.rect.y < 620 and popup_open == False:
                spy.rect.move_ip(0, spy.vel)
                spy.right = True
                spy.left = False
                questions.question_ui.hide_all()
        else:
                spy.right = False
                spy.left = False
                # spy.walkCount = 0
        blocked = ''

def redrawGameWindow():

    # Draws map / spy / popups
    map.draw_map(win)
    if map_instance.end == True:
      win.blit(pygame.image.load('./img/x_2.png'), (spy.rect.x,spy.rect.y))
    else:
      spy.draw(win)
    popup.manager.draw_ui(win)
    
    pygame.display.update()

#mainloop
spy = Player(321, 550, 33, 34)

canCollide = True
blocked = ''

def game():
    run = True
    while run:
        win.fill(BG)
        map = map_instance.map
        intro = True

    # Timer for Popup Manager GUI
        time_delta = clock.tick(60)/1000.0

    # Event Processing Loop
    for event in pygame.event.get():   #This event processing loop will loop through a list of any keyboard or mouse events.
        if event.type == pygame.QUIT:   #Checks if the red button in the corner of the window is clicked
            run=False   #Ends the game loop

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            for button in questions.answer_buttons:    
                if event.ui_element == button:
                    print('button')
            if button.text == questions.loaded_question_info.correct_answer:
                questions.question_answered('correctly')
                map_instance.change_map()
            else:
                questions.question_answered('incorrectly')
                map_instance.change_map()
            popup_open = False

        if event.type == pygame_gui.UI_WINDOW_CLOSE:
            if event.ui_element == questions.question_ui.ui_window.element:
                print("Question window closed")
            questions.question_ui = Question_ui(popup.manager, WIN_WIDTH, WIN_HEIGHT)

        if event.ui_element == questions.passcode_ui.passcode_window.element:
            print("Passcode window closed")
            questions.passcode_ui = Passcode_ui(popup.manager, WIN_WIDTH, WIN_HEIGHT, questions.anagram, MODE)
        popup_open = False

        if event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
            if event.ui_element == questions.passcode_ui.passcode_entrybox.element:
                print("Entered text:", event.text)
            if event.text.upper() == questions.anagram.anagram:
                print("correct")
            questions.anagram_correct()
            map_instance.final_map()
            popup_open = False

        popup.manager.process_events(event)
    popup.manager.update(time_delta)
    

    keys = pygame.key.get_pressed()
    #This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.
    # if keys[pygame.K_ESCAPE]:
    #     # break

    update(spy, keys)

    if not(spy.isJump):
            if keys[pygame.K_SPACE]:
                spy.isJump = True
                spy.right = False
                spy.left = False
                spy.walkCount = 0
                if intro:
                    intro = False
                questions.intro_ui.hide_all()
                popup_open = False
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
menu