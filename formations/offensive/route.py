class Route:
    def __init__(self):
        self.coordinates = []

    def add_point(self, x, y):
        """Add a point to the route."""
        self.coordinates.append((x, y))

    def get_route(self):
        """Return the list of coordinates."""
        return self.coordinates