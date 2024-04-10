import pygame

from formations.offensive.Shotgun import Shotgun
import random

from plays.offensive.Play import Play


class Out(Play):
    def __init__(self):
        super().__init__(Shotgun())
        self.set_player_routes()

    def set_player_routes(self):
        routes = [[(5, 0), (5, 1), (5, 3), (2, 4), (0, 5), (-30, 0)], [(-3,0),(-2,2)], [(0,30)], [(0,10),(6,4), (0, 20)], [(0, 5), (-5, 0)], [(0, 0)]]
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
    play = Out()
    play.visualize_play()
