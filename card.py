import pygame
from random import randrange, choice
from settings import Settings


class NumberCards(pygame.sprite.Sprite):
    def __init__(self, bingo):
        super().__init__()
        self.screen = bingo.screen
        self.settings = Settings()
        self.font_number = pygame.font.SysFont(self.settings.font_numbers,
                                               self.settings.font_numbers_size)
        self.image = pygame.Surface((1000, 340))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.split_horizontal_card = self.create_card()
        self.test()
        self.draw_numbers()

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
        split_horizontal_card_base = [horizontal_line[0:9],
                                      horizontal_line[9: 18],
                                      horizontal_line[18:28]]

        # Заменяем 4 рандомных числа в каждой строке карточки на 0.
        for i in split_horizontal_card_base:
            random_number = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # Список для функции
            # choice.
            for k in range(0, 4):
                t = choice(random_number)  # Выбираем из списка random_number 4
                # случайных числа.
                random_number.remove(t)  # Удаляем выбранное число из списка
                i[t] = 0  # Заменяем число по рандомной позиции t в строке
                # на 0.
        split_horizontal_card = split_horizontal_card_base[0] + \
                                split_horizontal_card_base[1] + \
                                split_horizontal_card_base[2]

        print(split_horizontal_card)
        return split_horizontal_card

    def draw_numbers(self):
        x = 62
        y = 62
        flag = 0
        for i in self.test():
            if i != None:
                self.image.blit(i, i.get_rect(center=(x, y)))
                x += 110
                flag += 1
                if flag >= 9:
                    flag = 0
                    x = 62
                    y += 110
            else:
                x += 110
                flag += 1
                if flag >= 9:
                    flag = 0
                    x = 62
                    y += 110

    def test(self):
        j = []
        for i in self.split_horizontal_card:
            print(i)
            if i:

                font_surface = self.font_number.render(str(i), True,
                                                       self.settings.font_color)

                print(font_surface)
                j.append(font_surface)
            else:
                j.append(None)
        return j


class CardNew(pygame.sprite.Sprite):
    def __init__(self, bingo):
        super().__init__()
        self.screen = bingo.screen
        self.image = pygame.Surface((1000, 340))
        self.image.fill((70, 120, 90))
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.draw_card()

    def draw_card(self):

        self.surf_rect = pygame.Surface((100, 100))
        self.surf_rect.fill((255, 255, 255))
        self.rect_card_rect = self.surf_rect.get_rect(midleft=(10, 10))

        self.rect_card_rect.y = 10
        n = 0
        while n != 3:
            self.rect_card_rect.x = 10
            for i in range(9):
                self.image.blit(self.surf_rect, (
                    self.rect_card_rect.x, self.rect_card_rect.y))
                self.rect_card_rect.x += 110
            self.rect_card_rect.y += 110
            n += 1
