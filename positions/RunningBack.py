from positions.Player import Player


class RunningBack(Player):
    def __init__(self, first_name, last_name, speed, agility, blocking, catching, route_running):
        super().__init__(first_name, last_name, "Running Back")
        self.speed = speed
        self.agility = agility
        self.blocking = blocking
        self.catching = catching
        self.route_running = route_running
