from positions.Player import Player


class TightEnd(Player):
    def __init__(self, first_name, last_name, blocking, catching, route_running, speed, agility):
        super().__init__(first_name, last_name, "Tight End")
        self.blocking = blocking
        self.catching = catching
        self.route_running = route_running
        self.speed = speed
        self.agility = agility
