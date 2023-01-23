import pygame as pg
from settings import *
from utilities import *


class TextCard(pg.sprite.Sprite):
    def __init__(self, text, i, j):
        super().__init__()
        self.utilities = Utilities()
        self.i = i
        self.j = j
        self.size_rect_x, self.size_rect_y = Rectangle.size_rect_x, \
            Rectangle.size_rect_y

        self.font = pg.font.Font(Fonts.font_text.value,
                                 Fonts.font_text_size.value)
        self.text = text
        self.number = self.font.render(self.text, True,
                                       Colors.light_blue.value,
                                       Colors.color_white.value)

        self.size_rect_x = Rectangle.size_rect_x
        self.size_rect_y = Rectangle.size_rect_y

        self.image = pg.Surface((self.size_rect_x, self.size_rect_y))
        self.image.fill(Colors.color_white.value)
        self.rect = self.image.get_rect()
        self.number_rect = self.number.get_rect(center=(self.size_rect_x // 2,
                                                        self.size_rect_y // 2))
        self.center = self.image.get_rect(center=(self.i, self.j))

        self.image.blit(self.number, self.number_rect)

    def get_text(self):
        return self.text

    def update(self):
        pg.draw.rect(self.image, Colors.red.value, (0, 0, self.size_rect_x,
                                                    self.size_rect_y), 8)

    @staticmethod
    def get_card_numbers(i, n, pos_numbers_text, list_of_card_numbers,
                         group):
        # Генерируем спрайты класса TextCard и заполняем группу text_group.

        for j in pos_numbers_text:
            number_text = str(list_of_card_numbers[j])
            text = TextCard(number_text, i, n)
            text.rect.x = \
                Utilities.get_coords(j, Rectangle.size_rect_x,
                                     Rectangle.size_rect_y,
                                     text.center[0],
                                     text.center[1])[0]
            text.rect.y = \
                Utilities.get_coords(j, Rectangle.size_rect_x,
                                     Rectangle.size_rect_y,
                                     text.center[0],
                                     text.center[1])[1]
            group.add(text)
