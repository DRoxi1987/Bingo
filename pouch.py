import pygame
from random import choice
from settings import *
from draw import *


class Pouch:
    def __init__(self):
        self.surface = pg.Surface((150, 150))
        self.rect = self.surface.get_rect(
            center=(Screen.screen_width.value // 2,
                    Screen.screen_height.value - 125))
        # Пустой список для заполнения числами от 1 до 90 по порядку (
        # функция create_rand_list(self)) и рандомного вытаскивания числа из
        # списка и последующего его удаления (функция iter(self)).
        self.rand_list = []

        # Переменная, получающая в функции draw_pouch(self) результат работы
        # iter(self).
        self.number = None

        # Переменная, получающая Rect от текстовой поверхности, полученной в
        # функции draw_pouch(self).

        self.number_rect = None

        # Функция create_rand_list(self) вызывается сразу при создании
        # объекта класса и заполняет список self.rand_list.
        self.create_rand_list()

    # Заполняет список rand_list значениями от 1 до 90 подряд.
    def create_rand_list(self):
        for i in range(1, 76):
            self.rand_list.append(i)

    def iter(self, rand_list):
        # Возвращает из списка rand_list случайное число и удаляет его из
        # списка. Если список пуст, возвращает строку "Бочонки закончились".

        if rand_list:
            ran = choice(self.rand_list)
            # Проверка. Если число в списке, то мы его удаляем.
            if ran in self.rand_list:
                self.rand_list.remove(ran)
                return ran
        else:
            return "X"

    @staticmethod
    def draw_pouch_bg(layer):
        Drawer.draw_rect(Size(150, 150), layer, Colors.color_white.value,
                         Coords(Screen.screen_width.value // 2 - 75,
                                Screen.screen_height.value - 200))

    @staticmethod
    def draw_pouch_text(ran, layer):
        """Отрисовывает на поверхности layer число."""

        Drawer.draw_text(str(ran), Fonts.font_text.value, 100, layer,
                         Colors.red.value,
                         None, Coords(Screen.screen_width.value // 2 + 5,
                                      Screen.screen_height.value - 120))
