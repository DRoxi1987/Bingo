import pygame
import sys
from settings import Settings
from card import Card


class Game:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        self.fps = self.settings.fps
        pygame.display.set_caption("Bingo")

    def _check_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _fps(self):
        clock = pygame.time.Clock()
        clock.tick(self.fps)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()

    def run_game(self):
        while True:
            self._update_screen()
            self._fps()
            self._check_events()


if __name__ == '__main__':
    bingo = Game()
    bingo.run_game()
