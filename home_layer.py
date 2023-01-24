import sys
from sounds import *
from pouch import Pouch
from card import Card
from sprites import *


class HomeLayer:
    def __init__(self):
        # Флаг запуска основного цикла слоя.
        self.running = True

        # Настройки фпс.
        self.clock = pg.time.Clock()
        self.fps = Screen.fps.value

    def create_layer(self, screen: pg.surface.Surface,
                     run_layer_screen_game: 'function') -> None:
        """Создает основной цикл слоя"""
        while self.running:
            self.clock.tick(self.fps)
            self._check_events_home(run_layer_screen_game)
            screen.fill(Colors.blue.value)
            Drawer.draw_text("Bingo!",
                             Fonts.font_text.value,
                             Fonts.home_screen_font_logo_size.value,
                             screen, Colors.red.value, None,
                             Coords(Screen.screen_width.value // 2,
                                    Screen.screen_height.value // 3))

            Drawer.draw_text("Нажмите на пробел, чтобы начать!",
                             Fonts.font_text.value,
                             Fonts.home_screen_font_menu_size.value,
                             screen, Colors.color_white.value, None,
                             Coords(Screen.screen_width.value // 2,
                                    Screen.screen_height.value // 8 * 5))
            pg.display.update()

    def _check_events_home(self, run_layer_screen_game: 'function') -> None:
        """Проверяет события"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False
                    pg.quit()
                    sys.exit()
                elif event.key == pg.K_SPACE:
                    self.running = False
                    run_layer_screen_game()



