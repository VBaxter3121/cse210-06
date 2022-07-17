import constants
import random
from game.casting.actor import Actor
from game.shared.color import Color
from game.shared.point import Point

class Powerup(Actor):
    """A powerup that can be collected by the racer
    
    The responsibility of Powerup is to move itself."""

    def __init__(self):
        """Creates a new instance of Powerup."""
        super().__init__()
        self._text = "?"
        self._color = constants.GREEN
        self._velocity = Point(-constants.CELL_SIZE * 2, 0)
        self._font_size = constants.FONT_SIZE * 4
        self._is_new = True

    def move_next(self):
        """Moves the actor to its next position according to its velocity."""
        super().move_next()
        self._is_new = False

    def check_new(self):
        """Returns the value of _is_new"""
        return self._is_new