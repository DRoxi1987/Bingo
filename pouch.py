from random import choice
from draw import *


class Pouch:
    def __init__(self):
        self.surface = pg.Surface((225, 150))
        self.rect = self.surface.get_rect(
            center=(Screen.screen_width.value // 2,
                    Screen.screen_height.value - 125))

        self.image_bg = pg.image.load(
            "asset/72ppi/Asset 12.png").convert_alpha()
        self.image_bg_scale = pg.transform.smoothscale(self.image_bg,
                                                       (self.image_bg.get_width() * 1.5,
                                                       self.image_bg.get_height()))

        # Пустой список для заполнения числами от 1 до 90 по порядку
        # (функция create_rand_list(self)) и рандомного вытаскивания числа из
        # списка и последующего его удаления (функция iter(self)).
        self.rand_list = []

        # Переменная, получающая в функции draw_pouch(self) результат работы
        # iter(self).
        self.number = None

        # Переменная, получающая Rect от текстовой поверхности, полученной в
        # функции draw_pouch(self).

        self.number_rect = None

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

    def draw_pouch_bg(self, layer):

        layer.blit(self.image_bg_scale,
                   (Screen.screen_width.value // 2 - 225 // 2,
                    Screen.screen_height.value - 200))

    @staticmethod
    def draw_pouch_text(ran, layer):
        """Отрисовывает на поверхности layer число."""

        Drawer.draw_text(str(ran), Fonts.font_text3.value, 90, layer,
                         Colors.pink.value,
                         None, Coords(Screen.screen_width.value // 2 + 3,
                                      Screen.screen_height.value - 120))

    @staticmethod
    def get_letter(ran):
        list_check = [n for n in range(1, 76)]
        if ran in list_check[0:15]:
            return "B"
        elif ran in list_check[15:30]:
            return "I"
        elif ran in list_check[30:45]:
            return "N"
        elif ran in list_check[45:60]:
            return "G"
        elif ran in list_check[60:75]:
            return "O"
        else:
            return ""
