import pygame as pg
from settings import Settings


class TextCard(pg.sprite.Sprite):
    def __init__(self, text):
        super().__init__()
        self.settings = Settings()
        self.font = pg.font.SysFont(self.settings.font_numbers,
                                    self.settings.font_numbers_size)
        self.text = text
        self.number = self.font.render(self.text, True,
                                       self.settings.light_blue,
                                       self.settings.color_white)
        self.number_rect = self.number.get_rect(center=(50, 50))

        self.size_rect_x = 100
        self.size_rect_y = 100

        self.image = pg.Surface((self.size_rect_x, self.size_rect_y))
        self.image.fill(self.settings.color_white)
        self.rect = self.image.get_rect()

        self.center = self.image.get_rect(center=(60, 60))
        self.image.blit(self.number, self.number_rect)

        self.text_group = pg.sprite.Group

    def get_text(self):
        return self.text

    def update(self):
        pg.draw.rect(self.image, self.settings.red, (0, 0, 100, 100), 8)
