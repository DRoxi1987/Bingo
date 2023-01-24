import pygame as pg
import sys
from settings import *
from draw import *


class RunGame:
    def __init__(self, run_layer_screen_game):
        self.running = True
        self.run_layer_screen_game = run_layer_screen_game

    def create_layer(self, clock, event_func, surface):
        while self.running:
            clock.tick(30)
            event_func()
            surface.fill(Colors.blue.value)
            Drawer.draw_text("Bingo!",
                             Fonts.font_text.value,
                             Fonts.home_screen_font_logo_size.value,
                             surface, Colors.red.value, None,
                             Coords(Screen.screen_width.value // 2,
                                    Screen.screen_height.value // 3))

            Drawer.draw_text("Нажмите на пробел, чтобы начать!",
                             Fonts.font_text.value,
                             Fonts.home_screen_font_menu_size.value,
                             surface, Colors.color_white.value, None,
                             Coords(Screen.screen_width.value // 2,
                                    Screen.screen_height.value // 8 * 5))

            pg.display.update()

    def check_events_home(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False
                    pg.quit()
                    sys.exit()
                elif event.key == pg.K_SPACE:
                    self.running = False
                    self.run_layer_screen_game()
