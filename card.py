import pygame as pg
from settings import *
from utilities import Utilities


class Card:
    def __init__(self, x, y, i, j):
        self.settings = Settings()
        self.utilities = Utilities()

        self.card_field = pg.Surface((50, 50))
        self.card_field.fill(Colors.color_white.value)
        self.card_field_rect = self.card_field.get_rect(center=(25, 25))

        self.size_rect_x = 50
        self.size_rect_y = 50
        self.gap = 10

        self.x = x
        self.y = y
        self.i = i
        self.j = j

    def get_card_field(self, card_field_coord_list, surface):
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

    def draw_background_card(self, surface):

        self.background_card = pg.Surface((550, 190))
        self.background_card.fill(Colors.light_blue.value)
        self.background_card_rect = self.background_card.get_rect(
            topleft=(self.i, self.j))
        surface.blit(self.background_card, self.background_card_rect)