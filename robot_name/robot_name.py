import string
import random


class Robot:
    
    def __init__(self):
        self.name = self.gener()

    def reset(self):
        while True:
            n_name = self.gener()
            if n_name != self.name:
                break
        self.name = n_name

    def gener(self):
        result = ''
        for _ in range (2):
            result += random.choice(string.ascii_uppercase)
        for _ in range (3):
            result += random.choice(string.digits)
        return result 
    