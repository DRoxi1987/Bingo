import sys
from sprites import *
from buttons import Button


class HomeLayer:
    def __init__(self):
        # Флаг запуска основного цикла слоя.

        self.state = "home"
        self.flag = True
        # Настройки фпс.
        self.clock = pg.time.Clock()
        self.fps = Screen.fps.value
        self.button_game = Button(
            "asset/72ppi/button_game.png",
            "asset/72ppi/button_game_pr.png",
            "asset/72ppi/button_game_cl.png",
            Coords(Screen.screen_width.value // 2,
                   Screen.screen_height.value // 3 * 2)
        )
        self.button_exit = Button(
            "asset/72ppi/button_exit.png",
            "asset/72ppi/button_exit_pr.png",
            "asset/72ppi/button_exit_cl.png",
            Coords(Screen.screen_width.value // 2,
                   Screen.screen_height.value // 6 * 5)
        )

        self.home_logo = pg.image.load("asset/72ppi/Asset 26-01.png").convert_alpha()
        self.home_logo_scale = pg.transform.smoothscale(self.home_logo,
                                                        (self.home_logo.get_width()*0.8,
                                                         self.home_logo.get_height() * 0.8))
        self.home_logo_rect = self.home_logo_scale.get_rect(
            center=(Screen.screen_width.value // 2,
                    Screen.screen_height.value // 3))

    def create_layer(self, screen: pg.surface.Surface) -> None:
        """Создает основной цикл слоя"""

        self.clock.tick(self.fps)

        screen.fill(Colors.light_blue.value)
        self.button_game.button_blit(screen)
        self.button_exit.button_blit(screen)
        screen.blit(self.home_logo_scale, self.home_logo_rect)
        # Drawer.draw_text("Bingo!",
        #                  Fonts.font_text3.value,
        #                  Fonts.home_screen_font_logo_size.value,
        #                  screen, Colors.pink.value, None,
        #                  Coords(Screen.screen_width.value // 2,
        #                         Screen.screen_height.value // 4))
        pg.display.update()

    def check_events_home(self) -> str:
        """Проверяет события"""
        mouse_pos = pg.mouse.get_pos()
        if self.button_game.rect.collidepoint(mouse_pos):
            self.button_game.image = self.button_game.image_pr
        else:
            self.button_game.image = self.button_game.image_initial

        if self.button_exit.rect.collidepoint(mouse_pos):
            self.button_exit.image = self.button_exit.image_pr
        else:
            self.button_exit.image = self.button_exit.image_initial

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                if event.key == pg.K_SPACE:
                    return "game"
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1 \
                    and self.button_game.rect.collidepoint(mouse_pos):
                self.button_game.image = self.button_game.image_cl
                return "game"

            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1 \
                    and self.button_exit.rect.collidepoint(mouse_pos):
                self.button_exit.image = self.button_game.image_cl
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
                self.button_game.image = self.button_game.image_initial
                self.button_exit.image = self.button_exit.image_initial
