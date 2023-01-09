import pygame
import sys
from settings import Settings
from card import NumberCards, CardNew
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
        self.screen.fill(self.settings.font_color)
        # Слои игры

        self.layer1 = pygame.Surface((1000, 340))
        self.layer2 = pygame.Surface((1000, 340))
        self.layer3 = pygame.Surface((1000, 340))


        # Экземпляры классов

        self.card_new_group = pygame.sprite.GroupSingle()
        self.card_new_group.add(CardNew(self))

        self.number_cards = NumberCards(self)
        self.number_cards_group = pygame.sprite.GroupSingle()
        self.number_cards_group.add(self.number_cards)

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

        self._fps()
        self._check_events()

    def run_game(self):
        while True:

            self.screen.blit(self.layer1, (0, 0))
            self.screen.blit(self.layer2, (0, 0))
            self.screen.blit(self.layer3, (0, 0),
                             special_flags=pygame.BLEND_RGB_MULT)
            self.card_new_group.draw(self.layer2)
            self.card_new_group.update()

            self.number_cards_group.draw(self.layer3)
            self.number_cards_group.update()



            self._update_screen()


if __name__ == '__main__':
    bingo = Game()
    bingo.run_game()
