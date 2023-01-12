"""Здесь задаются константы и параметры игры."""
import pygame.display
from pygame import font
from data.modules.database import DataBase


def get_fonts():
    FONT = font.Font(None, 40)
    FONT_END_SCREEN = font.Font(None, 60)
    FONT_HEAD = font.Font("data/fonts/Sevillana-Regular.ttf", 90)
    FONT_BALANCE = font.Font("data/fonts/Pacifico-Regular.ttf", 50)

    return FONT, FONT_END_SCREEN, FONT_HEAD, FONT_BALANCE


# общие
FPS = 140
WIDTH = 1200
HEIGHT = 720
COUNT_TEXT_X = 20
COUNT_TEXT_Y = 10
# название таблицы жизней в базе
LIVES_TABLE = "lives"
# Название таблицы ускорения в базе
# отныне speed - это время, когда происходит ускорение персонажа.
# То есть каждые value секунд, указанные в базе, персонаж ускоряется
SPEED_TABLE = "speed"
# название таблицы рыбок в базе
FISH_TABLE = "fish"

# фон
# скорость фона
BG_SPEED = 620
# ускорение фона будет увеличиваться каждые
# BG_SECONDS миллисекунд
BG_TIMER_SECONDS = DataBase.get_data(table=SPEED_TABLE)[0] * 1000
# ускорение фона каждые BG_SECONDS миллисекунд будет
# увеличиваться на BG_SPEED_PLUS
BG_SPEED_PLUS = 50

# барьеры
# изначально камни будут появляться каждые
# BARRIER_TIMER_SECONDS миллисекунд
BARRIER_TIMER_SECONDS = 1600
# каждый раз при ускорении фона таймер уменьшается
# на BARRIER_TIMER_DELAY миллисекунд
BARRIER_TIMER_DELAY = 200
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
LIFE_SHIFT = 40

# столкновение
# каждые COLLIDE_MILLIS будет срабатывать событие,
# ответственное за анимацию столкновения (collide_timer)
# проще говоря, 2-й аргумент pygame.time.set_timer()
COLLIDE_MILLIS = 200
# collide_timer будет срабатывать COLLIDE_LOOPS раз
COLLIDE_LOOPS = 4

# цены
# +1 жизнь, +1 секунда ускорения и +1 к цене рыбки, цены прокачки
LIFE_PRICE = DataBase.get_data(table="lives")[1]
SPEED_PRICE = DataBase.get_data(table=SPEED_TABLE)[1]
FISH_PRICE = DataBase.get_data(table="fish")[1]
