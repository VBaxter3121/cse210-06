import constants

from game.casting.actor import Actor
from game.shared.color import Color
from game.shared.point import Point


class Racer(Actor):
    """The player controlled car that races to overtake the other drivers.

    The responsibility of Racer is to move itself and keep track of its lane.
    """

    def __init__(self):
        """Creates a new instance of Racer."""
        super().__init__()
        self._text = "#"
        self._color = constants.BLUE
        self._position = Point(constants.RACER_X, constants.LANE_MIDDLE_Y)
        self._font_size = constants.FONT_SIZE * 4
        self._has_moved = False
        self._move_timer = 0

    def set_position(self, y):
        """Updates the position to the given one.
        
        Args:
            position (Point): The given position.
        """
        self._move_timer += 1
        if self._move_timer >= 5:
            self._has_moved = False
            self._move_timer = 0
        if self._has_moved == False and y != 0:
            x = constants.RACER_X
            y = self._position.get_y() + y
            if y > 500:
                y = 500
            elif y < 100:
                y = 100
            self._position = Point(x, y)
            self._has_moved = True