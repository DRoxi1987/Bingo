import sys
from sprites import *
from buttons import Button


class HomeLayer:
    def __init__(self):
        # Флаг запуска основного цикла слоя.
        self.state = "home"
        # Настройки фпс.
        self.clock = pg.time.Clock()
        self.fps = Screen.fps.value
        self.button = Button(
            "asset/72ppi/button_game.png",
            "asset/72ppi/button_game_pr.png",
            "asset/72ppi/button_game_cl.png",
            Coords(Screen.screen_width.value // 2,
                   Screen.screen_height.value // 3 * 2)
        )

    def create_layer(self, screen: pg.surface.Surface) -> None:
        """Создает основной цикл слоя"""

        self.clock.tick(self.fps)
        screen.fill(Colors.light_blue.value)
        self.button.button_blit(screen)
        Drawer.draw_text("Bingo!",
                         Fonts.font_text3.value,
                         Fonts.home_screen_font_logo_size.value,
                         screen, Colors.pink.value, None,
                         Coords(Screen.screen_width.value // 2,
                                Screen.screen_height.value // 4))
        pg.display.update()

    def check_events_home(self) -> str:
        """Проверяет события"""
        mouse_pos = pg.mouse.get_pos()
        if self.button.rect.collidepoint(mouse_pos):
            self.button.image = self.button.image_pr
        else:
            self.button.image = self.button.image_initial

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
                    and self.button.rect.collidepoint(mouse_pos):
                self.button.image = self.button.image_cl
                return "game"
