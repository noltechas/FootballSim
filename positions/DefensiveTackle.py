from positions.Player import Player


class DefensiveTackle(Player):
    def __init__(self, first_name, last_name, pass_rush, run_stopping, strength, tackling, speed):
        super().__init__(first_name, last_name, "Defensive Tackle")
        self.pass_rush = pass_rush # Implemented
        self.run_stopping = run_stopping
        self.strength = strength # Implemented
        self.tackling = tackling
        self.speed = speed
