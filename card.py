import pygame as pg
from settings import Settings
from utilities import Utilities


class Card:
    def __init__(self):
        self.settings = Settings()
        self.utilities = Utilities()

        self.background_card = pg.Surface((1000, 340))
        self.background_card.fill(self.settings.light_blue)
        self.background_card_rect = self.background_card.get_rect(
            topleft=(0, 0))

        self.card_field = pg.Surface((100, 100))
        self.card_field.fill(self.settings.color_white)
        self.card_field_rect = self.card_field.get_rect(center=(50, 50))

        self.size_rect_x = 100
        self.size_rect_y = 100
        self.gap = 10

    def get_card_field(self, card_field_coord_list, surface):
        coord_list = self.utilities.get_list(card_field_coord_list)
        for i in coord_list:
            self.card_field_rect.x = \
                self.utilities.get_coords(i, self.size_rect_x,
                                          self.size_rect_y, 10,
                                          10)[0]
            self.card_field_rect.y = \
                self.utilities.get_coords(i, self.size_rect_x,
                                          self.size_rect_y, 10,
                                          10)[1]
            surface.blit(self.card_field,
                         (self.card_field_rect.x,
                          self.card_field_rect.y))
