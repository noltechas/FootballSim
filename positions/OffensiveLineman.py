from positions.Player import Player


class OffensiveLineman(Player):
    def __init__(self, first_name, last_name, blocking_power, blocking_technique, strength, speed, football_iq):
        super().__init__(first_name, last_name, "Offensive Lineman")
        self.blocking_power = blocking_power # Implemented
        self.blocking_technique = blocking_technique # Implemented
        self.strength = strength
        self.speed = speed
        self.football_iq = football_iq
