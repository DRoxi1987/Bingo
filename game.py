import pygame as pg
import sys
from random import choice
from text import Text
from settings import Settings


class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.screen = pg.display.set_mode((1200, 720))
        self.clock = pg.time.Clock()
        self.fps = self.settings.fps
        self.clock.tick(30)
        self.size_rect_x = 100
        self.size_rect_y = 100
        self.home_coord_list = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

        self.coord_list = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.choice_list(self.coord_list)
        self.rectangle = pg.Surface((self.size_rect_x, self.size_rect_y))
        self.rectangle.fill((255, 255, 255))
        self.rect_rectangle = self.rectangle.get_rect()
        self.pos_numbers_rectangle = self.get_list(self.home_coord_list)
        self.pos_numbers_text = self.get_list(self.coord_list)
        self.text_group = pg.sprite.Group()
        self.s = [0, 1, 2, 3, 99, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                  17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

    def get_list(self, mass):
        emp = []
        for i in range(3):
            for j in range(9):
                if mass[i][j] == 0:
                    num = self.get_number(i, j)
                    emp.append(num)
        return emp

    def get_number(self, m, n):
        return m * 9 + n

    def get_pos(self, num):
        return num // 9, num % 9

    def choice_list(self, mas):
        for i in mas:
            random_number = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            for j in range(4):
                t = choice(random_number)
                random_number.remove(t)
                i[t] = 1

    def get_coords(self, number, m, n, x0, y0):
        y = self.get_pos(number)[0]
        x = self.get_pos(number)[1]
        gap = 10

        x_pos = x0 + (m + gap) * x
        y_pos = y0 + (n + gap) * y
        return x_pos, y_pos

    def run_game(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            self.text_group.draw(self.screen)
            pg.display.update()

            for i in self.pos_numbers_rectangle:
                self.rect_rectangle.x = \
                    self.get_coords(i, self.size_rect_x, self.size_rect_y, 10,
                                    10)[0]
                self.rect_rectangle.y = \
                    self.get_coords(i, self.size_rect_x, self.size_rect_y, 10,
                                    10)[1]
                self.screen.blit(self.rectangle,
                                 (self.rect_rectangle.x,
                                  self.rect_rectangle.y))

                for j in self.pos_numbers_text:
                    number_text = str(self.s[j])
                    text = Text(number_text)
                    text.rect.x = \
                        self.get_coords(j, self.size_rect_x, self.size_rect_y,
                                        text.center[0],
                                        text.center[1])[0] + 3
                    text.rect.y = \
                        self.get_coords(j, self.size_rect_x, self.size_rect_y,
                                        text.center[0],
                                        text.center[1])[1] + 4

                    self.text_group.add(text)


if __name__ == '__main__':
    game = Game()
    game.run_game()
