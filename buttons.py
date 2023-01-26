import pygame as pg
from settings import *


class Button:
    def __init__(self, image: str, image_pr: str, image_cl: str,
                 coords: Coords):
        self.image = pg.image.load(image).convert_alpha()
        self.image_initial = pg.image.load(image).convert_alpha()
        self.rect = self.image.get_rect(center=coords)

        self.image_pr = pg.image.load(image_pr).convert_alpha()
        self.image_cl = pg.image.load(image_cl).convert_alpha()

    def button_blit(self, surface):
        surface.blit(self.image, self.rect)
