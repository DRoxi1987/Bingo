import pygame as pg
import sys
from random import choice, randrange
from sprites import TextCard
from settings import Settings
from pouch import Pouch


class Game:
    def __init__(self):
        pg.init()

        pg.display.set_caption("Bingo")

        self.settings = Settings()

        self.screen = pg.display.set_mode(
            (self.settings.screen_width,
             self.settings.screen_height))

        self.screen.fill(self.settings.blue)
        self.layer0 = pg.Surface((1000, 340))
        self.layer0.fill(self.settings.color_white)

        self.card_field = pg.Surface((100, 100))
        self.card_field.fill(self.settings.color_white)
        self.card_field_rect = self.card_field.get_rect(center=(50, 50))

        self.clock = pg.time.Clock()
        self.fps = self.settings.fps
        self.win = ""

        self.size_rect_x = 100
        self.size_rect_y = 100

        self.card_field_coord_list = self.settings.coord_list
        self.coord_list = self.choice_list()

        self.coord_list_checks = []
        print(self.coord_list_checks)
        self.pos_numbers_card_field = self.get_list(self.card_field_coord_list)
        self.pos_numbers_text = self.get_list(self.coord_list)
        print(self.pos_numbers_text)

        self.text_group = pg.sprite.Group()
        self.card_field_group = pg.sprite.Group()

        self.list_of_card_numbers = self._create_card()
        print(self.list_of_card_numbers)
        self.background_card = pg.Surface((1000, 340))
        self.background_card.fill(self.settings.light_blue)
        self.background_card_rect = self.background_card.get_rect(
            topleft=(0, 0))

        self.pouch = Pouch()

        self.get_card_field()
        self.get_card_numbers()
        self.create_coord_list_checks()

    def win_check(self):

        if set(self.coord_list_checks[0:10]) == {0}:
            self.win = "Win1"

        if set(self.coord_list_checks[10:19]) == {0}:
            self.win = "Win1"

        if set(self.coord_list_checks[19:28]) == {0}:
            self.win = "Win1"

        if set(self.coord_list_checks[0:10]) == {0} and set(self.coord_list_checks[10:19]) == {0}:
            self.win = "Win2"

        if set(self.coord_list_checks[0:10]) == {0} and set(self.coord_list_checks[19:28]) == {0}:
            self.win = "Win2"

        if set(self.coord_list_checks[10:19]) == {0} and set(self.coord_list_checks[19:28]) == {0}:
            self.win = "Win2"

        if set(self.coord_list_checks) == {0}:
            self.win = "Win3"

        print(self.win)

    def create_coord_list_checks(self):

        for i in self.list_of_card_numbers:
            a = self.list_of_card_numbers.index(i)
            if a in self.pos_numbers_text:
                self.coord_list_checks.append(i)
            else:
                self.coord_list_checks.append(0)

    def _create_card(self):
        nums_per_letter = 10
        # Создаем рандомную карточку БИНГО из 3 строк и 9 столбцов.

        card = {}  # Создаем пустой словарь под будущую карточку.

        # Верхний диапазон целых чисел, для генератора чисел в карточке.
        lower = 1

        # Нижний диапазон целых чисел, для генератора чисел в карточке.
        upper = 1 + nums_per_letter

        # Генератор чисел, заполняющий всю карточку числами. В первом столбце числа.
        # от 1 до 10. Во втором от 11 до 20. И так далее до 9 ряда от 81 до 90.

        for letter in range(1, 10):  # Для диапазона от 0 до 9.
            card[letter] = []  # Создаем пустой список для каждой цифры.

            # Генерируем 3 случайных номера.
            while len(card[letter]) != 3:
                next_num = randrange(lower, upper)

                # Проверяем числа на уникальность.
                if next_num not in card[letter]:
                    card[letter].append(next_num)

            # Обновляем диапазон чисел для следующего столбца.
            lower = lower + nums_per_letter
            upper = upper + nums_per_letter

        # Преобразуем полученный словарь в список справа налево сверху вниз.
        horizontal_line = []
        for i in range(0, 3):
            for k, value in card.items():
                horizontal_line.append(card[k][i])

        return horizontal_line

    def get_list(self, mass):
        emp = []
        for i in range(3):
            for j in range(9):
                if mass[i][j] == 0:
                    num = self.get_number(i, j)
                    emp.append(num)
        return emp

    def get_number(self, m, n):
        return m * 9 + n

    def get_pos(self, num):
        return num // 9, num % 9

    def choice_list(self):

        coord_list_base = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

        for i in coord_list_base:
            random_number = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            for j in range(4):
                t = choice(random_number)
                random_number.remove(t)
                i[t] = 1
        return coord_list_base

    def get_coords(self, number, m, n, x0, y0):
        y = self.get_pos(number)[0]
        x = self.get_pos(number)[1]
        gap = 10

        x_pos = x0 + (m + gap) * x
        y_pos = y0 + (n + gap) * y
        return x_pos, y_pos

    def get_card_numbers(self):

        for j in self.pos_numbers_text:
            number_text = str(self.list_of_card_numbers[j])
            text = TextCard(number_text)
            text.rect.x = \
                self.get_coords(j, self.size_rect_x, self.size_rect_y,
                                text.center[0],
                                text.center[1])[0]
            text.rect.y = \
                self.get_coords(j, self.size_rect_x, self.size_rect_y,
                                text.center[0],
                                text.center[1])[1]

            self.text_group.add(text)

    def get_card_field(self):

        coord_list = self.get_list(self.card_field_coord_list)
        for i in coord_list:
            self.card_field_rect.x = \
                self.get_coords(i, self.size_rect_x, self.size_rect_y, 10,
                                10)[0]
            self.card_field_rect.y = \
                self.get_coords(i, self.size_rect_x, self.size_rect_y, 10,
                                10)[1]
            self.screen.blit(self.card_field,
                             (self.card_field_rect.x,
                              self.card_field_rect.y))

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
            self.get_card_field()
            self.text_group.draw(self.screen)
            self.check_events()

            pg.display.update()


if __name__ == '__main__':
    game = Game()
    game.run_game()
