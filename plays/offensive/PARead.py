import pygame

from formations.offensive.Shotgun import Shotgun
import random

from plays.offensive.Play import Play


class PARead(Play):
    def __init__(self):
        super().__init__(Shotgun())
        self.set_player_routes()

    def set_player_routes(self):
        routes = [[(-1, 1), (-2, 1), (-7, 0)], [(2, 5), (6, 4), (5, 2), (5, 1), (18, 0), (-30, 4)], [(2, 10), (-2, 10), (2, 10)], [(0, 1)], [(6, 3), (4, 2), (6, 1), (2, 0), (5, 1), (5, 3), (0, 10)], [(0, 0)]]
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
    play = PARead()
    play.visualize_play()
