from typing import NamedTuple
from enum import Enum


class Size(NamedTuple):
    width: int
    height: int


class Coords(NamedTuple):
    x: int
    y: int


class Track(NamedTuple):
    track_pouch = "sound/pouch.mp3"
    volume_pouch = 0.2


class Rectangle(NamedTuple):
    size_rect_x = 60
    size_rect_y = 60
    gap = 10


class Color(NamedTuple):
    red: int
    green: int
    blue: int


class Colors(Enum):
    bg_color = Color(128, 128, 128)
    color_white = Color(255, 255, 255)
    font_color = Color(70, 120, 90)
    font_background_color = (255, 255, 255)
    red = Color(188, 2, 5)
    gray = Color(231, 234, 227)
    light_blue = Color(115, 183, 188)
    blue = Color(15, 34, 51)
    black = Color(4, 5, 10)
    pink = Color(221, 98, 98)


class Fonts(Enum):
    font_text = 'font/clacon2.ttf'
    font_text1 = 'font/AgentOrange.ttf'
    font_text3 = 'font/Dunkin Bold.ttf'
    font_text4 = 'font/Anton.ttf'
    font_text_size = 30
    home_screen_font_logo_size = 250
    home_screen_font_menu_size = 60


class Screen(Enum):
    screen_width = 1280
    screen_height = 720
    fps = 30
    set_caption: str = "Bingo"


coord_list_base = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]