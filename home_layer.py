import sys
from sounds import *
from pouch import Pouch
from card import Card
from sprites import *


class HomeLayer:
    def __init__(self):
        # Флаг запуска основного цикла слоя.
        self.state = "home"
        # Настройки фпс.
        self.clock = pg.time.Clock()
        self.fps = Screen.fps.value

    def create_layer(self, screen: pg.surface.Surface) -> None:
        """Создает основной цикл слоя"""

        self.clock.tick(self.fps)
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

    def check_events_home(self) -> str:
        """Проверяет события"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                if event.key == pg.K_SPACE:
                    print("game")
                    return "game"
                else:
                    continue

