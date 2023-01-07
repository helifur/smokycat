"""Здесь задаются константы и параметры игры."""
from pygame import font


def get_fonts():
    FONT = font.Font(None, 60)
    FONT_HEAD = font.Font("data/fonts/Sevillana-Regular.ttf", 90)

    return FONT, FONT_HEAD


# общие
FPS = 140
WIDTH = 1200
HEIGHT = 720
COUNT_TEXT_X = 990
COUNT_TEXT_Y = 20

# фон
# скорость фона
BG_SPEED = 600
# ускорение фона будет увеличиваться каждые
# BG_SECONDS миллисекунд
BG_TIMER_SECONDS = 10000
# ускорение фона каждые BG_SECONDS миллисекунд будет
# увеличиваться на BG_SPEED_PLUS
BG_SPEED_PLUS = 50

# барьеры
# изначально камни будут появляться каждые
# BARRIER_TIMER_SECONDS миллисекунд
BARRIER_TIMER_SECONDS = 1600
# каждый раз при ускорении фона таймер уменьшается
# на BARRIER_TIMER_DELAY миллисекунд
BARRIER_TIMER_DELAY = 100
# начальная координата любого камня
BARRIER_X = 1150
# размеры барьера по x и y
BARRIER_SIZE_X = 110
BARRIER_SIZE_Y = 110

# прыжок
# счетчик прыжков
JUMP_COUNT = 30

# жизни
# сдвиг первого сердца на экране
FIRST_LIFE_SHIFT = 20
# расстояние между всеми сердцами на экране
LIFE_SHIFT = 70

# столкновение
# каждые COLLIDE_MILLIS будет срабатывать событие,
# ответственное за анимацию столкновения (collide_timer)
# проще говоря, 2-й аргумент pygame.time.set_timer()
COLLIDE_MILLIS = 200
# collide_timer будет срабатывать COLLIDE_LOOPS раз
COLLIDE_LOOPS = 4
