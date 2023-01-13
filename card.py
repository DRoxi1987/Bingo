import pygame
from random import randrange, choice
from settings import Settings


class NumberCards(pygame.sprite.Sprite):
    def __init__(self, text):
        super().__init__()
        self.settings = Settings()
        self.text = text
        self.font_number = pygame.font.SysFont(self.settings.font_numbers,
                                               self.settings.font_numbers_size)
        self.image = self.font_number.render(self.text, True,
                                             self.settings.font_color)
        self.rect = self.image.get_rect(center=(62, 62))




class CardNew(pygame.sprite.Sprite):
    def __init__(self, bingo):
        super().__init__()
        self.screen = bingo.screen
        self.image = pygame.Surface((1000, 340))
        self.image.fill((70, 120, 90))
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.draw_card()

    def draw_card(self):

        self.surf_rect = pygame.Surface((100, 100))
        self.surf_rect.fill((255, 255, 255))
        self.rect_card_rect = self.surf_rect.get_rect(midleft=(10, 10))

        self.rect_card_rect.y = 10
        n = 0
        while n != 3:
            self.rect_card_rect.x = 10
            for i in range(9):
                self.image.blit(self.surf_rect, (
                    self.rect_card_rect.x, self.rect_card_rect.y))
                self.rect_card_rect.x += 110
            self.rect_card_rect.y += 110
            n += 1
