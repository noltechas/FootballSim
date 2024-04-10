import pygame
import random
import math


# Base class for all plays
class Play:
    def __init__(self, formation):
        self.formation = formation
        self.routes = []
        self.window_size = (800, 600)  # This is an arbitrary window size

    def set_player_routes(self):
        raise NotImplementedError("This method should be implemented by subclasses.")

    def visualize_play(self):
        pygame.init()
        window_size = (800, 600)  # This is an arbitrary window size
        screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption("Play Visualization")
        clock = pygame.time.Clock()

        green = (0, 128, 0)
        white = (255, 255, 255)
        red = (255, 0, 0)

        x_scale = window_size[0] / 120
        y_scale = window_size[1] / 53.3

        # Center the formation horizontally on the screen
        formation_center_x = window_size[0] // 2

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill(green)

            # Draw the players and their routes
            for player_info in self.routes:
                player, routes = player_info[0], player_info[1] if len(player_info) > 1 else []

                # Player's initial position on the screen
                player_screen_x = formation_center_x + (player[1] * x_scale)
                player_screen_y = (window_size[1] / 2) - (player[2] * y_scale)  # Center vertically and adjust for position

                pygame.draw.circle(screen, white, (int(player_screen_x), int(player_screen_y)), 10)

                # Draw the route for each player from their position
                for route in routes:
                    next_x = player_screen_x + (route[0] * x_scale)
                    next_y = player_screen_y - (route[1] * y_scale)
                    # Draw the route line
                    pygame.draw.line(screen, red, (int(player_screen_x), int(player_screen_y)), (int(next_x), int(next_y)), 3)

                    if routes.index(route) == len(routes)-1:
                        # Draw the arrow at the end of the route
                        self.draw_arrow(screen, red, (int(player_screen_x), int(player_screen_y)), (int(next_x), int(next_y)))

                    # Update the initial position for the next segment of the route
                    player_screen_x, player_screen_y = next_x, next_y

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()

    def draw_play(self, screen, formation_center_x, x_scale, y_scale, route_color, player_color):
        for player_info in self.routes:
            player, route = player_info
            initial_x, initial_y = self.convert_to_screen(player[1], player[2], x_scale, y_scale)
            pygame.draw.circle(screen, player_color, (int(initial_x), int(initial_y)), 10)

            if route:
                for point in route:
                    dest_x, dest_y = self.convert_to_screen(point[0], point[1], x_scale, y_scale)
                    pygame.draw.line(screen, route_color, (int(initial_x), int(initial_y)), (int(dest_x), int(dest_y)), 3)
                    self.draw_arrow(screen, route_color, (int(initial_x), int(initial_y)), (int(dest_x), int(dest_y)))
                    initial_x, initial_y = dest_x, dest_y

    def convert_to_screen(self, x, y, x_scale, y_scale):
        # Adjust the coordinates for the center of the field
        screen_x = (50 + x) * x_scale
        screen_y = (26.65 - y) * y_scale  # Subtract y because the screen coordinates increase downwards

        return screen_x, screen_y

    @classmethod
    def draw_arrow(self, screen, color, start, end, width=3):
        pygame.draw.line(screen, color, start, end, width)
        rotation = math.degrees(math.atan2(start[1]-end[1], end[0]-start[0])) + 90
        pygame.draw.polygon(screen, color, (
            (end[0] + 12 * math.sin(math.radians(rotation)), end[1] + 12 * math.cos(math.radians(rotation))),
            (end[0] + 12 * math.sin(math.radians(rotation - 120)), end[1] + 12 * math.cos(math.radians(rotation - 120))),
            (end[0] + 12 * math.sin(math.radians(rotation + 120)), end[1] + 12 * math.cos(math.radians(rotation + 120)))
        ))