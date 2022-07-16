import constants
import random
from game.casting.actor import Actor
from game.casting.driver import Driver
from game.casting.powerup import Powerup
from game.scripting.action import Action
from game.shared.point import Point

class SpawnActorsAction(Action):
    """
    An update action that handles the spawning of drivers and powerups.
    
    The responsibility of SpawnActorsAction is to create drivers and powerups,
    and randomly assign them a lane.
    """

    def __init__(self):
        """Creates a new instance of SpawnActorsAction"""
        self._spawn_timer = 0

    def execute(self, cast, script):
        # updates = script.get_actions("updates")
        # collisions = updates[1]
        # if not collisions.check_game_over():
        self._spawn_timer += 1
        self._spawn_drivers(cast)
        self._spawn_powerups(cast)

    def _spawn_drivers(self, cast):
        if self._spawn_timer >= 10:
            spawn = random.randint(0, 100)
            if spawn >= 40:
                self._spawn_timer = 0
                # number = random.randint(1, 2)
                lanes = [constants.LANE_BOTTOM_Y, constants.LANE_MIDDLE_Y, constants.LANE_TOP_Y]
                # for i in range(number):
                cast.add_actor("drivers", Driver())
                lane = lanes[random.randint(0, len(lanes) - 1)]
                # lanes.remove(lane)
                drivers = cast.get_actors("drivers")
                for driver in drivers:
                    if driver.check_new():
                        driver.set_position(Point(constants.RIGHT_X, lane))

    def _spawn_powerups(self, cast):
        powerups = cast.get_actors("powerups")
        if len(powerups) == 0:
            if self._spawn_timer >= 10:
                spawn = random.randint(0, 100)
                if spawn >= 70:
                    self._spawn_timer = 0
                    lanes = [constants.LANE_BOTTOM_Y, constants.LANE_MIDDLE_Y, constants.LANE_TOP_Y]
                    cast.add_actor("powerups", Powerup())
                    lane = lanes[random.randint(0, len(lanes) - 1)]
                    powerups = cast.get_actors("powerups")
                    for powerup in powerups:
                        if powerup.check_new():
                            powerup.set_position(Point(constants.RIGHT_X, lane))