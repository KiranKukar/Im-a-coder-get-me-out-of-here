import random

class Question_bank():
  def __init__(self):
    self.list = []

class Question_info():
  def __init__(self, question, correct_answer, incorrect_answers):
    self.answered = 'no'
    self.question = question
    self.correct_answer = correct_answer
    self.incorrect_answers = incorrect_answers
    self.shuffle_answers()

  def shuffle_answers(self):
    list = self.incorrect_answers
    list.append(self.correct_answer)
    random.shuffle(list)
    self.answers = list

class Question_setup():
  def __init__(self, question_bank):
    self.question_bank = question_bank

    q1 = {
      'question' : 'Which number is largest?',
      'correct_answer' : '4',
      'incorrect_answers' : ['1', '2', '3']
    }
    q2 = {
      'question' : 'Which letter is a vowel?',
      'correct_answer' : 'A',
      'incorrect_answers' : ['B', 'C', 'D']
    }
    q3 = {
      'question' : 'Which number is largest?',
      'correct_answer' : '40',
      'incorrect_answers' : ['10', '20', '30']
    }
    q4 = {
      'question' : 'Which number is smallest?',
      'correct_answer' : '-4',
      'incorrect_answers' : ['-1', '-2', '-3']
    }
    q5 = {
      'question' : 'Which letter is a vowel?',
      'correct_answer' : 'E',
      'incorrect_answers' : ['F', 'G', 'H']
    }
    q6 = {
      'question' : 'Which number is largest?',
      'correct_answer' : '1000',
      'incorrect_answers' : ['750', '500', '250']
    }
    q7 = {
      'question' : 'Which planet is largest?',
      'correct_answer' : 'Jupiter',
      'incorrect_answers' : ['Saturn', 'Neptune', 'Uranus']
    }
    q8 = {
      'question' : 'Which ocean is largest?',
      'correct_answer' : 'Pacific',
      'incorrect_answers' : ['Indian', 'Atlantic', 'Southern']
    }
    q9 = {
      'question' : 'Which country is largest by area?',
      'correct_answer' : 'Russia',
      'incorrect_answers' : ['Canada', 'China', 'Australia']
    }
    q10 = {
      'question' : 'Which desert is largest?',
      'correct_answer' : 'Antarctica',
      'incorrect_answers' : ['Kalahari', 'Gobi', 'Sahara']
    }

    questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    random.shuffle(questions)

    self.load_questions(questions)

  def load_questions(self, questions):
    for value in questions:
      (self.question_bank.list).append(Question_info(value['question'], value['correct_answer'], value['incorrect_answers']))







    