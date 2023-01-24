import pygame as pg
from settings import *
from utilities import *
from draw import Drawer


class TextCard(pg.sprite.Sprite):
    def __init__(self, text, coords: Coords):
        super().__init__()

        self.x, self.y = coords

        self.size_rect_x, self.size_rect_y = Rectangle.size_rect_x, \
            Rectangle.size_rect_y

        self.text = text

        self.image = pg.Surface((self.size_rect_x, self.size_rect_y))
        self.image.fill(Colors.color_white.value)
        self.rect = self.image.get_rect()
        self.center = self.image.get_rect(center=(self.x, self.y))

        Drawer.draw_text(self.text, Fonts.font_text.value,
                         Fonts.font_text_size.value, self.image,
                         Colors.light_blue.value,
                         Colors.color_white.value,
                         (self.size_rect_x // 2,
                          self.size_rect_y // 2+3))

    def get_text(self) -> str:
        return self.text

    def update(self) -> None:
        pg.draw.rect(self.image, Colors.red.value, (0, 0, self.size_rect_x,
                                                    self.size_rect_y), 8)

    @staticmethod
    def get_card_numbers(x: Coords.x, y: Coords.y,
                         pos_numbers_text,
                         list_of_card_numbers: list,
                         group: pg.sprite.Group) -> None:
        """Генерируем спрайты класса TextCard и заполняем группу text_group"""

        for j in pos_numbers_text:
            number_text = str(list_of_card_numbers[j])
            text: TextCard = TextCard(number_text, Coords(x, y))
            text.rect.x = \
                Utilities.get_coords(j, Rectangle.size_rect_x,
                                     Rectangle.size_rect_y,
                                     Coords(text.center[0],
                                            text.center[1]))[0]
            text.rect.y = \
                Utilities.get_coords(j, Rectangle.size_rect_x,
                                     Rectangle.size_rect_y,
                                     Coords(text.center[0],
                                            text.center[1]))[1]
            group.add(text)
