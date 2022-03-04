import pygame
import pygame_gui

class Popup():
    def __init__(self, win_width, win_height):
      self.manager = pygame_gui.UIManager((win_width, win_height))
      self.hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 275), (500, 50)),
                          text='Click me to make me disappear',
                          manager=self.manager)  
