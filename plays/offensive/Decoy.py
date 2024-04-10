import pygame

from formations.offensive.Shotgun import Shotgun
import random

from plays.offensive.Play import Play


class Decoy(Play):
    def __init__(self):
        super().__init__(Shotgun())
        self.set_player_routes()

    def set_player_routes(self):
        routes = [[(10, 5), (5, 0), (0, 80)], [(0, 10), (0, -2)], [(0, 10), (-20, 0)], [(0, 7), (-2, 2), (-10, 0)], [(0, 8), (-15, 0)], [(0, 80)]]
        player_routes = []
        i = 0
        for player in self.formation.get_player_positions():
            if player[0] in ['Running Back', 'Wide Receiver', 'Tight End']:
                player_routes.append([player, routes[i]])
                i += 1
            else:
                player_routes.append([player])
        self.routes = player_routes


# Example usage
if __name__ == "__main__":
    four_verticals = Decoy()
    four_verticals.visualize_play()