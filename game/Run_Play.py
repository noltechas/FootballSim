import pygame
import random
import time
import math

from formations.offensive.Shotgun import Shotgun
from game.game_state import game_state
from plays.offensive.FourVerticals import FourVerticals

from formations.defensive.FourThree import FourThree


class Run_Play:
    def __init__(self, game_state, simulated_game=False):
        self.window_size = (1200, 533)  # Example window size
        self.offensive_formation = game_state.offensive_formation  # Create an instance of the formation
        self.defensive_formation = game_state.defensive_formation  # Create an instance of the formation
        self.line_of_scrimmage_yard = game_state.line_of_scrimmage_yard
        self.first_down_yard = game_state.first_down_yard
        self.ball_position = game_state.ball_position
        self.down = game_state.down
        self.home_score = game_state.home_score
        self.away_score = game_state.away_score
        self.has_ball = game_state.has_ball
        self.time_remaining = game_state.time_remaining
        self.home_team = game_state.home_team
        self.away_team = game_state.away_team
        self.players = []
        self.ball_position_x = self.line_of_scrimmage_yard * self.window_size[0] / 120
        self.ball_position_y = self.window_size[1] / 2
        self.throw_time = None
        self.target_receiver = None
        self.ball_in_air = False
        self.ball_target_x = None
        self.ball_target_y = None
        self.ball_caught = False
        self.play_active = True
        self.first_down_achieved = False
        self.possession_over = False
        self.target_coordinates = None
        self.predicted_positions = None
        self.intercepted = False
        self.start_ball_x = 0
        self.start_ball_y = 0
        self.ball_speed = 175
        self.sacked = False
        self.sack_position = 0
        self.overtime = game_state.overtime
        self.overtime_possessions = 0
        self.simulated_game = simulated_game

        print(f"Starting a new play. {self.down} and {self.line_of_scrimmage_yard - self.first_down_yard}")

        if not self.simulated_game:
        # Initialize Pygame
            pygame.init()
            self.screen = pygame.display.set_mode(self.window_size, pygame.DOUBLEBUF)
            pygame.display.set_caption("Football Play Simulation")
            self.font = pygame.font.Font(None, 50)  # Initialize font
            # Create a surface for the field
            self.field_surface = pygame.Surface(self.window_size)
            self.draw_field(self.field_surface)  # Draw the field on this surface

    def get_qb_strength(self):
        for player in self.players:
            if player['player_object'].position == 'Quarterback':
                return player['player_object'].arm_strength * 2.5

    def draw_arrow(self, screen, color, start, end, width=3):
        pygame.draw.line(screen, color, start, end, width)
        rotation = math.degrees(math.atan2(start[1] - end[1], end[0] - start[0])) + 90
        pygame.draw.polygon(screen, color, (
            (end[0] + 12 * math.sin(math.radians(rotation)), end[1] + 12 * math.cos(math.radians(rotation))),
            (
            end[0] + 12 * math.sin(math.radians(rotation - 120)), end[1] + 12 * math.cos(math.radians(rotation - 120))),
            (end[0] + 12 * math.sin(math.radians(rotation + 120)), end[1] + 12 * math.cos(math.radians(rotation + 120)))
        ))

    def draw_target(self, x, y):
        TARGET_COLOR = (255, 0, 0)  # Red color for the target
        TARGET_RADIUS = 10
        TARGET_LINE_WIDTH = 3
        LINE_LENGTH = TARGET_RADIUS // 2

        # Draw a circle as the target
        pygame.draw.circle(self.screen, TARGET_COLOR, (int(x), int(y)), TARGET_RADIUS, TARGET_LINE_WIDTH)

        # Coordinates for the center of the target
        center_x, center_y = int(x), int(y)

        # Draw small lines on the top, bottom, left, and right of the circle
        # Top line
        pygame.draw.line(self.screen, TARGET_COLOR, (center_x, center_y - TARGET_RADIUS),
                         (center_x, center_y - TARGET_RADIUS - LINE_LENGTH - 1), TARGET_LINE_WIDTH)

        # Bottom line
        pygame.draw.line(self.screen, TARGET_COLOR, (center_x, center_y + TARGET_RADIUS),
                         (center_x, center_y + TARGET_RADIUS + LINE_LENGTH), TARGET_LINE_WIDTH)

        # Left line
        pygame.draw.line(self.screen, TARGET_COLOR, (center_x - TARGET_RADIUS, center_y),
                         (center_x - 1 - TARGET_RADIUS - LINE_LENGTH, center_y), TARGET_LINE_WIDTH)

        # Right line
        pygame.draw.line(self.screen, TARGET_COLOR, (center_x + TARGET_RADIUS, center_y),
                         (center_x + TARGET_RADIUS + LINE_LENGTH, center_y), TARGET_LINE_WIDTH)

    def add_player(self, player_type, x, y, route=None):
        player_info = {
            'player_object': None,
            'type': player_type,
            'x': x,
            'y': y + self.ball_position,
            'route': route,
            'route_index': 0,
            'is_active': True,  # New attribute to track if player is active
            'original_color': self.get_player_color(player_type)  # Store original color
        }
        self.players.append(player_info)

    def place_players(self, play=None):
        # Clear existing players
        self.players.clear()

        # Calculate the line of scrimmage position on the screen
        x_scale = self.window_size[0] / 120
        y_scale = self.window_size[1] / 53.3
        line_of_scrimmage = (self.line_of_scrimmage_yard * x_scale)  # Center on the field width

        if play:  # Only if a play is provided (for offensive players)
            for player_info in play.routes:
                player, route = player_info[0], player_info[1] if len(player_info) > 1 else None
                rel_x, rel_y = player[1], player[2]
                screen_route = self.convert_route_to_screen({'x': rel_x, 'y': rel_y, 'route': route}, x_scale,
                                                            y_scale) if route else None
                self.add_player(player[0], line_of_scrimmage - (rel_y * y_scale),
                                (self.window_size[1] / 2) + (rel_x * x_scale), screen_route)
        # Place defensive players based on the line of scrimmage
        # You need to add defensive formation logic here similar to your original code
        # For example:
        if self.defensive_formation:
            self.defensive_formation.set_player_positions()
            for position, rel_x, rel_y in self.defensive_formation.player_positions:
                # Adjust positions to rotate formation 90 degrees
                self.add_player(position, line_of_scrimmage - (rel_y * y_scale),
                                (self.window_size[1] / 2) + (rel_x * x_scale))

    def get_player_color(self, position):
        color_map = {
            'Quarterback': (255, 0, 0),  # Red
            'Running Back': (0, 255, 0),  # Green
            'Wide Receiver': (0, 0, 255),  # Blue
            'Tight End': (255, 20, 147),  # Pink
            'Offensive Lineman': (255, 215, 0),  # Gold
            'Defensive End': (100, 100, 100),  # Gray
            'Defensive Tackle': (140, 140, 140),  # Gray
            'Linebacker': (128, 0, 128),  # Purple
            'Cornerback': (75, 0, 130),  # Indigo
            'Safety': (82, 45, 161)  # Indigo
        }
        return color_map.get(position, (128, 128, 0))  # Default color

    def draw_scoreboard(self):
        # Scoreboard dimensions and position
        scoreboard_width = 200  # Adjust as needed
        scoreboard_height = 50  # Adjust as needed
        scoreboard_x = ((self.window_size[0] - scoreboard_width) // 2) + 1
        scoreboard_y = 45  # 10 pixels from the top

        # Scoreboard background color
        scoreboard_color = (50, 50, 50)  # Dark gray background

        # Draw the scoreboard rectangle
        pygame.draw.rect(self.screen, scoreboard_color,
                         (scoreboard_x, scoreboard_y, scoreboard_width, scoreboard_height))

        # Set font for the scoreboard
        font_size = 20  # Adjust size as needed
        font = pygame.font.Font(None, font_size)

        # Render the text for home and away team scores
        home_score_text = font.render(f"Home: {self.home_score}", True, self.home_team.color)  # White text
        away_score_text = font.render(f"Away: {self.away_score}", True, self.away_team.color)

        # Render the text for time remaining
        time_text = font.render(f"Time: {self.time_remaining}", True, (255, 255, 255))
        if self.overtime:
            time_text = font.render(f"OT", True, (255, 255, 255))

        # Calculate positions to center the text within the scoreboard
        home_score_x = scoreboard_x + 10  # 10 pixels padding
        away_score_x = scoreboard_x + scoreboard_width - away_score_text.get_width() - 10
        time_x = scoreboard_x + (scoreboard_width - time_text.get_width()) // 2
        text_y = scoreboard_y + (scoreboard_height - home_score_text.get_height()) // 2

        # Draw the text on the scoreboard
        self.screen.blit(home_score_text, (home_score_x, text_y))
        self.screen.blit(away_score_text, (away_score_x, text_y))
        self.screen.blit(time_text, (time_x, text_y))

    def draw_players(self):
        font = pygame.font.Font(None, 20)  # Adjust as needed

        for player in self.players:
            player_color = player['original_color'] if player['is_active'] else (self.home_team.field.field_color_2)  # Grey out if inactive
            outline_color = (255,255,255)
            if player['player_object'] in self.home_team.get_players():
                outline_color = self.home_team.color

            player_x = int(player['x'])
            player_y = int(player['y'])

            # Draw player with outline (slightly larger circle behind the colored circle)
            pygame.draw.circle(self.screen, outline_color, (player_x, player_y), 12)
            pygame.draw.circle(self.screen, player_color, (player_x, player_y), 10)

            # Render the player's number as text
            player_number = str(player['player_object'].number) if player['player_object'] else '0'
            color = self.away_team.secondary_color
            if player['player_object'] in self.home_team.get_players():
                color = self.home_team.secondary_color

            text = font.render(player_number, True, color)  # White color for the number

            # Center the text on the player's circle
            text_x = player_x - text.get_width() // 2
            text_y = player_y - text.get_height() // 2

            # Draw the text
            self.screen.blit(text, (text_x, text_y))

    def draw_football(self):
        FOOTBALL_COLOR = (139, 69, 19)  # Brown color for the football
        original_football_size = (17, 10)  # Width and height for the football ellipse

        if self.ball_target_x is not None and self.ball_target_y is not None:
            # Calculate total distance from the start to the target
            total_distance = math.hypot(self.ball_target_x - self.start_ball_x, self.ball_target_y - self.start_ball_y)

            # Define thresholds for short, medium, and long passes (these values can be adjusted)
            short_pass_threshold = 100  # Example value
            long_pass_threshold = 300  # Example value

            # Determine maximum scale factor based on pass length
            if total_distance <= short_pass_threshold:
                max_scale_factor = 1.2  # Small growth for short passes
            elif total_distance <= long_pass_threshold:
                # Gradually increase scale factor for medium passes
                max_scale_factor = 1.2 + (total_distance - short_pass_threshold) / (
                            long_pass_threshold - short_pass_threshold) * 0.8
            else:
                max_scale_factor = 2.0  # Maximum growth for long passes

            # Calculate current distance from the start to the current position
            current_distance = math.hypot(self.ball_position_x - self.start_ball_x,
                                          self.ball_position_y - self.start_ball_y)

            # Calculate progress along the route (0 to 1)
            progress = min(current_distance / total_distance, 1) if total_distance != 0 else 0

            # Determine the scale factor based on progress and maximum scale factor
            scale_factor = 1.0 + (max_scale_factor - 1.0) * (1.0 - abs(progress - 0.5) * 2)
        else:
            # If target coordinates are not set, use original size
            scale_factor = 1.0

        # Adjust football size based on scale factor
        football_width = int(original_football_size[0] * scale_factor)
        football_height = int(original_football_size[1] * scale_factor)

        # Use the updated ball positions and scaled size
        ball_x = int(self.ball_position_x - football_width // 2)
        ball_y = int(self.ball_position_y - football_height // 2)

        # Draw the football as an ellipse with the new size
        pygame.draw.ellipse(self.screen, FOOTBALL_COLOR, (ball_x, ball_y, football_width, football_height))

    def draw_field(self, surface):
        GREEN = (0, 128, 0)
        WHITE = (255, 255, 255)
        OFFENSIVE_ENDZONE_COLOR = self.home_team.color
        if self.home_team.name == 'Oakland Hogs':
            OFFENSIVE_ENDZONE_COLOR = (48, 21, 0)
        LINE_OF_SCRIMMAGE_COLOR = (128, 128, 128)  # Red line of scrimmage
        FIRST_DOWN_COLOR = (255, 255, 0)

        # Load the fonts from the team's field
        yard_number_font = pygame.font.Font(self.home_team.field.yard_number_font_path, self.home_team.field.yard_number_font_size)

        x_scale = self.window_size[0] / 120  # Length of the field including end zones
        y_scale = self.window_size[1] / 53.3  # Width of the field

        # Define hash mark offset
        hash_mark_x_offset = 18.5 * y_scale  # Hash marks are 18.5 yards from each sideline

        # Fill the field with alternating colors every 10 yards
        if not self.home_team.field.symmetrical:
            for i in range(0, 120, 10):
                field_color = self.home_team.field.field_color_1 if i // 10 % 2 == 0 else self.home_team.field.field_color_2
                pygame.draw.rect(surface, field_color, (i * x_scale, 0, 10 * x_scale, self.window_size[1]))
        else:
            for i in range(0, 120, 10):
                # Adjust the index for symmetry around the 50-yard line
                adjusted_index = i // 10 if i <= 50 else 11 - (i // 10)

                # Determine the field color based on the adjusted index
                field_color = self.home_team.field.field_color_1 if adjusted_index % 2 == 0 else self.home_team.field.field_color_2

                # Draw the rectangle for this segment
                pygame.draw.rect(surface, field_color, (i * x_scale, 0, 10 * x_scale, self.window_size[1]))


        # Draw end zones
        pygame.draw.rect(surface, OFFENSIVE_ENDZONE_COLOR, (0, 0, 10 * x_scale, self.window_size[1]))
        pygame.draw.rect(surface, OFFENSIVE_ENDZONE_COLOR, (110 * x_scale, 0, 10 * x_scale, self.window_size[1]))

        # Draw hash marks
        for i in range(11, 110):
            x_pos = i * x_scale
            if 10 < i < 110:  # Only draw between the 10-yard markers
                # Top hash marks
                pygame.draw.line(surface, WHITE, (x_pos, hash_mark_x_offset), (x_pos, hash_mark_x_offset + 4), 2)
                # Bottom hash marks
                pygame.draw.line(surface, WHITE, (x_pos, self.window_size[1] - hash_mark_x_offset),
                                 (x_pos, self.window_size[1] - hash_mark_x_offset - 4), 2)

        # Draw yard lines and numbers
        for i in range(1, 110):
            x_pos = i * x_scale
            if i % 10 == 0 and 10 < i < 110:  # Only draw at every 10 yards and not in the end zones
                # Draw yard line
                pygame.draw.line(surface, WHITE, (x_pos, 0), (x_pos, self.window_size[1]), 2)

                # Draw yard numbers
                number = i // 10 if i <= 60 else 12 - (i // 10)
                if number != 0:  # Skip the 0 at the 50-yard line
                    if self.home_team.field.yard_numbers_spaced:
                        text = yard_number_font.render(f'{str((number - 1) * 10)[0]} {str((number - 1) * 10)[1]}', True, self.home_team.field.yard_number_color)
                    else:
                        text = yard_number_font.render(f'{str((number - 1) * 10)[0]}{str((number - 1) * 10)[1]}', True, self.home_team.field.yard_number_color)
                    # Numbers for top side
                    surface.blit(text, (x_pos - text.get_width() // 2 + 1, 10))
                    # Numbers for bottom side, flipped
                    text_flipped = pygame.transform.flip(text, True, True)
                    surface.blit(text_flipped,
                                 (x_pos - text.get_width() // 2, self.window_size[1] - text.get_height() - 10))

        # Load the team's logo
        logo_path = self.home_team.logo  # Adjust the path as necessary
        logo_image = pygame.image.load(logo_path)

        division_logo_path = self.home_team.division.logo_path  # Adjust the path as necessary
        division_logo_image = pygame.image.load(division_logo_path)
        division_logo_image = pygame.transform.scale(division_logo_image, (80, 80))
        # Calculate the center of the field
        center_x = (self.window_size[0] // 2)
        center_y = self.window_size[1] // 2

        # Calculate the top-left position to draw the logo
        division_logo_position = ((center_x+250) - 80 // 2, (center_y+150) - 80 // 2)
        surface.blit(division_logo_image, division_logo_position)

        division_logo_position = ((center_x-250) - 80 // 2, (center_y-150) - 80 // 2)
        surface.blit(division_logo_image, division_logo_position)

        # Resize the logo to a standard size (e.g., 50x50 pixels)
        logo_size = (self.home_team.field.midfield_logo_size, self.home_team.field.midfield_logo_size)
        logo_image = pygame.transform.scale(logo_image, logo_size)

        if self.home_team.name == 'Empire State Terrors':
            center_x += 3

        # Calculate the top-left position to draw the logo
        logo_position = (center_x - logo_size[0] // 2, center_y - logo_size[1] // 2)

        # Draw the logo on the field
        surface.blit(logo_image, logo_position)

        # Draw the line of scrimmage
        line_of_scrimmage_x = self.line_of_scrimmage_yard * x_scale
        pygame.draw.line(surface, LINE_OF_SCRIMMAGE_COLOR, (line_of_scrimmage_x, 0),
                         (line_of_scrimmage_x, self.window_size[1]), 3)

        # Draw first down line
        first_down_x = self.first_down_yard * x_scale
        pygame.draw.line(surface, FIRST_DOWN_COLOR, (first_down_x, 0), (first_down_x, self.window_size[1]), 3)

        # Draw Down and Distance Text
        # Define text color and font size
        text_color = (128, 128, 128)
        font_size = 30
        font = pygame.font.Font(None, font_size)

        # Calculate yards to go for a first down
        yards_to_go = abs(self.first_down_yard - self.line_of_scrimmage_yard)
        down_text = '4th'
        if self.down == 1:
            down_text = '1st'
        elif self.down == 2:
            down_text = '2nd'
        elif self.down == 3:
            down_text = '3rd'

        # Determine the text based on the distance
        if yards_to_go < 1:
            down_and_distance_text = f"{down_text} and Inches"
        elif self.first_down_yard <= 10.5:
            down_and_distance_text = f'{down_text} and Goal'
        else:
            rounded_yards_to_go = round(yards_to_go)
            down_and_distance_text = f"{down_text} and {rounded_yards_to_go}"

        # Render the text
        text = font.render(down_and_distance_text, True, text_color)

        # Calculate the x-coordinate of the line of scrimmage on the screen
        line_of_scrimmage_x = self.line_of_scrimmage_yard * x_scale

        # Offset to the right of the line of scrimmage
        offset_x = 20  # 20 pixels to the right

        # Position for the text
        text_x = min(line_of_scrimmage_x + offset_x, self.window_size[0] - text.get_width())
        text_y = 150  # Y position for the text

        # Blit the text onto the surface
        surface.blit(text, (text_x, text_y))

        self.draw_team_name_in_endzone(surface, (0, 0, 10 * x_scale, self.window_size[1]),
                                       self.home_team.secondary_color)
        self.draw_team_name_in_endzone(surface,
                                       (110 * x_scale, 0, 10 * x_scale, self.window_size[1]),
                                       self.home_team.secondary_color, 'Away')

    def draw_team_name_in_endzone(self, surface, rect, text_color, orientation='Home'):
        font = pygame.font.Font(self.home_team.field.endzone_font_path, self.home_team.field.endzone_font_size)
        if(self.home_team.name != 'Oakland Hogs'):
            text = font.render(self.home_team.field.endzone_1_text, True, text_color)
        else:
            text = font.render(self.home_team.field.endzone_1_text, True, (82, 37, 2))
        offset = self.home_team.field.endzone_text_offset
        if orientation == 'Home':
            offset *= -1
        text_rect = text.get_rect(center=((rect[0] + rect[2] / 2) + offset, rect[1] + rect[3] / 2))

        if orientation == 'Away':
            text = pygame.transform.rotate(text, 270)
            text_rect = text.get_rect(center=text_rect.center)
        else:
            if(self.home_team.name != 'Oakland Hogs'):
                text = font.render(self.home_team.field.endzone_2_text, True, text_color)
            else:
                text = font.render(self.home_team.field.endzone_2_text, True, (82, 37, 2))
            text = pygame.transform.rotate(text, 90)
            text_rect = text.get_rect(center=text_rect.center)

        surface.blit(text, text_rect)

    def interpolate(self, start, end, step):
        """Linearly interpolate between two points."""
        x_diff = end[0] - start[0]
        y_diff = end[1] - start[1]
        distance = math.sqrt(x_diff ** 2 + y_diff ** 2)
        if distance == 0:
            return start
        else:
            return (start[0] + (x_diff / distance) * step,
                    start[1] + (y_diff / distance) * step)

    def move_player(self, player, delta_time):
        if player['route'] is None or player['route_index'] >= len(player['route']) or self.ball_caught:
            return  # Skip if no route or route is complete

        speed = 50  # Adjust the speed as necessary
        if player['player_object'].speed is not None:
            speed = player['player_object'].speed
            if player['type'] == 'Offensive Lineman':
                speed *= 0.8
        distance_to_move = speed * delta_time

        while distance_to_move > 0:
            current_point = (player['x'], player['y'])
            next_point = player['route'][player['route_index']]

            proposed_x, proposed_y = self.interpolate(current_point, next_point, distance_to_move)
            remaining_distance = math.hypot(next_point[0] - proposed_x, next_point[1] - proposed_y)

            # Ensure the player stays within the boundaries of the field
            proposed_x = max(5, min(proposed_x, self.window_size[0]))
            proposed_y = max(10, min(proposed_y, self.window_size[1]))

            # Update player's position
            player['x'], player['y'] = proposed_x, proposed_y

            if remaining_distance <= distance_to_move:
                player['route_index'] += 1
                if player['route_index'] >= len(player['route']):
                    break  # Stop if the end of the route is reached
                distance_to_move -= remaining_distance
                next_point = player['route'][player['route_index']]
            else:
                distance_to_move = 0

    def update_player_positions(self, delta_time):
        """Update the positions of all players."""
        for player in self.players:
            self.move_player(player, delta_time)  # Change to method call

    def convert_route_to_screen(self, player, x_scale, y_scale):
        if player['route'] is None:
            return None  # Return None if there is no route

        # Initial screen position of the player
        line_of_scrimmage = (self.line_of_scrimmage_yard * x_scale)
        initial_screen_x = line_of_scrimmage - (player['y'] * y_scale)
        initial_screen_y = (self.window_size[1] / 2) + (player['x'] * x_scale)

        screen_route = []
        current_x, current_y = initial_screen_x, initial_screen_y + self.ball_position
        for point in player['route']:
            # Rotate route points 90 degrees to the left
            next_x = current_x - (point[1] * y_scale)  # Y becomes X
            next_y = current_y + (point[0] * x_scale)  # X becomes Y
            screen_route.append((next_x, next_y))
            # Update current position for the next point
            current_x, current_y = next_x, next_y

        return screen_route

    def move_ball(self, delta_time):
        # Assuming a constant speed for the ball
        ball_speed = self.ball_speed  # Adjust as needed
        distance_to_move = ball_speed * delta_time
        self.ball_position_x, self.ball_position_y = self.interpolate((self.ball_position_x, self.ball_position_y),
                                                                      (self.ball_target_x, self.ball_target_y),
                                                                      distance_to_move)

    def create_end_zone_route(self, player):
        """Create a route for the player to run towards the end zone."""
        field_length = 120  # Length of the field, including end zones

        # Determine the direction towards the closest end zone
        direction_to_end_zone = 1 if player['x'] < field_length / 2 else -1

        # Calculate the x-coordinate of the end zone
        end_zone_x = 0 if direction_to_end_zone == 1 else field_length

        # Create a route that extends from the current position to the end zone
        route_to_end_zone = [(end_zone_x - 20, player['y'])]
        return route_to_end_zone

    def get_receiver_positions_for_ticks(self, receiver, quarterback, total_ticks, ball_speed):
        quarterback_x = quarterback['x']
        quarterback_y = quarterback['y']
        positions_with_distances_and_times = []

        player_speed = receiver['player_object'].speed / (self.ball_speed / 60)

        distance_per_tick = player_speed / 60  # Assuming 60 ticks per second

        current_x, current_y = receiver['x'], receiver['y']
        route_index = receiver['route_index']

        # print(f'Current receiver position: ({current_x}, {current_y})')
        for tick in range(1, total_ticks + 1):  # Starting from tick 1 to total_ticks
            if route_index >= len(receiver['route']):
                # If the end of the route is reached, stay at the last position
                distance = math.hypot(quarterback_x - current_x, quarterback_y - current_y)
                time_to_reach = distance / ball_speed
                positions_with_distances_and_times.append((tick, (current_x, current_y), distance, time_to_reach))
                # print(f"Predicted Tick {tick}: Receiver at end of route, position: ({current_x}, {current_y})")
                continue

            next_x, next_y = receiver['route'][route_index]
            distance_to_next_point = math.hypot(next_x - current_x, next_y - current_y)

            if distance_per_tick >= distance_to_next_point:
                current_x, current_y = next_x, next_y
                route_index += 1
                remaining_distance = distance_per_tick - distance_to_next_point
                while route_index < len(receiver['route']) and remaining_distance > 0:
                    next_x, next_y = receiver['route'][route_index]
                    distance_to_next_point = math.hypot(next_x - current_x, next_y - current_y)
                    if remaining_distance >= distance_to_next_point:
                        current_x, current_y = next_x, next_y
                        route_index += 1
                        remaining_distance -= distance_to_next_point
                    else:
                        break
            else:
                fraction = distance_per_tick / distance_to_next_point
                current_x += (next_x - current_x) * fraction
                current_y += (next_y - current_y) * fraction

            distance = math.hypot(quarterback_x - current_x, quarterback_y - current_y)
            time_to_reach = distance / ball_speed
            positions_with_distances_and_times.append((tick, (current_x, current_y), distance, time_to_reach))
            # print(f"Predicted Tick {tick}: Receiver position: ({current_x}, {current_y})")

        return positions_with_distances_and_times

    def predict_receiver_position(self, receiver, quarterback):
        # Find every receiver location in every subsequent amount of ticks (and distance away from the qb (x))
        # Find how long it would take to reach every distance away from the QB (y)
        # Find the first intersection (or close enough)

        ball_speed = self.ball_speed  # Ball speed in units per second
        positions = self.get_receiver_positions_for_ticks(receiver, quarterback, 500, ball_speed)
        self.predicted_positions = positions

        # Find the position where the time for the ball to reach the receiver is closest to the receiver's arrival time
        best_match = min(positions, key=lambda p: abs(p[0] - p[2]))

        # Extract the best target coordinates
        target_x, target_y = best_match[1]

        return target_x, target_y

    def check_contact(self, player1, player2, contact_threshold=10.7):
        if not player1['is_active'] or not player2['is_active']:
            return False

        if player1['type'] == 'Running Back':
            contact_threshold += 12
        if player1['type'] == 'Tight End':
            contact_threshold += 6
        """Check if two players are in contact based on position."""
        distance = math.hypot(player1['x'] - player2['x'], player1['y'] - player2['y'])
        return distance < contact_threshold

    def move_defensive_players(self, delta_time):
        if not self.play_active:  # Stop updating positions if the play is no longer active
            return
        for defensive_player in self.players:
            if defensive_player['type'] in ['Defensive End', 'Defensive Tackle']:
                # Move towards the ball
                ball_x = self.ball_position_x
                ball_y = self.ball_position_y
                player_x = defensive_player['x']
                player_y = defensive_player['y']

                # Calculate the direction vector from the defensive player to the ball
                direction_x = ball_x - player_x
                direction_y = ball_y - player_y

                # Normalize the direction vector
                magnitude = math.sqrt(direction_x ** 2 + direction_y ** 2)
                if magnitude > 0:
                    direction_x /= magnitude
                    direction_y /= magnitude

                # Adjust the player's position towards the ball
                speed = 52  # Adjust the speed as necessary
                if hasattr(defensive_player['player_object'], 'speed'):
                    speed = defensive_player['player_object'].speed
                    speed *= 0.6

                new_x = player_x + direction_x * speed * delta_time
                new_y = player_y + direction_y * speed * delta_time

                defensive_player['x'] = new_x
                defensive_player['y'] = new_y

            elif defensive_player['type'] in ['Cornerback', 'Safety']:
                # Check if the ball has not been thrown
                if not self.ball_caught and not self.ball_in_air:
                    closest_player = None
                    closest_distance = float('inf')

                    # Iterate through offensive players to find the closest receiver, tight end, or running back
                    for offensive_player in self.players:
                        if offensive_player['type'] in ['Wide Receiver', 'Tight End', 'Running Back']:
                            distance = math.hypot(defensive_player['x'] - offensive_player['x'],
                                                  defensive_player['y'] - offensive_player['y'])
                            if distance < closest_distance:
                                closest_player = offensive_player
                                closest_distance = distance

                    if closest_player is not None:
                        offset = 50
                        if defensive_player['type'] == 'Safety':
                            offset = 200
                        # Move the cornerback towards the closest player
                        player_x = defensive_player['x']
                        player_y = defensive_player['y']
                        target_x = closest_player['x'] - offset
                        target_y = closest_player['y']

                        # Calculate the direction vector
                        direction_x = target_x - player_x
                        direction_y = target_y - player_y

                        # Normalize the direction vector
                        magnitude = math.sqrt(direction_x ** 2 + direction_y ** 2)
                        if magnitude > 0:
                            direction_x /= magnitude
                            direction_y /= magnitude

                        # Adjust the cornerback's position towards the closest player
                        speed = defensive_player['player_object'].speed
                        new_x = player_x + direction_x * speed * delta_time
                        new_y = player_y + direction_y * speed * delta_time

                        # Update the cornerback's position
                        defensive_player['x'] = new_x
                        defensive_player['y'] = new_y
                elif self.ball_in_air:
                    # Move towards the target
                    ball_x = self.ball_target_x
                    ball_y = self.ball_target_y
                    player_x = defensive_player['x']
                    player_y = defensive_player['y']

                    # Calculate the direction vector from the defensive player to the ball
                    direction_x = ball_x - player_x
                    direction_y = ball_y - player_y

                    # Normalize the direction vector
                    magnitude = math.sqrt(direction_x ** 2 + direction_y ** 2)
                    if magnitude > 0:
                        direction_x /= magnitude
                        direction_y /= magnitude

                    # Adjust the player's position towards the ball
                    speed = defensive_player['player_object'].speed
                    new_x = player_x + direction_x * speed * delta_time
                    new_y = player_y + direction_y * speed * delta_time

                    # Check for contact with any other players (offensive or defensive)
                    contact_detected = False
                    for other_player in self.players:
                        if other_player != defensive_player:
                            distance = math.hypot(new_x - other_player['x'], new_y - other_player['y'])
                            if distance < 5:  # Adjust the contact radius as necessary
                                # Contact detected, stop moving in that direction
                                contact_detected = True
                                break

                    if not contact_detected:
                        # No contact detected, update player's position
                        defensive_player['x'] = new_x
                        defensive_player['y'] = new_y
                else:
                    # Move towards the ball
                    ball_x = self.ball_position_x
                    ball_y = self.ball_position_y
                    player_x = defensive_player['x']
                    player_y = defensive_player['y']

                    # Calculate the direction vector from the defensive player to the ball
                    direction_x = ball_x - player_x
                    direction_y = ball_y - player_y

                    # Normalize the direction vector
                    magnitude = math.sqrt(direction_x ** 2 + direction_y ** 2)
                    if magnitude > 0:
                        direction_x /= magnitude
                        direction_y /= magnitude

                    # Adjust the player's position towards the ball
                    speed = defensive_player['player_object'].speed
                    new_x = player_x + direction_x * speed * delta_time
                    new_y = player_y + direction_y * speed * delta_time

                    # Check for contact with any other players (offensive or defensive)
                    contact_detected = False
                    for other_player in self.players:
                        if other_player != defensive_player:
                            distance = math.hypot(new_x - other_player['x'], new_y - other_player['y'])
                            if distance < 6:  # Adjust the contact radius as necessary
                                # Contact detected, stop moving in that direction
                                contact_detected = True
                                break

                    if not contact_detected:
                        # No contact detected, update player's position
                        defensive_player['x'] = new_x
                        defensive_player['y'] = new_y
            elif defensive_player['type'] in ['Linebacker']:
                # Check if the ball has not been thrown
                if not self.ball_caught:
                    pass
                else:
                    # Move towards the ball
                    ball_x = self.ball_position_x
                    ball_y = self.ball_position_y
                    player_x = defensive_player['x']
                    player_y = defensive_player['y']

                    # Calculate the direction vector from the defensive player to the ball
                    direction_x = ball_x - player_x
                    direction_y = ball_y - player_y

                    # Normalize the direction vector
                    magnitude = math.sqrt(direction_x ** 2 + direction_y ** 2)
                    if magnitude > 0:
                        direction_x /= magnitude
                        direction_y /= magnitude

                    # Adjust the player's position towards the ball
                    speed = defensive_player['player_object'].speed
                    new_x = player_x + direction_x * speed * delta_time
                    new_y = player_y + direction_y * speed * delta_time

                    # Check for contact with any other players (offensive or defensive)
                    contact_detected = False
                    for other_player in self.players:
                        if other_player != defensive_player:
                            distance = math.hypot(new_x - other_player['x'], new_y - other_player['y'])
                            if distance < 5:  # Adjust the contact radius as necessary
                                # Contact detected, stop moving in that direction
                                contact_detected = True
                                break

                    if not contact_detected:
                        # No contact detected, update player's position
                        defensive_player['x'] = new_x
                        defensive_player['y'] = new_y

    def calculate_new_line_of_scrimmage(self):
        # Check if the ball was caught
        if self.ball_caught:
            # Convert pixels to yards
            x_scale = self.window_size[0] / 120  # Length of the field in pixels
            current_ball_position_yards = self.ball_position_x / x_scale

            # Calculate yards gained or lost
            yards_gained = current_ball_position_yards - self.line_of_scrimmage_yard
            print(f'Yards gained: {yards_gained * -1}')
            # print(f'Initial LOS: {self.line_of_scrimmage_yard}')

            # Update line of scrimmage
            new_line_of_scrimmage = self.line_of_scrimmage_yard + yards_gained
            # print(f'New LOS: {new_line_of_scrimmage}')

            # print(f'First Down Yard: {self.first_down_yard}')
            # Determine if a first down is achieved
            if new_line_of_scrimmage <= self.first_down_yard:
                # Set new line of scrimmage and new first down yard line
                self.first_down_achieved = True
                new_first_down_yard_line = new_line_of_scrimmage - 10  # Assuming 10 yards for a first down
            else:
                # Keep the first down yard line the same
                new_first_down_yard_line = self.first_down_yard
        elif self.sacked:
            # Calculate the yardage lost due to the sack
            sack_x, _ = self.sack_position
            sack_x = sack_x / (self.window_size[0] / 120)
            sack_yard_loss = sack_x - self.line_of_scrimmage_yard
            new_line_of_scrimmage = self.line_of_scrimmage_yard + sack_yard_loss
            new_first_down_yard_line = self.first_down_yard
            print(f"Quarterback sacked! Lost {sack_yard_loss} yards.")
        else:
            # If the ball was dropped, keep the line of scrimmage and first down yard line the same
            new_line_of_scrimmage = self.line_of_scrimmage_yard
            new_first_down_yard_line = self.first_down_yard
            if not self.intercepted:
                print("Ball dropped. Line of scrimmage remains the same.")

        # Ensure the values are within the bounds of the field
        new_line_of_scrimmage = max(0, min(new_line_of_scrimmage, 120))
        new_first_down_yard_line = max(10, min(new_first_down_yard_line, 120))

        return new_line_of_scrimmage, new_first_down_yard_line

    def capture_final_state(self):
        # Capture necessary details for the new game state
        lines = self.calculate_new_line_of_scrimmage()
        new_line_of_scrimmage = lines[0]
        new_first_down_line = lines[1]
        new_ball_position = self.ball_position_x  # Example, adjust based on your game's coordinate system
        new_down = self.down + 1
        if self.first_down_achieved:
            new_down = 1
        elif new_down > 4:
            # It's more than 4th down, possession is over
            print("Turnover on downs.")
            self.possession_over = True
            new_down = 1  # Reset down for next possession

        if self.possession_over:
            if self.has_ball == 'Home':
                self.has_ball = 'Away'
            else:
                self.has_ball = 'Home'

        # Create a new game_state object with updated values
        new_state = game_state(
            offensive_formation=self.offensive_formation,
            defensive_formation=self.defensive_formation,
            line_of_scrimmage_yard=new_line_of_scrimmage,
            ball_position=0,  # Fix this eventually
            first_down_yard=new_first_down_line,
            down=new_down,
            home_score=self.home_score,
            away_score=self.away_score,
            time_remaining=self.time_remaining - 5,
            has_ball=self.has_ball,
            home_team=self.home_team,
            away_team=self.away_team
        )
        return new_state

    def set_placed_players(self):
        if self.has_ball == 'Home':
            offensive_team = self.home_team
            defensive_team = self.away_team
        else:
            offensive_team = self.away_team
            defensive_team = self.home_team

        wr_counter = 0
        ol_counter = 0
        de_counter = 0
        dt_counter = 0
        lb_counter = 0
        s_counter = 0
        cb_counter = 0
        for player in self.players:
            if player['type'] == "Quarterback":
                player['player_object'] = offensive_team.get_position("Quarterback")
            elif player['type'] == "Running Back":
                player['player_object'] = offensive_team.get_position("Running Back")
            elif player['type'] == "Wide Receiver":
                player['player_object'] = offensive_team.get_position("Wide Receiver", wr_counter)
                wr_counter += 1
            elif player['type'] == "Tight End":
                player['player_object'] = offensive_team.get_position("Tight End")
            elif player['type'] == "Offensive Lineman":
                player['player_object'] = offensive_team.get_position("Offensive Lineman", ol_counter)
                ol_counter += 1

            elif player['type'] == "Defensive End":
                player['player_object'] = defensive_team.get_position("Defensive End", de_counter)
                de_counter += 1
            elif player['type'] == "Defensive Tackle":
                player['player_object'] = defensive_team.get_position("Defensive Tackle", dt_counter)
                dt_counter += 1
            elif player['type'] == "Linebacker":
                player['player_object'] = defensive_team.get_position("Linebacker", lb_counter)
                lb_counter += 1
            elif player['type'] == "Safety":
                player['player_object'] = defensive_team.get_position("Safety", s_counter)
                s_counter += 1
            elif player['type'] == "Cornerback":
                player['player_object'] = defensive_team.get_position("Cornerback", cb_counter)
                cb_counter += 1
            else:
                print(player['type'])

    def generate_throw_time(self, mean=2.0, std_dev=0.75, min_time=0.3, max_time=6.0):
        while True:
            throw_time = random.gauss(mean, std_dev)
            if min_time <= throw_time <= max_time:
                return throw_time

    def simulate_tackle(self, defenders, ball_carrier):
        agility = ball_carrier['player_object'].agility / 2
        tackling = 0
        for defender in defenders:
            tackling += defender['player_object'].tackling * len(defenders)
        total_skills = agility + tackling
        result = random.randint(0, int(total_skills + 1))
        # print(f'Total Number: {total_skills}')
        # print(f'Agility: {agility}')
        #  print(f'Random Number: {result}')
        if result < agility:
            return False
        return True

    def select_receiver(self, receivers, defenders, quarterback):
        # Calculate distance of closest defender to each receiver
        receiver_defender_distances = []
        for receiver in receivers:
            closest_defender_distance = min(
                [math.hypot(defender['x'] - receiver['x'], defender['y'] - receiver['y']) for defender in defenders]
            )
            receiver_defender_distances.append((receiver, closest_defender_distance))

        # Sort receivers by the distance of the closest defender (ascending)
        sorted_receivers = sorted(receiver_defender_distances, key=lambda x: x[1], reverse=True)
        #for i in sorted_receivers:
            #print(i[0]['player_object'].number, i[1])

        receiver_counter = 0
        # Select a receiver based on quarterback's field vision
        chance_to_pick_correctly = (quarterback['player_object'].field_vision / 100) ** 2
        # print(f'Every cycle, the QB has a {chance_to_pick_correctly}% chance to pick the right receiver.')
        while receiver_counter < len(receivers):
            r_num = random.random()
            if r_num < chance_to_pick_correctly:
                # Choose the best option most of the time
                return sorted_receivers[receiver_counter][0]
            receiver_counter += 1

        return sorted_receivers[-1][0]

    def calculate_optimal_direction(self, ball_carrier, defenders):
        """
        Calculate the optimal direction for the ball carrier to move in, considering nearby defenders and field boundaries.
        The endzone is always to the left of the screen.
        """
        evasion_factor = ball_carrier['player_object'].route_running / 100  # Normalize between 0 and 1
        move_x, move_y = -1, 0  # Default movement towards the left endzone

        # Check if the player is on the sideline
        sideline_threshold = 12  # Distance from the edge of the field to be considered 'on the sideline'
        on_sideline = ball_carrier['y'] <= sideline_threshold or ball_carrier['y'] >= self.window_size[1] - sideline_threshold

        # If on the sideline, move directly left towards the endzone
        if on_sideline:
            return math.radians(180)  # 180 degrees for moving left

        for defender in defenders:
            dx, dy = defender['x'] - ball_carrier['x'], defender['y'] - ball_carrier['y']
            distance = math.hypot(dx, dy)
            if distance < 70:  # Evasion radius
                # Adjust move direction away from defender, but only alter the y-component to avoid moving right
                move_y -= evasion_factor * dy / distance
                evasion_required = True

        # Normalize the move direction and apply a speed factor
        move_distance = math.hypot(move_x, move_y)
        if move_distance != 0:
            move_x, move_y = move_x / move_distance, move_y / move_distance

        return math.atan2(move_y, move_x)

    def update_ball_carrier_movement(self, ball_carrier, delta_time, defenders):
        # Get the optimal direction as an angle
        angle = self.calculate_optimal_direction(ball_carrier, defenders)

        # Determine speed of the ball carrier
        speed = ball_carrier['player_object'].speed  # Adjust the speed as necessary
        distance_to_move = speed * delta_time

        # Determine the next point based on the direction and distance
        next_point_x = ball_carrier['x'] + math.cos(angle) * distance_to_move
        next_point_y = ball_carrier['y'] + math.sin(angle) * distance_to_move

        # Update the ball carrier's position using interpolation for smoother movement
        ball_carrier['x'], ball_carrier['y'] = self.interpolate((ball_carrier['x'], ball_carrier['y']), (next_point_x, next_point_y), distance_to_move)

    def is_near(self, player1, player2, threshold=25):
        if not player1['is_active'] or not player2['is_active']:
            return False
        if player2['x'] < player1['x'] - 8:
            return False
        return math.hypot(player1['x'] - player2['x'], player1['y'] - player2['y']) < threshold

    def calculate_breakthrough_chance(self, ol, dl):
        # Calculate chance based on OL's blocking technique and DL's pass rush
        pass_rush = (dl['player_object'].pass_rush**2) / 1000
        blocking = (ol['player_object'].blocking_technique**3) / 100
        return pass_rush/blocking

    def simulate_blocking(self):
        # Find the quarterback's position
        qb_position = next((player for player in self.players if player['type'] == 'Quarterback'), None)
        if qb_position is None:
            return  # Quarterback not found, skip blocking simulation

        qb_x, qb_y = qb_position['x'], qb_position['y']

        for dl in [p for p in self.players if p['type'] in ['Defensive Tackle', 'Defensive End']]:
            nearest_ol = []
            ol_strength = 0
            for ol in [p for p in self.players if p['type'] == 'Offensive Lineman' and p['is_active']]:
                if self.is_near(dl, ol):
                    nearest_ol.append(ol)
                    ol_strength += ol['player_object'].blocking_power

            if len(nearest_ol) > 0:
                dl_strength = dl['player_object'].strength
                total_strength = ol_strength + dl_strength
                random_number = random.randint(0, total_strength + 1)

                # Calculate angle between DL and QB
                angle = math.atan2(qb_y - dl['y'], qb_x - dl['x'])
                dx = math.cos(angle)
                dy = math.sin(angle)

                # DL wins
                if random_number > ol_strength:
                    for ol in nearest_ol:
                        ol['x'] -= dx
                        ol['y'] -= dy
                    dl['x'] += dx
                    dl['y'] += dy
                # OL wins
                else:
                    for ol in nearest_ol:
                        ol['x'] += dx
                        ol['y'] += dy
                    dl['x'] -= 3 * dx
                    dl['y'] -= 3 * dy

                if random.random() < self.calculate_breakthrough_chance(nearest_ol[0], dl):
                    nearest_ol[0]['is_active'] = False  # OL is beaten

    def run_play(self, play):
        # Initialize the players and play
        self.place_players(play)
        self.set_placed_players()
        self.ball_speed = self.get_qb_strength()
        quarterback = None

        # Find the quarterback's position
        quarterback_x, quarterback_y = None, None
        for player in self.players:
            if player['type'] == 'Quarterback':
                quarterback = player
                quarterback_x, quarterback_y = player['x'], player['y']
                break

        # Ensure quarterback position is found
        if quarterback_x is None or quarterback_y is None:
            raise ValueError("Quarterback position not found")

        # Initialize hike variables
        hike_start_time = time.time()
        hike_duration = 0.5
        hike_completed = False
        start_ball_x, start_ball_y = self.line_of_scrimmage_yard * self.window_size[0] / 120, self.window_size[1] / 2

        # Randomly choose time to throw between 1 and 3 seconds after the hike
        throw_time = self.generate_throw_time()
        time_since_hike = 0

        # Initialize the target receiver and ball state
        self.target_receiver = None
        self.ball_in_air = False
        self.ball_caught = False
        tick_counter = 1

        # Main game loop
        running = True
        last_frame_time = time.time()
        while running:
            current_time = time.time()
            if self.simulated_game:
                # For simulated games, process game logic faster with a fixed time step
                delta_time = 0.043  # This is an arbitrary number; you may adjust it as needed
            else:
                # For non-simulated games, calculate the time since the last frame
                delta_time = current_time - last_frame_time
                #delta_time = 0.05
                last_frame_time = current_time

                # Handle events and render graphics only for non-simulated games
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

            # Update player positions
            if not self.ball_caught:
                self.simulate_blocking()
                self.update_player_positions(delta_time)

            # Update ball position if hike is not completed
            if not hike_completed:
                progress = min(1, (current_time - hike_start_time) / hike_duration)
                self.ball_position_x = start_ball_x + (quarterback_x - start_ball_x) * progress
                self.ball_position_y = start_ball_y + (quarterback_y - start_ball_y) * progress

                if progress >= 1:
                    hike_completed = True

            # Update time since hike
            time_since_hike += delta_time

            if not self.ball_in_air and not self.ball_caught and time_since_hike >= throw_time:
                if self.target_receiver is None:
                    receivers = [p for p in self.players if p['type'] in ['Wide Receiver', 'Tight End', 'Running Back']]
                    defenders = [p for p in self.players if
                                 p['type'] in ['Safety', 'Cornerback', 'Linebacker', 'Defensive End',
                                               'Defensive Tackle']]

                    # Use the select_receiver method to choose a target
                    self.target_receiver = self.select_receiver(receivers, defenders, quarterback)

                    # Set the target coordinates for the pass
                    self.ball_target_x, self.ball_target_y = self.predict_receiver_position(self.target_receiver,
                                                                                            quarterback)
                    self.target_coordinates = (self.ball_target_x, self.ball_target_y)
                    self.ball_in_air = True
                    self.start_ball_x = self.ball_position_x
                    self.start_ball_y = self.ball_position_y

            # Move the ball towards the receiver if it's in the air
            if self.ball_in_air:
                ball_speed = self.ball_speed  # example speed
                distance_to_move = ball_speed * delta_time
                current_ball_pos = (self.ball_position_x, self.ball_position_y)
                # print(f'Live Tick {tick_counter}')
                # print(f'Ball at: {current_ball_pos}')
                # Inside the game loop
                # print(f"Receiver at: ({self.target_receiver['x']}, {self.target_receiver['y']})")
                # print(f"Predicted Receiver Position: ({self.predicted_positions[tick_counter-1][1][0]}, {self.predicted_positions[tick_counter-1][1][1]})")

                tick_counter += 1

                self.ball_position_x, self.ball_position_y = self.interpolate(current_ball_pos,
                                                                              (self.ball_target_x, self.ball_target_y),
                                                                              distance_to_move)

                # Check if the ball has reached the target
                if math.hypot(self.ball_target_x - self.ball_position_x, self.ball_target_y - self.ball_position_y) < 5:
                    self.ball_in_air = False
                    interception_radius = 15

                    potential_interceptors = [p for p in self.players if p['type'] in ['Safety', 'Cornerback']
                                              and math.hypot(p['x'] - self.ball_position_x,
                                                             p['y'] - self.ball_position_y) < interception_radius]

                    intercepted = False
                    for interceptor in potential_interceptors:
                        if random.randint(0, 100) < interceptor['player_object'].catching / 4:
                            intercepted = True
                            print("Interception!")
                            # Update game state for interception
                            self.possession_over = True
                            self.ball_caught = False
                            self.play_active = False
                            self.intercepted = True
                            # Handle change of possession and ball placement logic
                            break

                    pass_coverage = 0
                    defender_counter = 0
                    for defender in potential_interceptors:
                        pass_coverage += defender['player_object'].pass_coverage / max(1, (8 - (defender_counter * 6)))
                        # print(f"Defender {defender_counter+1} pass coverage: {defender['player_object'].pass_coverage}")
                        defender_counter = 1

                    # print(f'Pass coverage is: {pass_coverage} between {len(potential_interceptors)} defenders')
                    # print(f"Receiver's catching is: {self.target_receiver['player_object'].catching}")
                    # print(f"Odds to catch is: {self.target_receiver['player_object'].catching - pass_coverage}")
                    random_catch_number = random.randint(0, 100)
                    # print(f"Random catch number is: {random_catch_number}")

                    if not intercepted and random_catch_number < max(3, self.target_receiver[
                                                                            'player_object'].catching - pass_coverage):
                        self.ball_caught = True
                        nearby_defenders = [p for p in self.players if
                                            p['type'] in ['Safety', 'Cornerback', 'Linebacker', 'Defensive End',
                                                          'Defensive Tackle']
                                            and self.check_contact(self.target_receiver, p,
                                                                   contact_threshold=100)]  # 30 can be adjusted

                        # self.target_receiver['route'] = self.create_evading_route(self.target_receiver, nearby_defenders)
                        # self.target_receiver['route_index'] = 0
                        if self.ball_position_x <= 103 and self.play_active:  # Touchdown condition
                            print("Touchdown!")
                            self.play_active = False
                            self.possession_over = True
                            if self.has_ball == 'Home':
                                self.home_score += 7
                            else:
                                self.away_score += 7
                    elif not intercepted:
                        print("Ball dropped!")
                        self.play_active = False

            # Move defensive players
            if self.play_active:
                self.move_defensive_players(delta_time)

            # Additional logic to move the ball with the receiver after the catch
            if not self.ball_in_air and self.ball_caught and self.target_receiver:
                self.ball_position_x, self.ball_position_y = self.target_receiver['x'], self.target_receiver['y']

                # Check for touchdown
                if self.ball_position_x <= 103 and self.play_active:  # Replace 'end_zone_x_position' with the actual value
                    print("Touchdown!")
                    self.play_active = False
                    self.possession_over = True  # End the possession
                    if self.has_ball == 'Home':
                        self.home_score += 7
                    else:
                        self.away_score += 7

            # Check for sack before the ball is thrown
            if not self.ball_in_air and not self.ball_caught:
                for player in self.players:
                    if player['type'] in ['Defensive End', 'Defensive Tackle', 'Linebacker']:
                        if self.check_contact(player, quarterback):
                            self.sacked = True
                            self.sack_position = (self.ball_position_x, self.ball_position_y)
                            self.play_active = False
                            break

                if not self.play_active:
                    # Sack occurred, end the play
                    for player in self.players:
                        player['route'] = None
                    return

            # Check for tackles if the play is active and the ball is caught
            if self.play_active and self.ball_caught:
                ball_carrier = self.target_receiver
                players_available_to_tackle = []
                for player in self.players:
                    if player['type'] in ['Defensive End', 'Linebacker', 'Defensive Tackle', 'Cornerback',
                                          'Safety'] and self.check_contact(ball_carrier, player):
                        players_available_to_tackle.append(player)

                if len(players_available_to_tackle) > 0:
                    # print(f'Player is in contact with {len(players_available_to_tackle)} players')
                    tackle_result = self.simulate_tackle(players_available_to_tackle, ball_carrier)
                    if tackle_result:
                        # Tackled
                        self.play_active = False
                        print("Play ended due to tackle!")
                        break
                    else:
                        # Broke Out
                        for player in players_available_to_tackle:
                            player['x'] += 30

                # Identify nearby defenders for the ball carrier
                nearby_defenders = [p for p in self.players if
                                    p['type'] in ['Safety', 'Cornerback', 'Linebacker', 'Defensive End',
                                                  'Defensive Tackle']
                                    and self.check_contact(self.target_receiver, p, contact_threshold=70)]

                # Update ball carrier's movement based on nearby defenders
                self.update_ball_carrier_movement(self.target_receiver, delta_time, nearby_defenders)

            if not self.play_active:
                # Stop all players
                for player in self.players:
                    player['route'] = None

                return

            # Blit the field surface onto the main screen
            if not self.simulated_game:
                self.screen.blit(self.field_surface, (0, 0))

                # Draw dynamic elements
                self.draw_scoreboard()
                if self.target_coordinates:
                    self.draw_target(*self.target_coordinates)
                self.draw_players()
                self.draw_football()

                # Update the display
                pygame.display.flip()

                # Cap the frame rate to 60 frames per second (FPS)
                pygame.time.Clock().tick(60)

        pygame.quit()
