from utilities import Utilities
from draw import *


class Card:
    def __init__(self):
        self.card_field = pg.Surface(
            (Rectangle.size_rect_x, Rectangle.size_rect_y))
        self.card_field.fill(Colors.color_white.value)

        self.card_field_rect = self.card_field.get_rect(
            center=(Rectangle.size_rect_x // 2,
                    Rectangle.size_rect_y // 2))

        self.size_rect_x, self.size_rect_y = Rectangle.size_rect_x, \
            Rectangle.size_rect_y
        self.image = pg.image.load("asset/72ppi/Asset 7.png").convert_alpha()
        self.image2 = pg.image.load("asset/72ppi/Asset 10.png").convert_alpha()


    @staticmethod
    def draw_background_card(surface: pg.Surface, coords: Coords):
        """Рисует фон карточки"""
        Drawer.draw_rect(Size(360, 360), surface,
                         Colors.light_blue.value, coords)
