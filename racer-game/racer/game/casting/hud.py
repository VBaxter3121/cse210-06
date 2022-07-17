from game.casting.actor import Actor


class HUD(Actor):
    """
    A record of points earned, current lives and current powerup.
    
    The responsibility of Score is to keep track of the points the player has earned by passing cars,
    lives that have been lost and currently held powerups. It contains methods for adding and getting
    points, adding and getting powerups, and subtracting and getting lives. Client should use get_text()
    to get a string representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
        _powerup (string): The currently held powerup.
        _lives (int): The current number of lives.
    """
    def __init__(self):
        super().__init__()
        self._points = 0
        self._powerup = ""
        self._lives = 3
        self._update()

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self._update()

    def remove_life(self):
        """Removes one life."""
        self._lives -= 1
        self._update()

    def set_powerup(self, powerup):
        """Sets the current powerup to a new value.
        
        Args:
            powerup (string): The powerup to add."""
        self._powerup = powerup
        self._update()

    def _update(self):
        """Sets the textual value of the HUD."""
        self.set_text(f"""Score: {self._points}        Lives: {self._lives}       Powerup: {self._powerup}
__________________________________________________________________________________________________________""")

    def get_points(self):
        """Returns the value of _points."""
        return self._points

    def get_powerup(self):
        """Returns the value of _powerup."""
        return self._powerup

    def get_lives(self):
        """Returns the value of _lives."""
        return self._lives