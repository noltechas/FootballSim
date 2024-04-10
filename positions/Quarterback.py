import random

from positions.Player import Player


class Quarterback(Player):
    def __init__(self, first_name, last_name, passing_accuracy, arm_strength, field_vision, speed, leadership):
        super().__init__(first_name, last_name, "Quarterback")
        self.passing_accuracy = passing_accuracy
        self.arm_strength = arm_strength # Implemented
        self.field_vision = field_vision # Implemented
        self.speed = speed
        self.leadership = leadership
        self.number = random.randint(0, 11)
