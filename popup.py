import pygame
import pygame_gui

class Popup():
    def __init__(self, win_width, win_height):
      self.manager = pygame_gui.UIManager((win_width, win_height)) 
      self.win_width = win_width
      self.win_height = win_height

    def question_ui(self, question):
      Question_ui(self.manager, question, self.win_width, self.win_height)


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

class Question_ui():
  def __init__(self, manager, question_info, win_width, win_height):
    self.manager = manager
    self.question = question_info.question
    self.answers = question_info.answers

    self.create_ui_window(win_width, win_height)
    self.create_textbox()
    self.create_buttons()
    self.hide_all()


  def create_ui_window(self, win_width, win_height):
    ui_window_percentage_size = 0.75
    ui_window_padding = win_width * (1 - ui_window_percentage_size)
    display_title = "Question"
    self.ui_window = Window(ui_window_padding/2, ui_window_padding/2, win_width - ui_window_padding, win_height - ui_window_padding, display_title, self.manager)

  def show_ui_window(self):
    self.ui_window.element.show()

  def hide_ui_window(self):  
    self.ui_window.element.hide()
  
  def create_textbox(self):
    question_text = self.question
    self.question_textbox = Textbox(50, 40, 375, 150, question_text, self.manager, self.ui_window.element)
    self.question_textbox.text_effect_typing_appear()

  def show_question_textbox(self):
    self.question_textbox.element.show()
  
  def hide_question_textbox(self):
    self.question_textbox.element.hide()

  def create_buttons(self):
    answer_button_padding_left = 50
    answer_button_width = 375
    answer_button_height = 50

    self.answer_button_1 = Button(answer_button_padding_left, 205, answer_button_width, answer_button_height, self.answers[0], self.manager, self.ui_window.element)
    self.answer_button_2 = Button(answer_button_padding_left, 255, answer_button_width, answer_button_height, self.answers[1], self.manager, self.ui_window.element)
    self.answer_button_3 = Button(answer_button_padding_left, 305, answer_button_width, answer_button_height, self.answers[2], self.manager, self.ui_window.element)
    self.answer_button_4 = Button(answer_button_padding_left, 355, answer_button_width, answer_button_height, self.answers[3], self.manager, self.ui_window.element)

  def show_buttons(self):
    self.answer_button_1.element.show()
    self.answer_button_2.element.show()
    self.answer_button_3.element.show()
    self.answer_button_4.element.show()

  def hide_buttons(self):
    self.answer_button_1.element.hide()
    self.answer_button_2.element.hide()
    self.answer_button_3.element.hide()
    self.answer_button_4.element.hide()

  def hide_all(self):
    self.hide_ui_window()
    self.hide_question_textbox()
    self.hide_buttons()

  def show_all(self):
    self.show_ui_window()
    self.show_question_textbox()
    self.show_buttons()



  # def disable_all(self):
  #   self.

  #def enable_all

  #writes the buttons - accepts lists of answers in order and prints associated answers in order

  #update text_box to say correct and another for incorrect - doesn't need to check logic
  # correct below question text
  # correct in green
  # incorrect in red

  # write question - updates textbox to string fed in        
  # changing button colors based on              
          


