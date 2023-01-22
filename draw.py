import pygame as pg
from settings import *
from typing import NamedTuple


class Size(NamedTuple):
    width: int
    height: int


class Coords(NamedTuple):
    x: int
    y: int


class Drawer:
    @staticmethod
    def draw_text(text: str, font: str, font_size: int, surface: pg.surface.Surface,
                  color_font: Color, color_bg: Color | None,
                  coords=Coords) -> None:

        """Рисует текст на поверхности"""
        font_init = pg.font.Font(font, font_size)
        text_surf = font_init.render(text, True, color_font, color_bg)
        text_rect = text_surf.get_rect(center=coords)
        surface.blit(text_surf, text_rect)

    @staticmethod
    def draw_rect(size: Size, surface: pg.surface.Surface, color: Color,
                  coords: Coords) -> None:

        """Рисует прямоугольник на поверхности"""
        rectangle = pg.Surface(size)
        rectangle.fill(color)
        rectangle_rect = rectangle.get_rect(topleft=coords)
        surface.blit(rectangle, rectangle_rect)
