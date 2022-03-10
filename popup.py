import pygame
import pygame_gui
import random
import pygame.mixer

pygame.mixer.init()
question_sound = pygame.mixer.Sound('./Sounds/MGSalertsound.mp3')
typing_sound = pygame.mixer.Sound('./Sounds/keyboard-typing.wav')
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
                        html_text=f'{html_text}',
                        manager=manager,
                        container=container)    

  def text_effect_typing_appear(self):
    self.element.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR, params = {'time_per_letter': .01})

class Anagram_Textbox():
  def __init__(self, manager, html_text):
    self.element = pygame_gui.elements.UITextBox(
                        relative_rect=pygame.Rect(206, 20, 258, 30),
                        html_text=f'<b>{html_text}</b>',
                        manager=manager) 
                  
  def fade_in(self):
    self.element.set_active_effect(pygame_gui.TEXT_EFFECT_FADE_IN)

  def text_effect_typing_appear(self):
    self.element.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR, params = {'time_per_letter': .02})

class Passcode_Entrybox():
  def __init__(self, manager, container):
    self.element = pygame_gui.elements.UITextEntryLine(
                        relative_rect=pygame.Rect(25, 25, 315, 50),
                        manager=manager,
                        container=container)

class Question_ui():
  def __init__(self, manager, win_width, win_height):
    self.manager = manager

    self.create_ui_window(win_width, win_height)
    self.create_textbox()
    self.create_buttons()
    self.hide_all()

  def create_ui_window(self, win_width, win_height):
    laptop_names = [
                    "alex-air @mac os",
                    "elliott-PC MSDos @home ",
                    "esther-PC HOME (win11)",
                    "haydn-mac personal - @macbook pro",
                    "kiran-mac(main) @home-air",
                    "saad-win95 PC-Desktop",]
    display_title = random.choice(laptop_names)

    ui_window_percentage_size = 0.75
    ui_window_padding = win_width * (1 - ui_window_percentage_size)
    self.ui_window = Window(ui_window_padding/2, ui_window_padding/2, win_width - ui_window_padding, win_height - ui_window_padding, display_title, self.manager)

  def show_ui_window(self):
    self.ui_window.element.show()

  def hide_ui_window(self):  
    self.ui_window.element.hide()
  
  def create_textbox(self):
    self.question_textbox = Textbox(50, 40, 375, 150, "Question Placeholder", self.manager, self.ui_window.element)

  def show_question_textbox(self):
    self.question_textbox.element.show()
  
  def hide_question_textbox(self):
    self.question_textbox.element.hide()

  def create_buttons(self):
    answer_button_padding_left = 50
    answer_button_width = 375
    answer_button_height = 50

    self.answer_button_1 = Button(answer_button_padding_left, 205, answer_button_width, answer_button_height, "Answer 1 Placeholder", self.manager, self.ui_window.element)
    self.answer_button_2 = Button(answer_button_padding_left, 255, answer_button_width, answer_button_height, "Answer 2 Placeholder", self.manager, self.ui_window.element)
    self.answer_button_3 = Button(answer_button_padding_left, 305, answer_button_width, answer_button_height, "Answer 3 Placeholder", self.manager, self.ui_window.element)
    self.answer_button_4 = Button(answer_button_padding_left, 355, answer_button_width, answer_button_height, "Answer 4 Placeholder", self.manager, self.ui_window.element)

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

  def load_question(self, question_info):
    self.question_info = question_info
    self.question_textbox.text_effect_typing_appear()
    question_sound.play()


    self.write_all()
    self.show_all()

    if question_info.answered == 'no':
      self.enable_all()
      print('enabling all')
    else:
      self.disable_all()
      print('disabling all')

  def answered_correctly(self):
    self.disable_all()
    self.question_info.question = (f'<font color=#03A062><b>{self.question_info.question}</font></b><br><br><font color=#FFFFFF><i>Correct!</font></i>')
    self.question_info.answered = "Correctly"
    self.rewrite_question()

  def answered_incorrectly(self):
    self.disable_all()
    self.question_info.question = (f'<font color=#03A062><b>{self.question_info.question}</font></b><br><br><font color=#FF0000><i>Wrong!</font></i><br><br>Correct answer: {self.question_info.correct_answer}')
    self.question_info.answered = "Incorrectly"
    self.rewrite_question()

  def disable_all(self):
    self.answer_button_1.element.disable()
    self.answer_button_2.element.disable()
    self.answer_button_3.element.disable()
    self.answer_button_4.element.disable()

  def enable_all(self):
    self.answer_button_1.element.enable()
    self.answer_button_2.element.enable()
    self.answer_button_3.element.enable()
    self.answer_button_4.element.enable()

  def write_buttons(self):
    self.answer_button_1.element.set_text(self.question_info.answers[0])
    self.answer_button_2.element.set_text(self.question_info.answers[1])
    self.answer_button_3.element.set_text(self.question_info.answers[2])
    self.answer_button_4.element.set_text(self.question_info.answers[3])

  def write_question(self):
    self.question_textbox.element.set_text(f'<font color=#03A062><b>{self.question_info.question}</b></font>')
  
  def rewrite_question(self):
    self.question_textbox.element.set_text(f'{self.question_info.question}')

  def write_all(self):
    self.write_buttons()
    self.write_question()
  
  def kill_all(self):
    self.ui_window.element.kill()
    self.question_textbox.element.kill()
    self.answer_button_1.element.kill()
    self.answer_button_2.element.kill()
    self.answer_button_3.element.kill()
    self.answer_button_4.element.kill()

