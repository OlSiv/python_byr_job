import string
import random


class Robot:
    def __init__(self):
        self.name = (''.join(random.choice(string.ascii_uppercase) for _ in range(
            2))) + (''.join(random.choice(string.digits) for _ in range(3)))

    def reset(self):
        while True:
            n_name = (''.join(random.choice(string.ascii_uppercase) for _ in range(
                2))) + (''.join(random.choice(string.digits) for _ in range(3)))
            if n_name != self.name:
                break
        self.name = n_name
