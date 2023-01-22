import pygame as pg
from settings import *


class TextCard(pg.sprite.Sprite):
    def __init__(self, text, i, j):
        super().__init__()
        self.settings = Settings()
        self.i = i
        self.j = j

        self.font = pg.font.Font(Fonts.font_text.value,
                                    Fonts.font_text_size.value)
        self.text = text
        self.number = self.font.render(self.text, True,
                                       Colors.light_blue.value,
                                       Colors.color_white.value)

        self.size_rect_x = 50
        self.size_rect_y = 50

        self.image = pg.Surface((self.size_rect_x, self.size_rect_y))
        self.image.fill(Colors.color_white.value)
        self.rect = self.image.get_rect()
        self.number_rect = self.number.get_rect(center=(25, 25))
        self.center = self.image.get_rect(center=(self.i, self.j))

        self.image.blit(self.number, self.number_rect)

    def get_text(self):
        return self.text

    def update(self):
        pg.draw.rect(self.image, Colors.red.value, (0, 0, 50, 50), 8)
