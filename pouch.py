import pygame
from random import choice
from settings import Settings


class Pouch:
    def __init__(self, bingo):
        self.screen = bingo.screen
        self.settings = Settings()

        # Пустой список для заполнения числами от 1 до 90 по порядку (
        # функция create_rand_list(self)) и рандомного вытаскивания числа из
        # списка и последующего его удаления (функция iter(self).
        self.rand_list = []

        # Поверхность фон для отрисовки чисел из бочонка.
        self.surface_pouch = pygame.Surface((220, 220))
        self.surface_pouch.fill(self.settings.font_background_color)
        self.surface_pouch_rect = self.surface_pouch.get_rect(
            center=(self.settings.screen_width - 230,
                    self.settings.screen_height - 230))

        # Шрифт для отображения чисел из бочонка
        self.font_pouch = pygame.font.SysFont(self.settings.font_numbers,
                                              80)
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
        for i in range(1, 90):
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
            return "Бочонки закончились"

    def draw_pouch(self, ran, layer):
        # Отрисовывает на поверхности screen фон для числа бочонка и само
        # число.

        # Фон
        layer.blit(self.surface_pouch, self.surface_pouch_rect.center)
        # Получаем поверхность со случайным числом из iter(self).
        self.number = self.font_pouch.render(str(ran), True,
                                             self.settings.font_color)
        # Получаем rect для поверхности.
        self.number_rect = self.number.get_rect(
            center=(self.settings.screen_width - 115,
                    self.settings.screen_height - 115))

        # Отрисовка числа в нужных координатах.
        layer.blit(self.number, self.number_rect)
