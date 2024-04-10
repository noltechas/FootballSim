from positions.Player import Player


class Linebacker(Player):
    def __init__(self, first_name, last_name, tackling, pass_coverage, run_stopping, speed, football_iq):
        super().__init__(first_name, last_name, 'Linebacker')
        self.tackling = tackling # Implemented
        self.pass_coverage = pass_coverage
        self.run_stopping = run_stopping
        self.speed = speed # Implemented
        self.football_iq = football_iq
