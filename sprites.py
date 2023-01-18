import pygame as pg
from settings import Settings


class TextCard(pg.sprite.Sprite):
    def __init__(self, text, i, j):
        super().__init__()
        self.settings = Settings()
        self.i = i
        self.j = j

        self.font = pg.font.Font(self.settings.font_numbers,
                                    self.settings.font_numbers_size)
        self.text = text
        self.number = self.font.render(self.text, True,
                                       self.settings.light_blue,
                                       self.settings.color_white)

        self.size_rect_x = 50
        self.size_rect_y = 50

        self.image = pg.Surface((self.size_rect_x, self.size_rect_y))
        self.image.fill(self.settings.color_white)
        self.rect = self.image.get_rect()
        self.number_rect = self.number.get_rect(center=(25, 25))
        self.center = self.image.get_rect(center=(self.i, self.j))

        self.image.blit(self.number, self.number_rect)

    def get_text(self):
        return self.text

    def update(self):
        pg.draw.rect(self.image, self.settings.red, (0, 0, 50, 50), 8)
