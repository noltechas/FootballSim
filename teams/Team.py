from teams.Field import Field


class Team:
    def __init__(self, name, field=None, logo=None):
        self.players = []
        self.name = name
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.color = (255, 255, 255)
        self.secondary_color = (255, 255, 255)
        self.field = field if field else Field()
        self.logo = logo
        self.division = None

    def add_player(self, player):
        self.players.append(player)

    def set_color(self, color):
        self.color = color

    def get_position(self, type, index=0):
        found = []
        for player in self.players:
            if player.position == type:
                found.append(player)
        return found[index]

    def get_players(self):
        return self.players

    def get_offensive_players(self):
        result = []
        for player in self.players:
            if player.position == "Quarterback" or player.position == "Wide Receiver" or player.position == "Running Back" or player.position == "Offensive Lineman" or player.position == "Tight End":
                result.append(player)
        return result

    def get_defensive_players(self):
        result = []
        for player in self.players:
            if player.position == "Defensive Tackle" or player.position == "Defensive End" or player.position == "Linebacker" or player.position == "Cornerback" or player.position == "Safety":
                result.append(player)
        return result
