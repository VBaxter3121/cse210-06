from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        powerups = cast.get_actors("powerups")
        hud = cast.get_first_actor("huds")
        if len(powerups) > 0:
            powerup = cast.get_first_actor("powerups")
        racer = cast.get_first_actor("racers")
        drivers = cast.get_actors("drivers")
        messages = cast.get_actors("messages")
        roads = cast.get_actors("roads")

        self._video_service.clear_buffer()
        if len(powerups) > 0:
            self._video_service.draw_actor(powerup)
        self._video_service.draw_actor(racer)
        self._video_service.draw_actors(drivers)
        self._video_service.draw_actor(hud)
        self._video_service.draw_actors(messages, True)
        self._video_service.draw_actors(roads)
        self._video_service.flush_buffer()