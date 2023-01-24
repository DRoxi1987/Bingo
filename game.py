import pygame as pg
import sys
from sprites import *
from settings import *
from pouch import Pouch
from card import Card
from utilities import *
from draw import *
from sounds import Sounds
from layers import *
from events import *


class Game:
    def __init__(self):
        pg.init()
        # Название окна.
        pg.display.set_caption(Screen.set_caption.value)

        # Экземпляры классов.

        self.pouch = Pouch()
        self.card = Card()
        self.card2 = Card()

        # Настройка основного окна.
        self.screen_coord = (Screen.screen_width.value,
                             Screen.screen_height.value)
        self.screen = pg.display.set_mode(self.screen_coord)
        self.screen.fill(Colors.blue.value)

        # Слои
        self.layer_game = pg.Surface(self.screen_coord)
        self.layer_game.fill(Colors.blue.value)

        # Настройка FPS
        self.clock = pg.time.Clock()
        self.fps = Screen.fps.value

        # Размеры квадратов, для размещения номеров карточки.
        self.size_rect_x, self.size_rect_y = Rectangle.size_rect_x, \
            Rectangle.size_rect_y

        # Базовая карточка со всеми нулями
        self.card_field_coord_list = coord_list_base

        # Список для проверки выигрыша игрока.
        # Простой список, где пустые места карточки заменены 0,
        # а остальные цифры оставлены на своих местах.
        self.coord_list_checks = []
        self.coord_list_checks_enemy = []
        print(self.coord_list_checks)
        # Флаг выигрыша игрока.
        self.win = ""
        self.win_enemy = ""
        self.win_game = ""

        # Список позиций 0-26, для фоновых квадратов карточки.
        self.pos_numbers_card_field = Utilities.get_list(
            coord_list_base)

        # Список позиций 0-26, для спрайтов с номерами.
        self.pos_numbers_text = Utilities.get_list(coord_list_base)
        print(self.pos_numbers_text)
        self.pos_numbers_text_enemy = Utilities.get_list(
            coord_list_base)
        print(self.pos_numbers_text_enemy)

        # Группы спрайтов
        self.text_group = pg.sprite.Group()
        self.text_group_enemy = pg.sprite.Group()

        # Основной список номеров для карточки.
        self.list_of_card_numbers = Utilities.create_list_of_card_numbers()
        self.list_of_card_numbers_enemy = Utilities.create_list_of_card_numbers()

        # Заполняем группы спрайтов.
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

        # Заполняем список coord_list_checks.
        Utilities.create_coord_list_checks(self.list_of_card_numbers,
                                           self.coord_list_checks,
                                           self.pos_numbers_text)

        Utilities.create_coord_list_checks(
            self.list_of_card_numbers_enemy,
            self.coord_list_checks_enemy,
            self.pos_numbers_text_enemy)

        self.pouch.draw_pouch_bg(self.layer_game)

    def win_check(self, coord_list_checks):
        # Проверка на выигрыш.
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

    @staticmethod
    def check_coord_list_checks(coord_list, sprite_group, ran):
        for j in coord_list:
            if ran == j:
                coord_list[
                    coord_list.index(j)] = 0
                print(coord_list)

        for i in sprite_group:
            if str(ran) == TextCard.get_text(i):
                i.update()

    def check_events_game(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.type == pg.QUIT:
                    sys.exit()
                elif event.key == pg.K_ESCAPE:
                    self.run_game()
                elif event.key == pg.K_e:
                    self.k_e_function()

    def k_e_function(self):
        Sounds.plays_sound(Track.track_pouch, Track.volume_pouch)
        ran = self.pouch.iter(self.pouch.rand_list)
        print(ran)
        print(self.win)
        self.pouch.draw_pouch_bg(self.layer_game)
        self.pouch.draw_pouch_text(ran, self.layer_game)
        self.check_coord_list_checks(self.coord_list_checks,
                                     self.text_group,
                                     ran)
        self.check_coord_list_checks(self.coord_list_checks_enemy,
                                     self.text_group_enemy,
                                     ran)
        self.win = self.win_check(self.coord_list_checks)
        self.win_enemy = self.win_check(
            self.coord_list_checks_enemy)

        if self.win == "Win3" and self.win_enemy != "Win3":
            self.win_game = "Игрок 1"

        elif self.win_enemy == "Win3" and self.win != "Win3":
            self.win_game = "Игрок 2"

        elif self.win_enemy == "Win3" and self.win == "Win3":
            if self.win_game == "":
                self.win_game = "Ничья"

        print(self.win_game)

    def run_layer_screen_game(self):
        running = True
        while running:
            self.clock.tick(30)
            self.check_events_game()
            self.screen.blit(self.layer_game, (0, 0))

            self.card.draw_background_card(self.layer_game, Coords(0, 0))
            self.card.draw_card_field(self.pos_numbers_card_field,
                                      self.layer_game, Coords(10, 10))
            self.text_group.draw(self.layer_game)
            self.card2.draw_background_card(self.layer_game, Coords(920, 0))
            self.card2.draw_card_field(self.pos_numbers_card_field,
                                       self.layer_game, Coords(930, 10))
            self.text_group_enemy.draw(self.layer_game)
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

    def check_events_home(self, running):

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
                    pg.quit()
                    sys.exit()
                elif event.key == pg.K_SPACE:
                    running = False
                    self.run_layer_screen_game()

    def run_game(self):
        run = RunGame(self.run_layer_screen_game)
        run.create_layer(self.clock,
                         run.check_events_home,
                         self.screen)
