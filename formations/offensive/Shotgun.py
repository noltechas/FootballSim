from formations.OffensiveFormation import OffensiveFormation


class Shotgun(OffensiveFormation):

    def __init__(self):
        super().__init__()
        self.player_positions = []
        self.set_player_positions()

    def set_player_positions(self):
        # Positions relative to the line of scrimmage
        self.player_positions = [
            ('Quarterback', 0, -8),  # QB is a couple yards behind the line of scrimmage
            ('Running Back', 3, -8),  # RB is next to the QB
            ('Wide Receiver', -15, -3),  # WR far left
            ('Wide Receiver', 15, -3),   # WR far right
            ('Wide Receiver', 7, -3),    # WR right slot
            ('Tight End', -7, -3),   # TE left side on the line of scrimmage
            ('Offensive Lineman', 0, -1.5),       # Center on the line of scrimmage
            ('Offensive Lineman', -2.5, -2),  # Guards and Tackles on the line of scrimmage
            ('Offensive Lineman', 2.5, -2),
            ('Offensive Lineman', -5, -2.2),
            ('Offensive Lineman', 5, -2.2)
        ]

    def get_player_positions(self):
        return self.player_positions
