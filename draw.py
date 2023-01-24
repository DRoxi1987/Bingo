import pygame as pg
from settings import *


class Drawer:
    @staticmethod
    def draw_text(text: str, font: str, font_size: int,
                  surface: pg.surface.Surface,
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

    @staticmethod
    def draw_field_and_text(win_game, size: Size, winner_font_rect_coord,
                            winner_field_rect_coord, surface: pg.surface.Surface):
        if win_game != "":
            Drawer.draw_rect(size,
                             surface,
                             Colors.red.value,
                             winner_field_rect_coord)

            Drawer.draw_text(win_game, Fonts.font_text.value,
                             Fonts.font_text_size.value,
                             surface,
                             Colors.color_white.value, Colors.red.value,
                             winner_font_rect_coord)

