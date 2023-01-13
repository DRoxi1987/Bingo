import pygame as pg
from settings import Settings


class Text(pg.sprite.Sprite):
    def __init__(self, text):
        super().__init__()
        self. settings = Settings()
        self.text = text
        self.font = pg.font.SysFont("arial", 60)
        self.image = self.font.render(self.text, True,
                                      self.settings.font_color, self.settings.color_white)
        self.rect = self.image.get_rect()
        self.center = self.image.get_rect(center=(55, 55))

    def update(self):
        pass
