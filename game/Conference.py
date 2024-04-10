class Conference:
    def __init__(self, name):
        self.name = name
        self.divisions = []

    def add_division(self, division):
        self.divisions.append(division)

    def get_division(self, name):
        for division in self.divisions:
            if division.name == name:
                return division
