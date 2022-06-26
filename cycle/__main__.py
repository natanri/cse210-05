import constants
from game.casting.cast import Cast
#from game.casting.food import Food
#from game.casting.score import Score
from game.casting.cycle1 import Cycle_1
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    #cast.add_actor("foods", Food())
    cast.add_actor("cycle", Cycle_1())
    #cast.add_actor("scores", Score())
    cycle1 = cast.get_first_actor("cycle1")
    cycle1.prepare_body(Point(50, 50), Point(constants.CELL_SIZE, 0), constants.GREEN)
    cast.add_actor("cycle2", Cycle_1())
    cycle2 = cast.get_first_actor("cycle2")
    cycle2.prepare_body(Point(845, 545), Point(constants.CELL_SIZE, 0), constants.RED)
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()
