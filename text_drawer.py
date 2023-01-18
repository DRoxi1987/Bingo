import pygame as pg


class TextDrawer:
    def __init__(self, font, font_size, color_font, color_bg, text, x, y,
                 surface):
        self.text = text
        self.font_size = font_size
        self.surface = surface
        self.font = font
        self.color_font = color_font
        self.color_bg = color_bg
        self.x = x
        self.y = y
        self.surface = surface

        self.font_init = pg.font.Font(self.font, self.font_size)
        self.text_surf = self.font_init.render(self.text, True,
                                               self.color_font, self.color_bg)
        self.text_rect = self.text_surf.get_rect(center=(self.x, self.y))

    def draw_text(self):
        self.surface.blit(self.text_surf, self.text_rect)
