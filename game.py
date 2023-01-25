import pygame as pg
from state_manager import StateManager
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

        # Экземпляр менеджера состояний
        self.state = StateManager(self.screen)

    def run_game(self):
        running = True
        while running:
            self.state.state_manager()
