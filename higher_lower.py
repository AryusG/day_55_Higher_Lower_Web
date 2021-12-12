import random

class HigherLower():
    def __init__(self):
        self.answer = random.randint(0, 9)

    def get_new_answer(self):
        self.answer = random.randint(0, 9)
