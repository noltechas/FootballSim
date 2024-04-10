class game_state:
    def __init__(self, offensive_formation, defensive_formation, line_of_scrimmage_yard, ball_position, first_down_yard, down,
                 home_score, away_score, time_remaining, has_ball, home_team, away_team, overtime=False):
        self.offensive_formation = offensive_formation
        self.defensive_formation = defensive_formation
        self.line_of_scrimmage_yard = line_of_scrimmage_yard
        self.ball_position = ball_position
        self.first_down_yard = first_down_yard
        self.down = down
        self.home_score = home_score
        self.away_score = away_score
        self.time_remaining = time_remaining
        self.has_ball = has_ball
        self.home_team = home_team
        self.away_team = away_team
        self.overtime = overtime
