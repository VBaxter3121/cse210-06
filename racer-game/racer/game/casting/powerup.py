import constants
import random
from game.casting.actor import Actor
from game.shared.color import Color
from game.shared.point import Point

class Powerup(Actor):
    """A powerup that can be collected by the racer
    
    The responsibility of Powerup is to move itself."""

    def __init__(self):
        """Creates a new instance of Driver."""
        super().__init__()
        self._text = "?"
        self._color = constants.GREEN
        self._velocity = Point(-constants.CELL_SIZE * 2, 0)
        self._font_size = constants.FONT_SIZE * 4
        self._is_new = True
    #     self._lane = ""
    #     self._set_lane()

    def move_next(self):
        super().move_next()
        self._is_new = False

    def check_new(self):
        return self._is_new

    # def _set_lane(self):
    #     """Randomly chooses a starting lane."""
    #     lanes = ["top", "middle", "bottom"]
    #     lane = random.choice(lanes)
    #     self._lane = lane
    #     x = constants.RIGHT_X
    #     y = 0
    #     if lanes == "top":
    #         y = constants.LANE_TOP_Y
    #     elif lanes == "middle":
    #         y = constants.LANE_MIDDLE_Y
    #     elif lanes == "bottom":
    #         y = constants.LANE_BOTTOM_Y
    #     self.set_position(Point(x, y))