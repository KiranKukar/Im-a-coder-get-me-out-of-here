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
      'question' : "Using Python, how would you print the string: 'Hello World'?",
      'correct_answer' : "print('Hello World')",
      'incorrect_answers' : ["print(Hello world)","print{'Hello World'}","print'{Hello World}'"]
    }
    q2 = {
      'question' : 'Using Python, what does // mean?',
      'correct_answer' : 'Floor division',
      'incorrect_answers' : ['Next line', 'Railroad Ahead', 'Divide twice']
    }
    q3 = {
      'question' : 'Using Python, what does the following code output:<br><br>fingers = 5<br># print(fingers)',
      'correct_answer' : 'Nothing',
      'incorrect_answers' : ['An error', '5', 'hand']
    }
    q4 = {
      'question' : 'Why is correct indentation so fundamental in Python?',
      'correct_answer' : 'defines a block of code',
      'incorrect_answers' : ['keeps code readable', 'can be used instead of a line break', 'all good code should look like a staircase']
    }
    q5 = {
      'question' : "Using Python, what does the following code output:<br><br>names = ['tam', 'tim']<br>name = 'tom'<br>print(names.append(name))",
      'correct_answer' : 'none',
      'incorrect_answers' : ['tom', "['tam', 'tim', 'tom']", "['tom', 'tam', 'tim']"]
    }
    q6 = {
      'question' : 'Ruby is to hash as Python is to?',
      'correct_answer' : 'Dictionary',
      'incorrect_answers' : ['Library', 'Reference_Table', 'kif']
    }
    q7 = {
      'question' : 'Using Python, what is a tuple?',
      'correct_answer' : 'An immutable list',
      'incorrect_answers' : ['A list limited to 2 or 3 objects', 'A mutable set', 'tuples are found in JS, not Python']
    }
    q8 = {
      'question' : 'Which of the following is the correct extension of a Python file?',
      'correct_answer' : '.py',
      'incorrect_answers' : ['.python', '.p', '.pn']
    }
    q9 = {
      'question' : 'What will be the value of the following Python expression?<br><br><br>4 + 3 % 5',
      'correct_answer' : '7',
      'incorrect_answers' : ['2', '4', '1']
    }
    q10 = {
      'question' : 'Which keyword  is used for function in Python language?',
      'correct_answer' : 'Def',
      'incorrect_answers' : ['Define', 'define', 'Function']
    }

    questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    random.shuffle(questions)

    self.load_questions(questions)

  def load_questions(self, questions):
    for value in questions:
      (self.question_bank.list).append(Question_info(value['question'], value['correct_answer'], value['incorrect_answers']))







    