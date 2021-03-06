import random
import pygame.mixer

from popup import *
from question_info import *
from anagram import *

endgame_sound = pygame.mixer.Sound('./Sounds/endgamemusic.mp3')
class Question():
  def __init__(self, manager, number, win_width, win_height, question_bank):
    self.number = number

    self.question_bank = question_bank
    self.question_info = question_bank.list[number]

class Questions():
  def __init__(self, popup, win_width, win_height, mode):
    self.popup = popup
    self.win_width = win_width
    self.win_height = win_height
    self.mode = mode

    question_bank = Question_bank()
    Question_setup(question_bank)
    self.setup_anagram()
    self.setup_intro()

    self.question_ui = Question_ui(popup.manager, win_width, win_height)
    self.q1 = Question(popup.manager, 1, win_width, win_height, question_bank)
    self.q2 = Question(popup.manager, 2, win_width, win_height, question_bank)
    self.q3 = Question(popup.manager, 3, win_width, win_height, question_bank)
    self.q4 = Question(popup.manager, 4, win_width, win_height, question_bank)
    self.q5 = Question(popup.manager, 5, win_width, win_height, question_bank)
    self.q6 = Question(popup.manager, 6, win_width, win_height, question_bank)

    self.question_textbox = self.question_ui.question_textbox.element
   
    self.answer_button_1 = self.question_ui.answer_button_1.element
    self.answer_button_2 = self.question_ui.answer_button_2.element
    self.answer_button_3 = self.question_ui.answer_button_3.element
    self.answer_button_4 = self.question_ui.answer_button_4.element

    self.answer_buttons = [self.answer_button_1, self.answer_button_2, self.answer_button_3, self.answer_button_4]
  
  def setup_intro(self):
    self.intro_ui = Intro_ui(self.popup.manager, self.win_width, self.win_height, self.mode)

  def setup_anagram(self):
    self.anagram = Anagram(self.mode)

    # Anagram
    self.anagram.select_anagram()
    self.anagram.randomise_anagram()
 
    # Anagram UI
    self.anagram_ui = Anagram_Textbox(self.popup.manager, f'<b><font color=#43FF33>{self.anagram.letters}</font></b>')

    # Passcode UI
    self.passcode_ui = Passcode_ui(self.popup.manager, self.win_width, self.win_height, self.anagram, self.mode)

  def load_question(self, question_info):
    self.question_ui.load_question(question_info)
    self.loaded_question_info = question_info

    self.question_textbox = self.question_ui.question_textbox.element
   
    self.answer_button_1 = self.question_ui.answer_button_1.element
    self.answer_button_2 = self.question_ui.answer_button_2.element
    self.answer_button_3 = self.question_ui.answer_button_3.element
    self.answer_button_4 = self.question_ui.answer_button_4.element

    self.answer_buttons = [self.answer_button_1, self.answer_button_2, self.answer_button_3, self.answer_button_4]

  def question_answered(self, status):
    if status == 'correctly':
      self.question_ui.answered_correctly()
      self.anagram.add_letter()
      self.print_anagram()
      self.anagram_ui.fade_in()
    elif status == 'incorrectly':
      self.question_ui.answered_incorrectly()
      self.anagram.add_qmark()
      self.print_anagram()

  def kill_and_recreate_question(self):
      self.question_ui.kill_all()
      self.question_ui = Question_ui(self.popup.manager, self.win_width, self.win_height)
  
  def print_anagram(self):
      self.anagram_ui.element.set_text(f'<b><font color=#0be01d>{self.anagram.letters}</font></b>')

  def load_passcode(self):
      self.passcode_ui.show_all()

  def anagram_correct(self):
      self.anagram_ui.element.set_text(f"<font color=#03A062><b>>>> CORRECT! You're Free! <<<</b></font>")
      self.anagram_ui.text_effect_typing_appear()
      self.passcode_ui.hide_all()
      pygame.mixer.music.stop()
      endgame_sound.play()
  
