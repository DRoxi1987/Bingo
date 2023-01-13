import pygame as pg


class Text(pg.sprite.Sprite):
    def __init__(self, text):
        super().__init__()
        self.text = text
        self.font = pg.font.SysFont("arial", 60)
        self.image = self.font.render(self.text, True, (0, 0, 0),
                                      (255, 255, 255))
        self.rect = self.image.get_rect()
        self.center = self.image.get_rect(center=(55, 55))

    def update(self):
        pass
