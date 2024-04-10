# Example of a defensive formation subclass
from formations.DefensiveFormation import DefensiveFormation


class FourThree(DefensiveFormation):
    def __init__(self):
        super().__init__()

    def set_player_positions(self):
        # Positions relative to the line of scrimmage
        self.player_positions = [
            ('Defensive End', -7, 2),  # Left Defensive End
            ('Defensive Tackle', -3, 2),  # Left Defensive Tackle
            ('Defensive Tackle', 3, 2),  # Right Defensive Tackle
            ('Defensive End', 7, 2),  # Right Defensive End
            ('Linebacker', -5, 7),  # Left Outside Linebacker
            ('Linebacker', 0, 7),  # Middle Linebacker
            ('Linebacker', 5, 7),  # Right Outside Linebacker
            ('Cornerback', -15, 2),  # Left Cornerback
            ('Safety', -7, 15),  # Left Safety
            ('Safety', 7, 15),  # Right Safety
            ('Cornerback', 15, 2)  # Right Cornerback
        ]
