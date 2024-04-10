import pygame

from formations.offensive.Shotgun import Shotgun
import random

from plays.offensive.Play import Play


class QuickSlants(Play):
    def __init__(self):
        super().__init__(Shotgun())
        self.set_player_routes()

    def set_player_routes(self):
        routes = [[(15, 3), (0, 50)], [(2,3), (24,6)], [(-2,3), (-24, 6)], [(-1, 4), (16, 4)], [(1, 4), (-16, 4)], [(0, 0)]]
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
    play = QuickSlants()
    play.visualize_play()