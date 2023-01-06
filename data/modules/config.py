"""Здесь задаются константы и параметры игры."""
from pygame import font


def get_fonts():
    FONT = font.Font(None, 60)
    FONT_HEAD = font.Font("data/fonts/Sevillana-Regular.ttf", 90)

    return FONT, FONT_HEAD


FPS = 120
WIDTH = 1200
HEIGHT = 720

# фон
# ускорение фона будет увеличиваться каждые
# BG_SECONDS миллисекунд
BG_TIMER_SECONDS = 10000
# ускорение фона каждые BG_SECONDS миллисекунд будет
# увеличиваться на BG_SPEED_PLUS
BG_SPEED_PLUS = 200

# барьеры
# изначально камни будут появляться каждые
# BARRIER_TIMER_SECONDS миллисекунд
BARRIER_TIMER_SECONDS = 1600
# каждый раз при ускорении фона таймер уменьшается
# на BARRIER_TIMER_DELAY миллисекунд
BARRIER_TIMER_DELAY = 300
# начальная координата любого камня
BARRIER_X = 1150

# прыжок
# счетчик прыжков
JUMP_COUNT = 30

# жизни
# сдвиг первого сердца на экране
FIRST_LIFE_SHIFT = 20
# расстояние между всеми сердцами на экране
LIFE_SHIFT = 70
