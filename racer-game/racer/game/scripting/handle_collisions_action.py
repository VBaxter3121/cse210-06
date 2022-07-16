import constants
import random
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.directing.director import Director

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the following situations:
    # The racer tries to move out of bounds
    The racer collides with a driver
    The racer collides with a powerup
    A driver reaches the left side of the screen
    A powerup reaches the left side of the screen
    The game is over

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        powerups = cast.get_actors("powerups")
        drivers = cast.get_actors("drivers")
        if not self._is_game_over:
            if len(drivers) > 0:
                self._handle_driver_collision(cast)
            if len(powerups) > 0:
                self._handle_powerup_collision(cast)
            if len(drivers) > 0 or len(powerups) > 0:
                self._handle_edge_delete(cast)
            self._handle_game_over(cast, script)

    def _handle_driver_collision(self, cast):
        """Removes drivers and powerups and deducts a life when racer collides with a driver."""
        racer = cast.get_first_actor("racers")
        racer_x = racer.get_position().get_x()
        racer_y = racer.get_position().get_y()
        racer_pos = [racer_x, racer_y]

        hud = cast.get_first_actor("huds")
        current_powerup = hud.get_powerup()

        drivers = cast.get_actors("drivers")

        for driver in drivers:
            driver_x = driver.get_position().get_x()
            driver_y = driver.get_position().get_y()
            driver_pos = [driver_x, driver_y]
            if racer_pos == driver_pos and current_powerup != "invincible":
                cast.remove_actors("drivers")
                cast.remove_actors("powerups")
                hud.remove_life()
                lives = hud.get_lives()
                if lives == 0:
                    self._is_game_over = True

    def _handle_powerup_collision(self, cast):
        """Gives a random powerup to the racer when it collides with a powerup."""
        powerups = ["invincible", "destroy"]
        current_powerup = random.choice(powerups)

        racer = cast.get_first_actor("racers")
        racer_x = racer.get_position().get_x()
        racer_y = racer.get_position().get_y()
        racer_pos = [racer_x, racer_y]

        hud = cast.get_first_actor("huds")

        powerups = cast.get_actors("powerups")
        for powerup in powerups:
            powerup_x = powerup.get_position().get_x()
            powerup_y = powerup.get_position().get_y()
            powerup_pos = [powerup_x, powerup_y]

            if racer_pos == powerup_pos:
                cast.remove_actor("powerups", powerup)
                hud.set_powerup(current_powerup)

    def _handle_edge_delete(self, cast):
        """Removes drivers and powerups that reach the left edge of the screen."""
        powerups = cast.get_actors("powerups")
        for powerup in powerups:
            position = powerup.get_position()
            x = position.get_x()
            if x <= 0:
                cast.remove_actor("powerups", powerup)

        drivers = cast.get_actors("drivers")
        for driver in drivers:
            position = driver.get_position()
            x = position.get_x()
            if x <= 0:
                cast.remove_actor("drivers", driver)
                hud = cast.get_first_actor("huds")
                hud.add_points(100)
                

    def _handle_game_over(self, cast, script):
        """Shows the 'game over' message and turns all actors white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:

            cast.remove_actors("drivers")
            cast.remove_actors("powerups")

            actors = cast.get_all_actors()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            hud = cast.get_first_actor("huds")
            score = hud.get_points()
            message.set_text(f"Game Over! Final score: {score}")
            message.set_position(position)
            cast.add_actor("messages", message)

            for actor in actors:
                actor.set_color(constants.WHITE)

            # updates = script.get_actions("updates")
            # for update in updates:
            #     script.remove_action("updates", update)

    def check_game_over(self):
        return self._is_game_over