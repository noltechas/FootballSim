class OffensiveFormation:
    def __init__(self):
        self.player_positions = []  # Holds tuples of position name and relative coordinates

    def set_player_positions(self):
        raise NotImplementedError("This method must be implemented by subclasses.")
