from random import choice, randrange


class Utilities:

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

    def get_list(self, mass):
        emp = []
        for i in range(3):
            for j in range(9):
                if mass[i][j] == 0:
                    num = self.get_number(i, j)
                    emp.append(num)
        return emp

    def create_coord_list_checks(self, list_of_card_numbers, coord_list_checks, pos_numbers_text):

        for i in list_of_card_numbers:
            a = list_of_card_numbers.index(i)
            if a in pos_numbers_text:
                coord_list_checks.append(i)
            else:
                coord_list_checks.append(0)

    def create_list_of_card_numbers(self):
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
        number_list_card = []
        for i in range(0, 3):
            for k, value in card.items():
                number_list_card.append(card[k][i])

        return number_list_card
