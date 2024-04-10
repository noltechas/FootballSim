import random


class Player:
    def __init__(self, first_name, last_name, position, number=-1):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.number = number
        if number == -1:
            self.number = random.randint(0, 99)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"
