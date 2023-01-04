import pygame
from random import randrange, choice


class Card:
    def __init__(self, bingo):
        self.screen = bingo.screen
        self.rect_card = pygame.Surface((100, 100))
        self.rect_card.fill((255, 255, 255))
        self.settings = bingo.settings

    def create_card(self) -> list:
        nums_per_letter = 10
        # Создаем рандомную карточку БИНГО из 3 строк и 9 столбцов.

        card = {}  # Создаем пустой словарь под будущую карточку.
        lower = 1  # Верхний диапазон целых чисел, для генератора чисел в карточке.
        upper = 1 + nums_per_letter  # Нижний диапазон целых чисел, для
        # генератора чисел в карточке.

        # Генератор чисел, заполняющий всю карточку числами. В первом столбце числа
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

        # Делим словарь на 3 части по 9 чисел, которые представляют из себя 3
        # словаря вложенные в словарь split_horizontal_card.
        split_horizontal_card = [horizontal_line[0:9], horizontal_line[9: 18],
                                 horizontal_line[18:28]]

        # Заменяем 4 рандомных числа в каждой строке карточки на 0.
        for i in split_horizontal_card:
            random_number = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # Список для функции
            # choice.
            for k in range(0, 4):
                t = choice(random_number)  # Выбираем из списка random_number 4
                # случайных числа.
                random_number.remove(t)  # Удаляем выбранное число из списка
                i[
                    t] = 0  # Заменяем число по рандомной позиции t в строке
                # на 0.

        return split_horizontal_card

    def draw_card(self):
        y = 10
        n = 0
        while n != 3:
            x = 10
            for i in range(9):
                self.screen.blit(self.rect_card, (x, y))
                x += 110
            y += 110
            n += 1
