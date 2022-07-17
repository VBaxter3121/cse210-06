from tkinter import Y
import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the racer.
    
    The responsibility of ControlActorsAction is to get the direction and move the racer.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        y = 0
        # up
        if self._keyboard_service.is_key_down('up'):
            y = -200
        # down
        elif self._keyboard_service.is_key_down('down'):
            y = 200
        
        racer = cast.get_first_actor("racers")
        racer.set_position(y)

        # use powerup (space)
        if self._keyboard_service.is_key_down('space'):
            hud = cast.get_first_actor("huds")
            powerup = hud.get_powerup()
            if powerup == "Destroy":
                cast.remove_actors("drivers")
                hud.set_powerup("")