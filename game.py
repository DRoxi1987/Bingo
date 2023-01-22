import pygame as pg
import sys
from sprites import TextCard
from settings import *
from pouch import Pouch
from card import Card
from utilities import Utilities


class Game:
    def __init__(self):
        pg.init()
        # Название окна.
        pg.display.set_caption(Screen.set_caption.value)

        # Экземпляры классов.
        self.settings = Settings()
        self.pouch = Pouch()
        self.card = Card(10, 10, 0, 0)
        self.card2 = Card(740, 10, 730, 0)
        self.utilities = Utilities()

        # Настройка основного окна.
        self.screen = pg.display.set_mode(
            (Screen.screen_width.value,
             Screen.screen_height.value))
        self.screen.fill(Colors.blue.value)

        self.s = pg.mixer.Sound("sound/pouch.mp3")
        self.s.set_volume(0.2)
        self.layer_game = pg.Surface((Screen.screen_width.value,
                                      Screen.screen_height.value))
        self.layer_game.fill(Colors.blue.value)
        # Настройка FPS
        self.clock = pg.time.Clock()
        self.fps = Screen.fps.value

        # Размеры квадратов, для размещения номеров карточки.
        self.size_rect_x = 50
        self.size_rect_y = 50

        self.home_screen_font = pg.font.Font(Fonts.font_text.value, 250)
        self.home_screen_font_surf = self.home_screen_font.render("Bingo!",
                                                                  True,
                                                                  Colors.red.value)
        self.home_screen_font_rect = self.home_screen_font_surf.get_rect(
            center=(
                Screen.screen_width.value // 2,
                Screen.screen_height.value // 3))
        self.home_screen_font1 = pg.font.Font(Fonts.font_text.value, 60)
        self.home_screen_font1_surf = self.home_screen_font1.render(
            "Нажмите на пробел, чтобы начать!",
            True,
            Colors.color_white.value)
        self.home_screen_font1_rect = self.home_screen_font1_surf.get_rect(
            center=(
                Screen.screen_width.value // 2,
                Screen.screen_height.value // 2 + 100))

        # Базовая карточка со всеми нулями
        self.card_field_coord_list = self.settings.coord_list

        # Карточка с рандомными единицами
        self.coord_list = self.utilities.choice_list()
        self.coord_list_enemy = self.utilities.choice_list()

        # Список для проверки выигрыша игрока.
        # Простой список, где пустые места карточки заменены 0,
        # а остальные цифры оставлены на своих местах.
        self.coord_list_checks = []
        self.coord_list_checks_enemy = []

        # Флаг выигрыша игрока.
        self.win = ""
        self.win_enemy = ""
        self.win_game = ""

        # Список позиций 0-26, для фоновых квадратов карточки.
        self.pos_numbers_card_field = self.utilities.get_list(
            self.card_field_coord_list)

        # Список позиций 0-26, для спрайтов с номерами.
        self.pos_numbers_text = self.utilities.get_list(self.coord_list)
        print(self.pos_numbers_text)
        self.pos_numbers_text_enemy = self.utilities.get_list(
            self.coord_list_enemy)
        print(self.pos_numbers_text_enemy)
        # Группы спрайтов
        self.text_group = pg.sprite.Group()
        self.text_group1 = pg.sprite.Group()

        # Основной список номеров для карточки.
        self.list_of_card_numbers = self.utilities.create_list_of_card_numbers()
        self.list_of_card_numbers_enemy = self.utilities.create_list_of_card_numbers()

        # Заполняем группу спрайтов text_group.
        self.get_card_numbers(35, 35, self.pos_numbers_text,
                              self.list_of_card_numbers, self.text_group)
        self.get_card_numbers(765, 35, self.pos_numbers_text_enemy,
                              self.list_of_card_numbers_enemy,
                              self.text_group1)

        # Заполняем список coord_list_checks.
        self.utilities.create_coord_list_checks(self.list_of_card_numbers,
                                                self.coord_list_checks,
                                                self.pos_numbers_text)

        self.utilities.create_coord_list_checks(
            self.list_of_card_numbers_enemy,
            self.coord_list_checks_enemy,
            self.pos_numbers_text_enemy)

    def draw_winner(self, win_game, winner_font_rect_coord,
                    winner_field_rect_coord):

        if win_game != "":
            win_font = pg.font.Font(Fonts.font_text.value, Fonts.font_text_size.value)
            text = win_game
            win_font_surface = win_font.render(text, True,
                                               Colors.color_white.value,
                                               Colors.red.value)

            winner_field = pg.Surface((250, 75))
            winner_font_rect = win_font_surface.get_rect(
                center=winner_font_rect_coord)
            win_field_rect = winner_field.get_rect(
                center=winner_field_rect_coord)
            winner_field.fill(Colors.red.value)
            self.screen.blit(winner_field, win_field_rect)
            self.screen.blit(win_font_surface, winner_font_rect)

    def draw_win_field(self, win_field, win_font_rect_coord,
                       win_field_rect_coord):
        if win_field != "":
            win_font = pg.font.Font(Fonts.font_text.value, Fonts.font_text_size.value)
            text = win_field
            win_font_surface = win_font.render(text, True,
                                               Colors.color_white.value,
                                               Colors.red.value)

            win_field = pg.Surface((250, 75))
            win_font_rect = win_font_surface.get_rect(
                center=win_font_rect_coord)
            win_field_rect = win_field.get_rect(center=win_field_rect_coord)
            win_field.fill(Colors.red.value)
            self.screen.blit(win_field, win_field_rect)
            self.screen.blit(win_font_surface, win_font_rect)

    def win_check(self, coord_list_checks):
        # Проверка на выигрыш.
        win = ""
        if set(coord_list_checks[0:9]) == {0}:
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

    def get_card_numbers(self, i, n, pos_numbers_text, list_of_card_numbers,
                         text_group):
        # Генерируем спрайты класса TextCard и заполняем группу text_group.

        for j in pos_numbers_text:
            number_text = str(list_of_card_numbers[j])
            text = TextCard(number_text, i, n)
            text.rect.x = \
                self.utilities.get_coords(j, self.size_rect_x,
                                          self.size_rect_y,
                                          text.center[0],
                                          text.center[1])[0]
            text.rect.y = \
                self.utilities.get_coords(j, self.size_rect_x,
                                          self.size_rect_y,
                                          text.center[0],
                                          text.center[1])[1]
            text_group.add(text)

    def check_events(self, running):
        # Проверки событий и их обработка на нажатие и отпускание клавиш.

        for event in pg.event.get():

            # Закрытие игры по нажатию на крестик окна.
            if event.type == pg.QUIT:
                sys.exit()

            # Проверка события на нажатие клавиши.
            elif event.type == pg.KEYUP:
                self.check_keyup_events(event)

            # Проверка события на отжатие клавиши.
            elif event.type == pg.KEYDOWN:
                self.check_keydown_events(event, running)

    def check_keyup_events(self, event):
        # Обработка событий отжатия клавиш.
        pass

    def check_keydown_events(self, event, running):
        # Если нажата клавиша ESCAPE, игра закрывается.
        if event.key == pg.K_ESCAPE:
            running = False
            self.run_game()

        elif event.key == pg.K_e:
            self.s.play()
            ran = self.pouch.iter(self.pouch.rand_list)
            print(ran)
            self.pouch.draw_pouch(ran, self.layer_game)

            for j in self.coord_list_checks:
                if ran == j:
                    self.coord_list_checks[
                        self.coord_list_checks.index(j)] = 0
                    print(self.coord_list_checks)

            for i in self.text_group:
                if str(ran) == TextCard.get_text(i):
                    i.update()

            for j in self.coord_list_checks_enemy:
                if ran == j:
                    self.coord_list_checks_enemy[
                        self.coord_list_checks_enemy.index(j)] = 0
                    print(self.coord_list_checks_enemy)

            for i in self.text_group1:
                if str(ran) == TextCard.get_text(i):
                    i.update()

            self.win = self.win_check(self.coord_list_checks)
            self.win_enemy = self.win_check(self.coord_list_checks_enemy)

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
            self.check_events(running)
            self.clock.tick(30)
            self.screen.blit(self.layer_game, (0, 0))
            self.draw_win_field(self.win, (275, 300), (275, 300))
            self.draw_win_field(self.win_enemy,
                                (Screen.screen_height.value + 200, 300),
                                (Screen.screen_height.value + 200, 300))

            self.draw_winner(self.win_game, (Screen.screen_width.value // 2,
                                             Screen.screen_height.value // 2),
                             (
                                 Screen.screen_width.value // 2,
                                 Screen.screen_height.value // 2))

            self.card.draw_background_card(self.layer_game)
            self.card.get_card_field(self.card_field_coord_list,
                                     self.layer_game)
            self.text_group.draw(self.layer_game)
            self.card2.draw_background_card(self.layer_game)
            self.card2.get_card_field(self.card_field_coord_list,
                                      self.layer_game)
            self.text_group1.draw(self.layer_game)
            pg.display.update()

    def run_game(self):
        running = True
        while running:
            self.clock.tick(30)
            self.screen.fill(Colors.blue.value)
            self.screen.blit(self.home_screen_font_surf,
                             self.home_screen_font_rect)
            self.screen.blit(self.home_screen_font1_surf,
                             self.home_screen_font1_rect)

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

            pg.display.update()


if __name__ == '__main__':
    game = Game()
    game.run_game()