class Passcode_ui():
  def __init__(self, manager, win_width, win_height, anagram, mode):
    self.manager = manager
    self.win_width = win_width
    self.win_height = win_height
    self.anagram = anagram
    self.mode = mode

    self.create_all()
    self.hide_all()

  def create_passcode_window(self):
    ui_window_percentage_size = 0.60
    ui_window_padding = self.win_width * (1 - ui_window_percentage_size)
    if self.mode == "easy":
      display_title = "Can you solve the word?"
    elif self.mode == "hard":
      display_title = "Can you solve the anagram?"
    

    self.passcode_window = Window(ui_window_padding/2, ui_window_padding/2, self.win_width - ui_window_padding, 160, display_title, self.manager)
    
  def create_passcode_entrybox(self):
    self.passcode_entrybox = Passcode_Entrybox(self.manager, self.passcode_window.element)

  def create_all(self):
    self.create_passcode_window()
    self.create_passcode_entrybox()

  def hide_all(self):
    self.passcode_window.element.hide()
    self.passcode_entrybox.element.hide()
  
  def show_all(self):
    self.passcode_window.element.show()
    self.passcode_entrybox.element.show()
   
class Intro_ui():
  def __init__(self, manager, win_width, win_height, mode):
    self.manager = manager
    self.win_width = win_width
    self.win_height = win_height
    self.mode = mode

    self.create_all()
    self.intro_textbox.text_effect_typing_appear()

  def create_intro_window(self):
    ui_window_percentage_size = 0.85
    ui_window_padding = self.win_width * (1 - ui_window_percentage_size)
    display_title = "Mission briefing"
    
    self.intro_window = Window(ui_window_padding/2, ui_window_padding/2, self.win_width - ui_window_padding, self.win_height - ui_window_padding, display_title, self.manager)
    
  def create_intro_textbox(self):
    text = f"Mode: {self.mode}<br><br><br>Agent, are you drunk again?<br><br><br>Careful you don't bump into walls, you may get disoriented.<br><br><br>Add more story here.<br><br><br>Press Spacebar to Continue..."
    self.intro_textbox = Textbox(20, 20, 500, 470, f'{text}', self.manager, self.intro_window.element)
    typing_sound.play()

  def create_all(self):
    self.create_intro_window()
    self.create_intro_textbox()

  def hide_all(self):
    self.intro_window.element.hide()
    self.intro_textbox.element.hide()

