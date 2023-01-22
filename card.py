import pygame as pg
from settings import *
from utilities import Utilities
from draw import *


class Card:
    def __init__(self, x, y):
        self.settings = Settings()
        self.utilities = Utilities()

        self.card_field = pg.Surface((50, 50))
        self.card_field.fill(Colors.color_white.value)
        self.card_field_rect = self.card_field.get_rect(center=(25, 25))

        self.size_rect_x, self.size_rect_y = Rectangle.size_rect_x, \
            Rectangle.size_rect_y

        self.gap = 10

        self.x = x
        self.y = y

    def draw_card_field(self, card_field_coord_list, surface):
        coord_list = self.utilities.get_list(card_field_coord_list)
        for i in coord_list:
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
        Drawer.draw_rect(Size(550, 190), surface,
                         Colors.light_blue.value, coords)
