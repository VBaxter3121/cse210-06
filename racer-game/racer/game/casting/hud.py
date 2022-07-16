from game.casting.actor import Actor


class HUD(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
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
        self._lives -= 1
        self._update()

    def set_powerup(self, powerup):
        self._powerup = powerup
        self._update()

    def _update(self):
        self.set_text(f"""Score: {self._points}       Powerup: {self._powerup}        Lives: {self._lives}
__________________________________________________________________________________________________________""")

    def get_points(self):
        return self._points

    def get_powerup(self):
        return self._powerup

    def get_lives(self):
        return self._lives