import random

class Anagram():
    def __init__(self):
      self.letters = []

    def select_anagram(self):
      anagrams = [
        'PYTHON',
        'MAKERS',
        'CODING',
        'METHOD',
        'CODERS',
        'COFFEE',
        'REVIEW',
        'OBJECT',
      ] 

      self.anagram = random.choice(anagrams)

    def randomise_anagram(self):
      self.list = self.anagram
      self.mixed_letters = list(self.list)
      random.shuffle(self.mixed_letters)

    def add_letter(self):
      letter = self.mixed_letters.pop(0)
      self.letters.append(letter)

    def add_qmark(self):
      self.letters.append('?')