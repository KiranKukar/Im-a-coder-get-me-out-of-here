# Setup Python 
from tkinter import Button
import pygame, sys
 
# Setup pygame/window 
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Menu feature')
screen = pygame.display.set_mode((500, 500),0,32)
 
font = pygame.font.SysFont('consolas', 60)
smallText = pygame.font.SysFont('arial', 20)
 
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
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(50, 100, 200, 50)
        # textSurf, textRect = button_1("Start game!", smallText)
        # textRect.center = ( (150+(100/2)), (450+(50/2)) )
        # gameDisplay.blit(textSurf, textRect)

        button_2 = pygame.Rect(50, 200, 200, 50)
        #This is to select the box with your mouse.
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        
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
 
def game():
    running = True
    while running:
        screen.fill((0,0,0))
        
        draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
def options():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('options', font, (255, 255, 255), screen, 20, 20)
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
