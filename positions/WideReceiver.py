from positions.Player import Player


class WideReceiver(Player):
    def __init__(self, first_name, last_name, route_running, catching, speed, agility, blocking):
        super().__init__(first_name, last_name, "Wide Receiver")
        self.route_running = route_running # Implementedd
        self.catching = catching # Implemented
        self.speed = speed # Implemented
        self.agility = agility # Implemented
        self.blocking = blocking

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position} - Speed: {self.speed}"

