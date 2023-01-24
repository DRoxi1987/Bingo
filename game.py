import pygame as pg
from home_layer import HomeLayer
from game_layer import GameLayer
from settings import *


class Game:
    def __init__(self):
        pg.init()

        # Настройка основного окна.
        pg.display.set_caption(Screen.set_caption.value)
        self.screen_coord = (Screen.screen_width.value,
                             Screen.screen_height.value)
        self.screen = pg.display.set_mode(self.screen_coord)
        self.screen.fill(Colors.blue.value)

    def run_layer_screen_game(self):
        run_game = GameLayer()
        run_game.create_layer(self.screen, self.run_game)

    def run_game(self):
        run_home = HomeLayer(self.run_layer_screen_game)
        run_home.create_layer(self.screen)
