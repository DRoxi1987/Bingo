import pygame
import sys
from settings import Settings
from card import Card
from pouch import Pouch


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Bingo")
        self.settings = Settings()
        self.fps = self.settings.fps
        # Настройка основного экрана.
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        self.screen.fill(self.settings.bg_color)

        # Экземпляры классов
        self.card = Card(self)
        self.pouch = Pouch(self)

    def _fps(self):
        # Настройка фпс игры
        clock = pygame.time.Clock()
        clock.tick(self.fps)

    def _check_events(self):
        # Проверки событий и их обработка на нажатие и отпускание клавиш.

        for event in pygame.event.get():

            # Закрытие игры по нажатию на крестик окна.
            if event.type == pygame.QUIT:
                sys.exit()

            # Проверка события на нажатие клавиши.
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            # Проверка события на отжатие клавиши.
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        # Обработка событий нажатия клавиш.

        # Если нажата клавиша ESCAPE, игра закрывается.
        if event.key == pygame.K_ESCAPE:
            sys.exit()

        # Если нажата клавиша E, создаем список чисел на карточке бинго,
        # рисуем саму карточку на экране и размещаем ранее созданный список
        # цифр на ней.
        elif event.key == pygame.K_e:
            a = self.card.create_card()
            print(a)
            self.card.draw_card()
            self.card.draw_numbers()

        # Если нажата клавиша W, отрисовываем фон и число, которое мы
        # вытаскиваем из бочонка.
        elif event.key == pygame.K_w:
            self.pouch.draw_pouch()
            print(self.pouch.rand_list)

    def _check_keyup_events(self, event):
        # Обработка событий отжатия клавиш.
        pass

    def _update_screen(self):
        pygame.display.update()

    def run_game(self):
        while True:
            self._update_screen()
            self._fps()
            self._check_events()


if __name__ == '__main__':
    bingo = Game()
    bingo.run_game()
