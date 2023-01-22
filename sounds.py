import pygame as pg


class Sounds:
    @staticmethod
    def plays_sound(sounds: str, volume: float):
        track = pg.mixer.Sound(sounds)
        track.set_volume(volume)
        track.play()

