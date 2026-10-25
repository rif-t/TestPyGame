from raylibpy import *

class Game:
    def run(self):
        init_window(1920, 1080, "raylib [core] example - basic window")

        set_target_fps(0)

        while not window_should_close():

            begin_drawing()
            clear_background(RAYWHITE)
            draw_text("Congrats! You created your first window!", 1920 // 2-200, 1080 //2, 32, MAROON)
            draw_fps(10, 10)
            end_drawing()

        close_window()

