import pygame
import pygame_gui

class Popup():
    def __init__(self, win_width, win_height):
      self.manager = pygame_gui.UIManager((win_width, win_height)) 

      ui_window_percentage_size = 0.75
      ui_window_padding = win_width * (1 - ui_window_percentage_size)
      popup_layout_rect = pygame.Rect(ui_window_padding/2, ui_window_padding/2, win_width - ui_window_padding, win_height - ui_window_padding)
      self.ui_window = pygame_gui.elements.UIWindow(rect = popup_layout_rect,
                       window_display_title=' Question ?',
                       manager=self.manager
                       )

      ui_window_width = win_width - ui_window_padding
      ui_window_height = win_height - ui_window_padding
      button_percentage_size = 0.50
      button_padding = ui_window_width * (1 - button_percentage_size)

      
      answer_button_padding_left = 50
      answer_button_width = 375
      answer_button_height = 50

      answer_button_rect_1 = pygame.Rect(answer_button_padding_left, 230, answer_button_width, answer_button_height)
      answer_button_rect_2 = pygame.Rect(answer_button_padding_left, 280, answer_button_width, answer_button_height)
      answer_button_rect_3 = pygame.Rect(answer_button_padding_left, 330, answer_button_width, answer_button_height)
      answer_button_rect_4 = pygame.Rect(answer_button_padding_left, 380, answer_button_width, answer_button_height)
      question_rect = pygame.Rect(50, 50, 375, 300)

      self.answer_button_1 = pygame_gui.elements.UIButton(
                             relative_rect=answer_button_rect_1,
                             text='Click me to make me disappear',
                             manager=self.manager,
                             container=self.ui_window)

      self.answer_button_2 = pygame_gui.elements.UIButton(
                             relative_rect=answer_button_rect_2,
                             text='Click me to make me disappear',
                             manager=self.manager,
                             container=self.ui_window)

      self.answer_button_3 = pygame_gui.elements.UIButton(
                             relative_rect=answer_button_rect_3,
                             text='Click me to make me disappear',
                             manager=self.manager,
                             container=self.ui_window)

      self.answer_button_4 = pygame_gui.elements.UIButton(
                             relative_rect=answer_button_rect_4,
                             text='Click me to make me disappear',
                             manager=self.manager,
                             container=self.ui_window)    

      self.question_label = pygame_gui.elements.UILabel(
                             relative_rect=question_rect,
                             text='Question text, what is the time?',
                             manager=self.manager,
                             container=self.ui_window)      

    
      self.question_label.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR, params = {'time_per_letter': .05})
