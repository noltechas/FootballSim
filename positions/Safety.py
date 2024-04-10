from positions.Player import Player


class Safety(Player):
    def __init__(self, first_name, last_name, pass_coverage, tackling, speed, iq, catching):
        super().__init__(first_name, last_name, "Safety")
        self.pass_coverage = pass_coverage
        self.tackling = tackling
        self.speed = speed
        self.iq = iq
        self.catching = catching
