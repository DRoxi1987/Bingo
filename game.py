import pygame
import sys
from settings import Settings
from card import Card
from pouch import Pouch


class Game:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        self.screen.fill(self.settings.bg_color)
        self.card = Card(self)
        self.pouch = Pouch()
        self.fps = self.settings.fps
        pygame.display.set_caption("Bingo")

    def _fps(self):
        clock = pygame.time.Clock()
        clock.tick(self.fps)

    def _check_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_e:
            a = self.card.create_card()
            print(a)
        elif event.key == pygame.K_w:
            b = self.pouch.iter()
            print(b)
            print(self.pouch.rand_list)

    def _check_keyup_events(self, event):
        pass

    def _update_screen(self):

        self.card.draw_card()
        pygame.display.flip()

    def run_game(self):
        while True:
            self._update_screen()
            self._fps()
            self._check_events()


if __name__ == '__main__':
    bingo = Game()
    bingo.run_game()
