import pygame
from random import choice
from settings import Settings


class Pouch:
    def __init__(self, bingo):

        self.screen = bingo.screen
        self.settings = Settings()
        self.rand_list = []
        self.create_rand_list()
        self.surface_pouch = pygame.Surface((220, 220))
        self.surface_pouch.fill(self.settings.font_background_color)
        self.surface_pouch_rect = self.surface_pouch.get_rect(
            center=(self.settings.screen_width - 230,
                    self.settings.screen_height - 230))
        self.font_pouch = pygame.font.SysFont(self.settings.font_numbers,
                                              80)
        self.number = None
        self.number_rect = None

    def create_rand_list(self):
        for i in range(1, 90):
            self.rand_list.append(i)

    def iter(self):

        if self.rand_list:
            ran = choice(self.rand_list)
            if ran in self.rand_list:
                self.rand_list.remove(ran)
                return ran
        else:
            return "Бочонки закончились"

    def draw_pouch(self):
        self.screen.blit(self.surface_pouch, self.surface_pouch_rect.center)
        self.number = self.font_pouch.render(str(self.iter()), True,
                                             self.settings.font_color)
        self.number_rect = self.number.get_rect(
            center=(self.settings.screen_width - 115,
                    self.settings.screen_height - 115))
        self.screen.blit(self.number, self.number_rect)
