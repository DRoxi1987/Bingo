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
    def __init__(self, surface):
        # Флаг запуска основного цикла слоя.
        self.screen = surface
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
        self.win = "Win"
        self.win_enemy = ""
        self.win_game = ""

        # Рандомные списки номеров карточек.
        self.list_of_card_numbers = []
        self.list_of_card_numbers_enemy = []

        # Номера позиций в матрице карточки для номеров.
        self.pos_numbers_text = None
        self.pos_numbers_text_enemy = None

        # Номера позиций в матрице карточки.
        self.pos_numbers_card_field = Utilities.get_list(
            coord_list_base)

        # Списки для проверки выигрыша.
        self.coord_list_checks = []
        self.coord_list_checks_enemy = []

        # Заполняем все списки
        self.get_all()

    def get_all(self):

        self.list_of_card_numbers = Utilities.create_list_of_card_numbers()
        self.list_of_card_numbers_enemy = Utilities.create_list_of_card_numbers()
        self.get_pos_numbers_text()
        self._fill_coord_list_checks()
        self.pouch.create_rand_list()
        self._fill_the_groups()
        self.pouch.draw_pouch_bg(self.layer_game)

    def get_pos_numbers_text(self):
        self.pos_numbers_text = None
        self.pos_numbers_text = Utilities.get_list(coord_list_base)

        self.pos_numbers_text_enemy = None
        self.pos_numbers_text_enemy = Utilities.get_list(
            coord_list_base)

    def get_list_of_card_numbers(self):
        self.list_of_card_numbers = Utilities.create_list_of_card_numbers()
        self.list_of_card_numbers_enemy = Utilities.create_list_of_card_numbers()

    def _fill_the_groups(self) -> None:
        """Заполняет группы спрайтов экземплярами класс TextCard."""
        TextCard.get_card_numbers(
            Rectangle.size_rect_x // 2 + Rectangle.gap + 4,
            Rectangle.size_rect_y // 2 + Rectangle.gap + 80,
            self.pos_numbers_text,
            self.list_of_card_numbers,
            self.text_group)
        TextCard.get_card_numbers(
            Rectangle.size_rect_x // 2 + Rectangle.gap + 920 - 6,
            Rectangle.size_rect_y // 2 + Rectangle.gap + 80,
            self.pos_numbers_text_enemy,
            self.list_of_card_numbers_enemy,
            self.text_group_enemy)

    def _fill_coord_list_checks(self) -> None:
        """Заполняет списки для проверки выигрыша."""
        self.coord_list_checks = []
        Utilities.create_coord_list_checks(self.list_of_card_numbers,
                                           self.coord_list_checks,
                                           self.pos_numbers_text)
        self.coord_list_checks_enemy = []
        Utilities.create_coord_list_checks(self.list_of_card_numbers_enemy,
                                           self.coord_list_checks_enemy,
                                           self.pos_numbers_text_enemy)

    def create_layer(self) -> None:
        """Создает основной цикл слоя."""
        self.clock.tick(self.fps)

        # Помещаем основной слой.
        self.screen.blit(self.layer_game, (0, 0))
        # self.layer_game.blit(self.image_bg, (0, 0))

        # Рисуем фон карточки и номера для 1 игрока.

        self.layer_game.blit(self.card.image, (0, 0))
        self.text_group.draw(self.layer_game)

        # Рисуем фон карточки и номера для 2 игрока.
        self.layer_game.blit(self.card.image2, (910, 0))

        # self.card_enemy.draw_card_field(self.pos_numbers_card_field,
        #                                 self.layer_game,
        #                                 Coords(930, 10))
        self.text_group_enemy.draw(self.layer_game)

        pg.display.update()

    def check_events_game(self) -> str:
        """Проверяет события"""
        mouse_pos = pg.mouse.get_pos()

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
                    self.layer_game.fill(Colors.blue.value)
                    return "home"
                else:
                    continue
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and \
                    self.pouch.rect.collidepoint(
                        mouse_pos):
                self._k_e_function()

    def _k_e_function(self) -> None:
        """Работа кнопки 'Е' """
        # Проигрывается звук
        Sounds.plays_sound(Track.track_pouch, Track.volume_pouch)

        # Получается рандомное число.
        ran = self.pouch.iter(self.pouch.rand_list)
        letter = self.pouch.get_letter(ran)

        # Рисуются фон и число из мешочка.
        self.pouch.draw_pouch_bg(self.layer_game)
        self.pouch.draw_pouch_text(f"{letter}  {ran}", self.layer_game)

        # Работа со списками проверки выигрыша.
        self._check_coord_list_checks(self.coord_list_checks,
                                      self.text_group,
                                      ran)

        self._check_coord_list_checks(self.coord_list_checks_enemy,
                                      self.text_group_enemy,
                                      ran)

    @staticmethod
    def _check_win_line(self, coord_list_checks: list) -> None:
        """Проверка на выигрыш."""
        if set(coord_list_checks[0:5]) == {0}:
            pass

        if set(coord_list_checks[5:10]) == {0}:
            pass

        if set(coord_list_checks[10:15]) == {0}:
            pass

        if set(coord_list_checks[15:20]) == {0}:
            pass

        if set(coord_list_checks[20:25]) == {0}:
            pass

        if coord_list_checks[0] == 0 and coord_list_checks[6] == 0 and \
                coord_list_checks[18] == 0 and coord_list_checks[24] == 0:
            pass

        if coord_list_checks[4] == 0 and coord_list_checks[8] == 0 and \
                coord_list_checks[16] == 0 and coord_list_checks[20] == 0:
            pass

        if coord_list_checks[0] == 0 and coord_list_checks[5] == 0 and \
                coord_list_checks[10] == 0 and coord_list_checks[15] == 0 and \
                coord_list_checks[20] == 0:
            pass

        if coord_list_checks[1] == 0 and coord_list_checks[6] == 0 and \
                coord_list_checks[11] == 0 and coord_list_checks[16] == 0 and \
                coord_list_checks[21] == 0:
            pass

        if coord_list_checks[2] == 0 and coord_list_checks[7] == 0 and \
                coord_list_checks[12] == 0 and coord_list_checks[17] == 0 and \
                coord_list_checks[22] == 0:
            pass

        if coord_list_checks[3] == 0 and coord_list_checks[8] == 0 and \
                coord_list_checks[13] == 0 and coord_list_checks[18] == 0 and \
                coord_list_checks[23] == 0:
            pass

        if coord_list_checks[4] == 0 and coord_list_checks[9] == 0 and \
                coord_list_checks[14] == 0 and coord_list_checks[19] == 0 and \
                coord_list_checks[24] == 0:
            pass

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

        for i in sprite_group:
            if str(ran) == TextCard.get_text(i):
                i.update()
