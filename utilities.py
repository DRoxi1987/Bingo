from random import randrange
from settings import Rectangle

class Utilities:
    @staticmethod
    def get_number(m, n):
        return m * 5 + n

    @staticmethod
    def get_pos(num):
        return num // 5, num % 5

    @staticmethod
    def get_coords(number, m, n, x0, y0):

        y = Utilities.get_pos(number)[0]
        x = Utilities.get_pos(number)[1]
        gap = Rectangle.gap

        x_pos = x0 + (m + gap) * x
        y_pos = y0 + (n + gap) * y
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
    def create_coord_list_checks(list_of_card_numbers, coord_list_checks,
                                 pos_numbers_text):

        for i in list_of_card_numbers:
            a = list_of_card_numbers.index(i)
            if a in pos_numbers_text:
                coord_list_checks.append(i)
            else:
                coord_list_checks.append(0)

    @staticmethod
    def create_list_of_card_numbers():
        nums_per_letter = 15
        # Создаем рандомную карточку БИНГО из 3 строк и 9 столбцов.

        card = {}  # Создаем пустой словарь под будущую карточку.

        # Верхний диапазон целых чисел, для генератора чисел в карточке.
        lower = 1

        # Нижний диапазон целых чисел, для генератора чисел в карточке.
        upper = 1 + nums_per_letter

        # Генератор чисел, заполняющий всю карточку числами. В первом столбце числа.
        # от 1 до 10. Во втором от 11 до 20. И так далее до 9 ряда от 81 до 90.

        for letter in range(1, 6):  # Для диапазона от 0 до 9.
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
        print(card)
        # Преобразуем полученный словарь в список справа налево сверху вниз.
        number_list_card = []
        for i in range(0, 5):
            for k, value in card.items():
                number_list_card.append(card[k][i])

        return number_list_card
