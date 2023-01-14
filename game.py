import pygame as pg
import sys
from random import choice, randrange
from sprites import TextCard, CardField
from settings import Settings


class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.screen = pg.display.set_mode((1200, 720))
        self.screen.fill(self.settings.blue)
        self.clock = pg.time.Clock()
        self.fps = self.settings.fps
        self.clock.tick(30)
        self.size_rect_x = 100
        self.size_rect_y = 100
        self.card_field_coord_list = self.settings.coord_list
        self.coord_list = self.choice_list()
        self.rectangle = pg.Surface((self.size_rect_x, self.size_rect_y))
        self.rectangle.fill(self.settings.color_white)
        self.rect_rectangle = self.rectangle.get_rect()
        self.pos_numbers_card_field = self.get_list(self.card_field_coord_list)
        self.pos_numbers_text = self.get_list(self.coord_list)
        self.text_group = pg.sprite.Group()
        self.card_field_group = pg.sprite.Group()
        self.s = self._create_card()
        self.background_card = pg.Surface((1000, 340))
        self.background_card.fill(self.settings.light_blue)
        self.background_card_rect = self.background_card.get_rect(
            topleft=(0, 0))

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

        print(horizontal_line)
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
            number_text = str(self.s[j])
            text = TextCard(number_text)
            text.rect.x = \
                self.get_coords(j, self.size_rect_x, self.size_rect_y,
                                text.center[0],
                                text.center[1])[0] + 5
            text.rect.y = \
                self.get_coords(j, self.size_rect_x, self.size_rect_y,
                                text.center[0],
                                text.center[1])[1] + 6
            self.text_group.add(text)

    def get_card_field(self):

        for j in self.pos_numbers_card_field:
            card_field = CardField()
            card_field.rect.x = \
                self.get_coords(j, self.size_rect_x, self.size_rect_y,
                                card_field.center[0],
                                card_field.center[1])[0] + 5
            card_field.rect.y = \
                self.get_coords(j, self.size_rect_x, self.size_rect_y,
                                card_field.center[0],
                                card_field.center[1])[1] + 6
            self.card_field_group.add(card_field)

    def run_game(self):

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            self.screen.blit(self.background_card, self.background_card_rect)
            self.card_field_group.draw(self.screen)
            self.get_card_field()
            self.text_group.draw(self.screen)
            self.get_card_numbers()
            pg.display.update()


if __name__ == '__main__':
    game = Game()
    game.run_game()
