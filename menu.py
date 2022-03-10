# Setup Python 
from socket import EAI_SYSTEM
from tkinter import Button
import pygame, sys
 
# Setup pygame/window 
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Menu feature')
screen = pygame.display.set_mode((672, 672),0,32)
pygame.display.set_caption("I'm a Coder, Get Me Out of Here!")
 
font = pygame.font.SysFont('consolas', 60)
smallText = pygame.font.SysFont('Verdana', 35)
 
def draw_text(text, font, colour, surface, x, y):
    textobj = font.render(text, 1, colour) 
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

#Adding a click variable
click = False
 
def main_menu():
    while True:
 
        screen.fill((0,0,0))
        draw_text('main menu', font, (255, 255, 255), screen, 80, 50)
 
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(175, 200, 372, 75)
        button_2 = pygame.Rect(175, 300, 372, 75)
        button_3 = pygame.Rect(175, 400, 372, 75)

        if button_1.collidepoint((mx, my)):
            if click:
                game_easy()
        if button_2.collidepoint((mx, my)):
            if click:
                game_hard()
        if button_3.collidepoint((mx, my)):
            if click:
                how_to_play()


        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        pygame.draw.rect(screen, (255, 0, 0), button_3)
        draw_text('Easy Mode', smallText, (255, 255, 255), screen, 265, 215)
        draw_text('Hard Mode', smallText, (255, 255, 255), screen, 265, 315)
        draw_text('How to Play', smallText, (255, 255, 255), screen, 255, 415)
        
        #Resets click to false after every frame. 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
def game_easy():
  exec(open("main.py").read())
  mode = 'easy'
  return mode

def game_hard():
  mode = 'hard'
  return mode
 
def how_to_play():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('how to play', font, (255,255, 255), screen, 80, 50)
        draw_text('Movement:', smallText, (255, 0, 0), screen, 120, 200)
        draw_text('Action:', smallText, (255, 0, 0), screen, 195, 250)
        draw_text('Exit:', smallText, (255, 0, 0), screen, 240, 300)
        draw_text('Arrow Keys', smallText, (255, 100, 0), screen, 330, 200)
        draw_text('Space Bar', smallText, (255, 100, 0), screen, 330, 250)
        draw_text('Esc Key', smallText, (255, 100, 0), screen, 330, 300)

        draw_text('Answer the Questions', smallText, (0, 255, 0), screen, 135, 400)
        draw_text('Solve the Riddle', smallText, (0, 255, 0), screen, 180, 450)
        draw_text('Escape the Room', smallText, (0, 255, 0), screen, 175, 500)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
main_menu()