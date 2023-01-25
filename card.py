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

    def draw_card_field(self, pos_numbers: list, surface: pg.surface.Surface,
                        start_coordinates: Coords):
        """Рисует на поверхности фоновые квадраты карточки по вычисленным
        координатам изначальной матрицы"""
        for i in pos_numbers:
            self.card_field_rect.x = \
                Utilities.get_coords(i, self.size_rect_x,
                                     self.size_rect_y, start_coordinates)[0]
            self.card_field_rect.y = \
                Utilities.get_coords(i, self.size_rect_x,
                                     self.size_rect_y, start_coordinates)[1]
            surface.blit(self.card_field,
                         (self.card_field_rect.x,
                          self.card_field_rect.y))

    @staticmethod
    def draw_background_card(surface: pg.Surface, coords: Coords):
        """Рисует фон карточки"""
        Drawer.draw_rect(Size(360, 360), surface,
                         Colors.light_blue.value, coords)
