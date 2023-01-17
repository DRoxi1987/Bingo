import pygame as pg
import sys
from sprites import TextCard
from settings import Settings
from pouch import Pouch
from card import Card
from utilities import Utilities


class Game:
    def __init__(self):
        pg.init()
        # Название окна.
        pg.display.set_caption("Bingo")

        # Экземпляры классов.
        self.settings = Settings()
        self.pouch = Pouch()
        self.card = Card(10, 10, 0, 0)
        self.card2 = Card(10, 350, 0, 340)
        self.utilities = Utilities()

        # Настройка основного окна.
        self.screen = pg.display.set_mode(
            (self.settings.screen_width,
             self.settings.screen_height))
        self.screen.fill(self.settings.blue)

        # Настройка FPS
        self.clock = pg.time.Clock()
        self.fps = self.settings.fps

        # Размеры квадратов, для размещения номеров карточки.
        self.size_rect_x = 100
        self.size_rect_y = 100

        # Базовая карточка со всеми нулями
        self.card_field_coord_list = self.settings.coord_list

        # Карточка с рандомными единицами
        self.coord_list = self.utilities.choice_list()
        self.coord_list_enemy = self.utilities.choice_list()

        # Список для проверки выигрыша игрока.
        # Простой список, где пустые места карточки заменены 0,
        # а остальные цифры оставлены на своих местах.
        self.coord_list_checks = []
        self.coord_list_checks_enemy = []

        # Флаг выигрыша игрока.
        self.win = ""
        self.win_enemy = ""

        # Список позиций 0-26, для фоновых квадратов карточки.
        self.pos_numbers_card_field = self.utilities.get_list(
            self.card_field_coord_list)

        # Список позиций 0-26, для спрайтов с номерами.
        self.pos_numbers_text = self.utilities.get_list(self.coord_list)
        print(self.pos_numbers_text)
        self.pos_numbers_text_enemy = self.utilities.get_list(
            self.coord_list_enemy)
        print(self.pos_numbers_text_enemy)
        # Группы спрайтов
        self.text_group = pg.sprite.Group()
        self.text_group1 = pg.sprite.Group()

        # Основной список номеров для карточки.
        self.list_of_card_numbers = self.utilities.create_list_of_card_numbers()
        print(self.list_of_card_numbers)
        self.list_of_card_numbers_enemy = self.utilities.create_list_of_card_numbers()
        print(self.list_of_card_numbers_enemy)

        # Заполняем группу спрайтов text_group.
        self.get_card_numbers(60, 60, self.pos_numbers_text,
                              self.list_of_card_numbers, self.text_group)
        self.get_card_numbers(60, 400, self.pos_numbers_text_enemy,
                              self.list_of_card_numbers_enemy, self.text_group1)


        # Заполняем список coord_list_checks.
        self.utilities.create_coord_list_checks(self.list_of_card_numbers,
                                                self.coord_list_checks,
                                                self.pos_numbers_text)

        self.utilities.create_coord_list_checks(
            self.list_of_card_numbers_enemy,
            self.coord_list_checks_enemy,
            self.pos_numbers_text_enemy)

    def draw_win_field(self, win_field, win_font_rect_coord, win_field_rect_coord):
        if win_field != "":
            win_font = pg.font.SysFont(self.settings.font_numbers,
                                       self.settings.font_numbers_size)
            text = win_field
            win_font_surface = win_font.render(text, True,
                                               self.settings.color_white,
                                               self.settings.red)

            win_field = pg.Surface((250, 75))
            win_font_rect = win_field.get_rect(center=(win_font_rect_coord))
            win_field_rect = win_field.get_rect(topleft=(win_field_rect_coord))
            win_field.fill(self.settings.red)
            self.screen.blit(win_field, (win_field_rect.x,
                                         win_field_rect.y))
            self.screen.blit(win_font_surface, win_font_rect)

    def win_check(self, coord_list_checks):
        # Проверка на выигрыш.
        win = ""
        if set(coord_list_checks[0:10]) == {0}:
            win = "Win1"

        if set(coord_list_checks[10:19]) == {0}:
            win = "Win1"

        if set(coord_list_checks[19:28]) == {0}:
            win = "Win1"

        if set(coord_list_checks[0:10]) == {0} and set(
                self.coord_list_checks[10:19]) == {0}:
            win = "Win2"

        if set(coord_list_checks[0:10]) == {0} and set(
                self.coord_list_checks[19:28]) == {0}:
            win = "Win2"

        if set(coord_list_checks[10:19]) == {0} and set(
                coord_list_checks[19:28]) == {0}:
            win = "Win2"

        if set(coord_list_checks) == {0}:
            win = "Win3"

        return win

    def get_card_numbers(self, i, n, pos_numbers_text, list_of_card_numbers,
                         text_group):
        # Генерируем спрайты класса TextCard и заполняем группу text_group.

        for j in pos_numbers_text:
            number_text = str(list_of_card_numbers[j])
            text = TextCard(number_text, i, n)
            text.rect.x = \
                self.utilities.get_coords(j, self.size_rect_x,
                                          self.size_rect_y,
                                          text.center[0],
                                          text.center[1])[0]
            text.rect.y = \
                self.utilities.get_coords(j, self.size_rect_x,
                                          self.size_rect_y,
                                          text.center[0],
                                          text.center[1])[1]
            text_group.add(text)

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

            for j in self.coord_list_checks_enemy:
                if ran == j:
                    self.coord_list_checks_enemy[self.coord_list_checks_enemy.index(j)] = 0
                    print(self.coord_list_checks_enemy)

            for i in self.text_group1:
                if str(ran) == TextCard.get_text(i):
                    i.update()

            self.win = self.win_check(self.coord_list_checks)
            self.win_enemy = self.win_check(self.coord_list_checks_enemy)


    def run_game(self):

        while True:
            self.clock.tick(30)
            self.check_events()

            self.draw_win_field(self.win, (1200, 66), (1015, 25))
            self.draw_win_field(self.win_enemy, (1200, 406), (1015, 365))

            self.card.draw_background_card(self.screen)
            self.card.get_card_field(self.card_field_coord_list, self.screen)
            self.text_group.draw(self.screen)
            self.card2.draw_background_card(self.screen)
            self.card2.get_card_field(self.card_field_coord_list, self.screen)
            self.text_group1.draw(self.screen)

            pg.display.update()


if __name__ == '__main__':
    game = Game()
    game.run_game()
