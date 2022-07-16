import constants
import random
from game.casting.actor import Actor
from game.casting.cast import Cast
from game.shared.color import Color
from game.shared.point import Point

class Road(Actor):
    """A collection of lines that seperate the three lanes.
    
    The responsibility of Road is simply to display road markings."""

    def __init__(self, cast):
        """Creates a new instance of Road."""
        super().__init__()
        self._generate_markings(cast)

    def _generate_markings(self, cast):
        """Creates actors to serve as road markings."""
        lane_length = int(constants.MAX_X / constants.CELL_SIZE)
        top_line = int((constants.LANE_MIDDLE_Y + constants.LANE_TOP_Y) / 2) + 25
        bottom_line = int((constants.LANE_BOTTOM_Y + constants.LANE_MIDDLE_Y) / 2) + 25
        
        for cell in range(lane_length):
            marking = Actor()
            marking.set_position(Point(cell * constants.CELL_SIZE, top_line))
            marking.set_text("-")
            marking.set_color(constants.GREY)
            cast.add_actor("roads", marking)

        for cell in range(lane_length):
            marking = Actor()
            marking.set_position(Point(cell * constants.CELL_SIZE, bottom_line))
            marking.set_text("-")
            marking.set_color(constants.GREY)
            cast.add_actor("roads", marking)