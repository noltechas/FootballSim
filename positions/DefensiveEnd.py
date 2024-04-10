from positions.Player import Player


class DefensiveEnd(Player):
    def __init__(self, first_name, last_name, pass_rush, run_stopping, strength, tackling, speed):
        super().__init__(first_name, last_name, "Defensive End")
        self.pass_rush = pass_rush
        self.run_stopping = run_stopping
        self.strength = strength
        self.tackling = tackling
        self.speed = speed
