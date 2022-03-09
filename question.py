from popup import *
from question_info import *
from anagram import *

class Question():
  def __init__(self, manager, number, win_width, win_height, question_bank):
    self.number = number

    self.question_bank = question_bank
    self.question_info = question_bank.list[number]

class Questions():
  def __init__(self, popup, win_width, win_height):
    question_bank = Question_bank()
    Question_setup(question_bank)

    self.anagram = Anagram()
    self.anagram.select_anagram()
    self.anagram.randomise_anagram()

    self.anagram_ui = Anagram_Textbox(popup.manager, self.anagram.letters)

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

  def load_question(self, question_info):
    self.question_ui.load_question(question_info)
    self.loaded_question_info = question_info

  def question_answered(self, status):
    if status == 'correctly':
      self.question_ui.answered_correctly()
      self.anagram.add_letter()
      self.anagram_ui.element.set_text(f'{self.anagram.letters}')
    elif status == 'incorrectly':
      self.question_ui.answered_incorrectly()
      self.anagram.add_qmark()
      self.anagram_ui.element.set_text(f'{self.anagram.letters}')