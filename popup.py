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

      answers = [
        "Answer 1 goes here.",
        "Answer 2 goes here.",
        "Answer 3 goes here.",
        "Answer 4 goes here.",
      ]



      answer_button_1 = Button(answer_button_padding_left, 205, answer_button_width, answer_button_height, answers[0], self.manager, self.ui_window)
      answer_button_2 = Button(answer_button_padding_left, 255, answer_button_width, answer_button_height, answers[1], self.manager, self.ui_window)
      answer_button_3 = Button(answer_button_padding_left, 305, answer_button_width, answer_button_height, answers[2], self.manager, self.ui_window)
      answer_button_4 = Button(answer_button_padding_left, 355, answer_button_width, answer_button_height, answers[3], self.manager, self.ui_window)

      question_text = "Hello there, can you tell me, what is the best way to why are you going to how come the first time a which way up is the what?"
      question_textbox = Textbox(50, 40, 375, 150, question_text, self.manager, self.ui_window)
      question_textbox.text_effect_typing_appear()

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
                        html_text=f'{html_text}',
                        manager=manager,
                        container=container)        

  def text_effect_typing_appear(self):
    self.element.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR, params = {'time_per_letter': .01})


                      
          


