import pygame as pg
from settings import *
from utilities import Utilities
from draw import *


class Card:
    def __init__(self, x, y):
        self.utilities = Utilities()

        self.card_field = pg.Surface((Rectangle.size_rect_x, Rectangle.size_rect_y))
        self.card_field.fill(Colors.color_white.value)
        self.card_field_rect = self.card_field.get_rect(center=(Rectangle.size_rect_x // 2,
                                                                Rectangle.size_rect_y // 2))

        self.size_rect_x, self.size_rect_y = Rectangle.size_rect_x, \
            Rectangle.size_rect_y

        self.gap = 10

        self.x = x
        self.y = y

    def draw_card_field(self, jjk, surface):
        for i in jjk:
            self.card_field_rect.x = \
                self.utilities.get_coords(i, self.size_rect_x,
                                          self.size_rect_y, self.x,
                                          self.y)[0]
            self.card_field_rect.y = \
                self.utilities.get_coords(i, self.size_rect_x,
                                          self.size_rect_y, self.x,
                                          self.y)[1]
            surface.blit(self.card_field,
                         (self.card_field_rect.x,
                          self.card_field_rect.y))

    @staticmethod
    def draw_background_card(surface, coords: Coords):
        """Рисует фон карточки"""
        Drawer.draw_rect(Size(360, 360), surface,
                         Colors.light_blue.value, coords)
