from positions.Player import Player


class Cornerback(Player):
    def __init__(self, first_name, last_name, pass_coverage, tackling, speed, agility, catching):
        super().__init__(first_name, last_name, "Cornerback")
        self.pass_coverage = pass_coverage
        self.tackling = tackling
        self.speed = speed
        self.agility = agility
        self.catching = catching

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position} - Speed: {self.speed}"

