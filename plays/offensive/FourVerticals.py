import pygame

from formations.offensive.Shotgun import Shotgun
import random

from plays.offensive.Play import Play


class FourVerticals(Play):
    def __init__(self):
        super().__init__(Shotgun())
        self.set_player_routes()

    def set_player_routes(self):
        routes = [[(9, 5), (0, 60)], [(0, 80)], [(0, 80)], [(0, 80)], [(0, 8), (16, 8), (-30, 0)], [(0, 80)]]
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
    four_verticals = FourVerticals()
    four_verticals.visualize_play()