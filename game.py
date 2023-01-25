import pygame as pg
from home_layer import HomeLayer
from game_layer import GameLayer
from settings import *


class StateManager:
    def __init__(self, surface):
        self.state = "home"
        self.game_layer = GameLayer()
        self.home_layer = HomeLayer()
        self.surface = surface

    def state_manager(self):
        if self.state == "home":
            self.home_layer.create_layer(self.surface)
            k = self.home_layer.check_events_home()
            if k == "game":
                self.state = "game"

        elif self.state == "game":
            self.game_layer.create_layer(self.surface)
            l = self.game_layer.check_events_game()
            if l == "home":
                self.state = "home"

    def func(self, flag, text):
        self.state = flag
        self.home_layer.state = text

    def func2(self):
        self.state = self.game_layer.state
        self.game_layer.state = "game"


class Game:
    def __init__(self):
        pg.init()

        # Настройка основного окна.
        pg.display.set_caption(Screen.set_caption.value)
        self.screen_coord = (Screen.screen_width.value,
                             Screen.screen_height.value)
        self.screen = pg.display.set_mode(self.screen_coord)
        self.screen.fill(Colors.blue.value)

        self.state = StateManager(self.screen)

    def run_game(self):
        running = True
        while running:
            self.state.state_manager()
