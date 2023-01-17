import pygame as pg
import sys
from random import choice, randrange
from sprites import TextCard
from settings import Settings
from pouch import Pouch
from card import Card
from utilities import Utilities


class Game:
    def __init__(self):
        pg.init()

        pg.display.set_caption("Bingo")

        self.settings = Settings()

        self.screen = pg.display.set_mode(
            (self.settings.screen_width,
             self.settings.screen_height))
        self.screen.fill(self.settings.blue)

        self.card_field = pg.Surface((100, 100))
        self.card_field.fill(self.settings.color_white)
        self.card_field_rect = self.card_field.get_rect(center=(50, 50))

        self.clock = pg.time.Clock()
        self.fps = self.settings.fps
        self.win = ""

        self.size_rect_x = 100
        self.size_rect_y = 100
        self.utilities = Utilities()

        self.card_field_coord_list = self.settings.coord_list
        self.coord_list = self.utilities.choice_list()

        self.coord_list_checks = []

        self.pos_numbers_card_field = self.utilities.get_list(
            self.card_field_coord_list)
        self.pos_numbers_text = self.utilities.get_list(self.coord_list)

        self.text_group = pg.sprite.Group()
        self.card_field_group = pg.sprite.Group()

        self.list_of_card_numbers = self.utilities.create_list_of_card_numbers()

        self.background_card = pg.Surface((1000, 340))
        self.background_card.fill(self.settings.light_blue)
        self.background_card_rect = self.background_card.get_rect(
            topleft=(0, 0))

        self.pouch = Pouch()
        self.card = Card()

        self.card.get_card_field(self.card_field_coord_list, self.screen)
        self.get_card_numbers()
        self.utilities.create_coord_list_checks(self.list_of_card_numbers, self.coord_list_checks, self.pos_numbers_text)

    def win_check(self):

        if set(self.coord_list_checks[0:10]) == {0}:
            self.win = "Win1"

        if set(self.coord_list_checks[10:19]) == {0}:
            self.win = "Win1"

        if set(self.coord_list_checks[19:28]) == {0}:
            self.win = "Win1"

        if set(self.coord_list_checks[0:10]) == {0} and set(
                self.coord_list_checks[10:19]) == {0}:
            self.win = "Win2"

        if set(self.coord_list_checks[0:10]) == {0} and set(
                self.coord_list_checks[19:28]) == {0}:
            self.win = "Win2"

        if set(self.coord_list_checks[10:19]) == {0} and set(
                self.coord_list_checks[19:28]) == {0}:
            self.win = "Win2"

        if set(self.coord_list_checks) == {0}:
            self.win = "Win3"

        print(self.win)

    def get_card_numbers(self):

        for j in self.pos_numbers_text:
            number_text = str(self.list_of_card_numbers[j])
            text = TextCard(number_text)
            text.rect.x = \
                self.utilities.get_coords(j, self.size_rect_x, self.size_rect_y,
                                text.center[0],
                                text.center[1])[0]
            text.rect.y = \
                self.utilities.get_coords(j, self.size_rect_x, self.size_rect_y,
                                text.center[0],
                                text.center[1])[1]

            self.text_group.add(text)


    def check_events(self):
        # Проверки событий и их обработка на нажатие и отпускание клавиш.

        for event in pg.event.get():

            # Закрытие игры по нажатию на крестик окна.
            if event.type == pg.QUIT:
                sys.exit()

            # Проверка события на нажатие клавиши.
            elif event.type == pg.KEYUP:
                self.check_keyup_events(event)

            # Проверка события на отжатие клавиши.
            elif event.type == pg.KEYDOWN:
                self.check_keydown_events(event)

    def check_keyup_events(self, event):
        # Обработка событий отжатия клавиш.
        pass

    def check_keydown_events(self, event):
        # Если нажата клавиша ESCAPE, игра закрывается.
        if event.key == pg.K_ESCAPE:
            sys.exit()
        elif event.key == pg.K_e:
            ran = self.pouch.iter(self.pouch.rand_list)
            print(ran)
            self.pouch.draw_pouch(ran, self.screen)

            for j in self.coord_list_checks:
                if ran == j:
                    self.coord_list_checks[self.coord_list_checks.index(j)] = 0
                    print(self.coord_list_checks)

            for i in self.text_group:
                if str(ran) == TextCard.get_text(i):
                    i.update()
            self.win_check()

    def run_game(self):

        while True:
            self.clock.tick(30)
            self.screen.blit(self.background_card, self.background_card_rect)
            self.card.get_card_field(self.card_field_coord_list, self.screen)
            self.text_group.draw(self.screen)
            self.check_events()

            pg.display.update()


if __name__ == '__main__':
    game = Game()
    game.run_game()
