import pygame
import pygame_gui

class Popup():
    def __init__(self, win_width, win_height):
      self.manager = pygame_gui.UIManager((win_width, win_height)) 
      self.win_width = win_width
      self.win_height = win_height

    def question(self, question, answers):
      ui_window_percentage_size = 0.75
      ui_window_padding = self.win_width * (1 - ui_window_percentage_size)
      display_title = "Question x"
      self.ui_window = Window(ui_window_padding/2, ui_window_padding/2, self.win_width - ui_window_padding, self.win_height - ui_window_padding, display_title, self.manager)

      question_text = question
      question_textbox = Textbox(50, 40, 375, 150, question_text, self.manager, self.ui_window.element)
      question_textbox.text_effect_typing_appear()

      answer_button_padding_left = 50
      answer_button_width = 375
      answer_button_height = 50

      answer_button_1 = Button(answer_button_padding_left, 205, answer_button_width, answer_button_height, answers[0], self.manager, self.ui_window.element)
      answer_button_2 = Button(answer_button_padding_left, 255, answer_button_width, answer_button_height, answers[1], self.manager, self.ui_window.element)
      answer_button_3 = Button(answer_button_padding_left, 305, answer_button_width, answer_button_height, answers[2], self.manager, self.ui_window.element)
      answer_button_4 = Button(answer_button_padding_left, 355, answer_button_width, answer_button_height, answers[3], self.manager, self.ui_window.element)

class Window():
  def __init__(self, left_padding, top_padding, width, height, display_title, manager):
      self.element = pygame_gui.elements.UIWindow(
                       rect=pygame.Rect(left_padding, top_padding, width, height),
                       window_display_title=f'{display_title}',
                       manager=manager)

class Button():
  def __init__(self, left_padding, top_padding, width, height, text, manager, container):
    self.element = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect(left_padding, top_padding, width, height),
                        text=f'{text}',
                        manager=manager,
                        container=container)

class Textbox():
  def __init__(self, left_padding, top_padding, width, height, html_text, manager, container):
    self.element = pygame_gui.elements.UITextBox(
                        relative_rect=pygame.Rect(left_padding, top_padding, width, height),
                        html_text=f'<font color=#03A062><b>{html_text}</b></font>',
                        manager=manager,
                        container=container)        

  def text_effect_typing_appear(self):
    self.element.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR, params = {'time_per_letter': .01})

