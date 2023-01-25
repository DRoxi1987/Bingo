import pygame as pg
import sys
from settings import *
from pouch import Pouch
from card import Card
from utilities import Utilities
from sprites import TextCard
from draw import Drawer
from sounds import Sounds
from typing import Callable


class GameLayer:
    def __init__(self):
        # Флаг запуска основного цикла слоя.
        self.state = "game"
        self.state_temp = "game"
        # Настройки фпс.
        self.clock = pg.time.Clock()
        self.fps = Screen.fps.value

        # Поверхность слоя.
        self.layer_game = pg.Surface((Screen.screen_width.value,
                                      Screen.screen_height.value))
        self.layer_game.fill(Colors.blue.value)

        # Группы спрайтов.
        self.text_group = pg.sprite.Group()
        self.text_group_enemy = pg.sprite.Group()

        # Экземпляры классов.
        self.pouch = Pouch()
        self.card = Card()
        self.card_enemy = Card()

        # Вывод проверки выигрыша.
        self.win = ""
        self.win_enemy = ""
        self.win_game = ""

        # Списки для проверки выигрыша.
        self.coord_list_checks = []
        self.coord_list_checks_enemy = []

        # Рандомные списки номеров карточек.
        self.list_of_card_numbers = Utilities.create_list_of_card_numbers()
        self.list_of_card_numbers_enemy = Utilities.create_list_of_card_numbers()

        # Номера позиций в матрице карточки для номеров.
        self.pos_numbers_text = Utilities.get_list(coord_list_base)
        print(self.pos_numbers_text)
        print(self.pos_numbers_text)
        self.pos_numbers_text_enemy = Utilities.get_list(
            coord_list_base)

        # Номера позиций в матрице карточки.
        self.pos_numbers_card_field = Utilities.get_list(
            coord_list_base)

        # Заполняем группы спрайтов спрайтами номеров.
        self._fill_the_groups()

        # Заполняем списки для проверки выигрыша.
        self._fill_coord_list_checks()

        # Заливаем фон для номеров из мешочка.
        self.pouch.draw_pouch_bg(self.layer_game)

    def _fill_the_groups(self) -> None:
        """Заполняет группы спрайтов экземплярами класс TextCard."""
        TextCard.get_card_numbers(Rectangle.size_rect_x // 2 + Rectangle.gap,
                                  Rectangle.size_rect_y // 2 + Rectangle.gap,
                                  self.pos_numbers_text,
                                  self.list_of_card_numbers,
                                  self.text_group)
        TextCard.get_card_numbers(
            Rectangle.size_rect_x // 2 + Rectangle.gap + 920,
            Rectangle.size_rect_y // 2 + Rectangle.gap,
            self.pos_numbers_text_enemy,
            self.list_of_card_numbers_enemy,
            self.text_group_enemy)

    def _fill_coord_list_checks(self) -> None:
        """Заполняет списки для проверки выигрыша."""
        Utilities.create_coord_list_checks(self.list_of_card_numbers,
                                           self.coord_list_checks,
                                           self.pos_numbers_text)

        Utilities.create_coord_list_checks(self.list_of_card_numbers_enemy,
                                           self.coord_list_checks_enemy,
                                           self.pos_numbers_text_enemy)

    def create_layer(self, screen: pg.surface.Surface) -> None:
        """Создает основной цикл слоя."""
        self.clock.tick(self.fps)

        # Помещаем основной слой.
        screen.blit(self.layer_game, (0, 0))

        # Рисуем фон карточки и номера для 1 игрока.
        self.card.draw_background_card(self.layer_game, Coords(0, 0))
        self.card.draw_card_field(self.pos_numbers_card_field,
                                  self.layer_game,
                                  Coords(10, 10))
        self.text_group.draw(self.layer_game)

        # Рисуем фон карточки и номера для 2 игрока.
        self.card_enemy.draw_background_card(self.layer_game,
                                             Coords(920, 0))
        self.card_enemy.draw_card_field(self.pos_numbers_card_field,
                                        self.layer_game,
                                        Coords(930, 10))
        self.text_group_enemy.draw(self.layer_game)

        # Функции вывода выигрышей на экран.
        Drawer.draw_field_and_text(self.win_game, Size(250, 75),
                                   (
                                       Screen.screen_width.value // 2,
                                       Screen.screen_height.value // 2),
                                   (
                                       Screen.screen_width.value // 2 - 250 // 2,
                                       Screen.screen_height.value // 2 - 75 // 2),
                                   self.layer_game
                                   )
        Drawer.draw_field_and_text(self.win,
                                   (Size(250, 75)),
                                   (Screen.screen_width.value // 2,
                                    Screen.screen_height.value // 5),
                                   (
                                       Screen.screen_width.value // 2 - 250 // 2,
                                       Screen.screen_height.value // 5 - 75 // 2),
                                   self.layer_game)
        Drawer.draw_field_and_text(self.win_enemy,
                                   (Size(250, 75)),
                                   (Screen.screen_width.value // 2,
                                    Screen.screen_height.value // 3),
                                   (
                                       Screen.screen_width.value // 2 - 250 // 2,
                                       Screen.screen_height.value // 3 - 75 // 2),
                                   self.layer_game)

        pg.display.update()

    def check_events_game(self) -> str:
        """Проверяет события"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.type == pg.QUIT:
                    sys.exit()
                elif event.key == pg.K_e:
                    self._k_e_function()
                if event.key == pg.K_ESCAPE:
                    return "home"
                else:
                    continue

    def _k_e_function(self) -> None:
        """Работа кнопки 'Е' """
        # Проигрывается звук
        Sounds.plays_sound(Track.track_pouch, Track.volume_pouch)

        # Получается рандомное число.
        ran = self.pouch.iter(self.pouch.rand_list)

        # Рисуются фон и число из мешочка.
        self.pouch.draw_pouch_bg(self.layer_game)
        self.pouch.draw_pouch_text(ran, self.layer_game)

        # Работа со списками проверки выигрыша.
        self._check_coord_list_checks(self.coord_list_checks,
                                      self.text_group,
                                      ran)
        self._check_coord_list_checks(self.coord_list_checks_enemy,
                                      self.text_group_enemy,
                                      ran)
        # Присваиваются значения выводу проверки выигрыша.
        self.win = self._check_win_line(self.coord_list_checks)
        self.win_enemy = self._check_win_line(self.coord_list_checks_enemy)

        # Проверяется выигрыш в игре.
        self._check_winner()

    def _check_win_line(self, coord_list_checks: list) -> str:
        """Проверка на выигрыш."""
        win = ""
        if set(coord_list_checks[0:5]) == {0}:
            win = "Win1"

        if set(coord_list_checks[9:18]) == {0}:
            win = "Win1"

        if set(coord_list_checks[18:27]) == {0}:
            win = "Win1"

        if set(coord_list_checks[0:9]) == {0} and set(
                self.coord_list_checks[9:18]) == {0}:
            win = "Win2"

        if set(coord_list_checks[0:9]) == {0} and set(
                self.coord_list_checks[18:27]) == {0}:
            win = "Win2"

        if set(coord_list_checks[9:18]) == {0} and set(
                coord_list_checks[18:27]) == {0}:
            win = "Win2"

        if set(coord_list_checks) == {0}:
            win = "Win3"

        return win

    def _check_winner(self) -> None:
        """Проверка выигрыша"""
        if self.win == "Win3" and self.win_enemy != "Win3":
            self.win_game = "Игрок 1"

        elif self.win_enemy == "Win3" and self.win != "Win3":
            self.win_game = "Игрок 2"

        elif self.win_enemy == "Win3" and self.win == "Win3":
            if self.win_game == "":
                self.win_game = "Ничья"

        print(self.win_game)

    @staticmethod
    def _check_coord_list_checks(coord_list: list,
                                 sprite_group: pg.sprite.Group,
                                 ran: int):
        """Проверка числа в спрайте из группы спрайтов.
        Если число в спрайте, то в списке проверки на выигрыш
        число заменяется на 0."""

        for j in coord_list:
            if ran == j:
                coord_list[
                    coord_list.index(j)] = 0
                print(coord_list)

        for i in sprite_group:
            if str(ran) == TextCard.get_text(i):
                i.update()
