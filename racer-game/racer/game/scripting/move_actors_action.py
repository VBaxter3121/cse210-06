from game.scripting.action import Action


class MoveActorsAction(Action):
    """
    An update action that moves all the actors.
    
    The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
    than zero.
    """

    def __init__(self):
        self._timer = 0
    
    def execute(self, cast, script):
        """Executes the move actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        self._timer += 1
        if self._timer >= 1:
            self._timer = 0
            actors = cast.get_all_actors()
            for actor in actors:
                actor.move_next()