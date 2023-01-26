from random import randrange
from settings import *


class Utilities:
    @staticmethod
    def get_number(m, n):
        return m * 5 + n

    @staticmethod
    def get_pos(num):
        return num // 5, num % 5

    @staticmethod
    def get_coords(number, m, n, start_coordinates: Coords):

        y = Utilities.get_pos(number)[0]
        x = Utilities.get_pos(number)[1]
        gap = Rectangle.gap

        x_pos = start_coordinates.x + (m + gap) * x
        y_pos = start_coordinates.y + (n + gap) * y
        return x_pos, y_pos

    @staticmethod
    def get_list(mass):
        emp = []
        for i in range(5):
            for j in range(5):
                if mass[i][j] == 0:
                    num = Utilities.get_number(i, j)
                    emp.append(num)
        return emp

    @staticmethod
    def create_coord_list_checks(list_of_card_numbers: list, coord_list_checks: list,
                                 pos_numbers_text: list):

        for i in list_of_card_numbers:
            a = list_of_card_numbers.index(i)
            if a in pos_numbers_text:
                coord_list_checks.append(i)
            else:
                coord_list_checks.append(0)

    @staticmethod
    def create_list_of_card_numbers() -> list:
        nums_per_letter = 15

        card = {}  # Создаем пустой словарь под будущую карточку.

        # Верхний диапазон целых чисел, для генератора чисел в карточке.
        lower = 1

        # Нижний диапазон целых чисел, для генератора чисел в карточке.
        upper = 1 + nums_per_letter

        for letter in range(1, 6):  # Для диапазона от 0 до 5.
            card[letter] = []  # Создаем пустой список для каждой цифры.

            # Генерируем 5 случайных номера.
            while len(card[letter]) != 5:
                next_num = randrange(lower, upper)

                # Проверяем числа на уникальность.
                if next_num not in card[letter]:
                    card[letter].append(next_num)

            # Обновляем диапазон чисел для следующего столбца.
            lower = lower + nums_per_letter
            upper = upper + nums_per_letter

        # Преобразуем полученный словарь в список справа налево сверху вниз.
        number_list_card = []
        for i in range(0, 5):
            for k, value in card.items():
                number_list_card.append(card[k][i])

        return number_list_card

    @staticmethod
    def _check_win_line(coord_list_checks: list) -> None:
        """Проверка на выигрыш."""
        if set(coord_list_checks[0:5]) == {0}:
            pass

        if set(coord_list_checks[5:10]) == {0}:
            pass

        if set(coord_list_checks[10:15]) == {0}:
            pass

        if set(coord_list_checks[15:20]) == {0}:
            pass

        if set(coord_list_checks[20:25]) == {0}:
            pass

        if coord_list_checks[0] == 0 and coord_list_checks[6] == 0 and \
                coord_list_checks[18] == 0 and coord_list_checks[24] == 0:
            pass

        if coord_list_checks[4] == 0 and coord_list_checks[8] == 0 and \
                coord_list_checks[16] == 0 and coord_list_checks[20] == 0:
            pass

        if coord_list_checks[0] == 0 and coord_list_checks[5] == 0 and \
                coord_list_checks[10] == 0 and coord_list_checks[15] == 0 and \
                coord_list_checks[20] == 0:
            pass

        if coord_list_checks[1] == 0 and coord_list_checks[6] == 0 and \
                coord_list_checks[11] == 0 and coord_list_checks[16] == 0 and \
                coord_list_checks[21] == 0:
            pass

        if coord_list_checks[2] == 0 and coord_list_checks[7] == 0 and \
                coord_list_checks[12] == 0 and coord_list_checks[17] == 0 and \
                coord_list_checks[22] == 0:
            pass

        if coord_list_checks[3] == 0 and coord_list_checks[8] == 0 and \
                coord_list_checks[13] == 0 and coord_list_checks[18] == 0 and \
                coord_list_checks[23] == 0:
            pass

        if coord_list_checks[4] == 0 and coord_list_checks[9] == 0 and \
                coord_list_checks[14] == 0 and coord_list_checks[19] == 0 and \
                coord_list_checks[24] == 0:
            pass

        if set(coord_list_checks[0:5]) == {0} and coord_list_checks[0] == 0 \
                and coord_list_checks[6] == 0 and coord_list_checks[18] == 0 \
                and coord_list_checks[24] == 0 and coord_list_checks[0] == 0 \
                and coord_list_checks[5] == 0 and coord_list_checks[10] == 0 \
                and coord_list_checks[15] == 0 and coord_list_checks[20] == 0:
            pass

        if set(coord_list_checks[0:5]) == {0} and coord_list_checks[4] == 0 \
                and coord_list_checks[8] == 0 and coord_list_checks[16] == 0 \
                and coord_list_checks[20] == 0 and coord_list_checks[4] == 0 \
                and coord_list_checks[9] == 0 and coord_list_checks[14] == 0 \
                and coord_list_checks[19] == 0 and coord_list_checks[24] == 0:
            pass

        if set(coord_list_checks[20:25]) == {0} and coord_list_checks[0] == 0 \
                and coord_list_checks[5] == 0 and coord_list_checks[10] == 0 \
                and coord_list_checks[15] == 0 and coord_list_checks[20] == 0 \
                and coord_list_checks[4] == 0 and coord_list_checks[8] == 0 \
                and coord_list_checks[16] == 0 and coord_list_checks[20] == 0:
            pass

        if set(coord_list_checks[20:25]) == {0} and coord_list_checks[4] == 0 \
                and coord_list_checks[9] == 0 and coord_list_checks[14] == 0 \
                and coord_list_checks[19] == 0 and coord_list_checks[24] == 0 \
                and coord_list_checks[0] == 0 and coord_list_checks[6] == 0 \
                and coord_list_checks[18] == 0 and coord_list_checks[24] == 0:
            pass
