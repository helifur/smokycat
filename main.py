import os
import random

import pygame

from data.modules.animated_smoky import AnimatedSmoky
from data.modules.background import Background
from data.modules.barrier import Barrier


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert_alpha()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message) from message

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


# функция прыжка
def jump():
    global is_jump, jump_count, smoky

    # если перемещение в пределах разумного
    if jump_count >= -30:
        # в класс героя добавлена функция move
        # она осуществляет перемещение героя
        # по переданным координатам
        # res_x + x
        # res_y + y
        # res_x = итоговый x
        # res_y = итоговый y
        # x, y - аргументы "сдвига"
        smoky.move(0, -jump_count / 2.5)
        jump_count -= 1

    else:
        # возвращаем исходные значения
        jump_count = 30
        is_jump = False


pygame.init()

FPS = 120
WIDTH = 1200
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smoky Cat")
clock = pygame.time.Clock()

# Группа спрайтов фона
# сюда относятся два фона
# и камни, т.к. они движутся синхронно с фонами
bg_group = pygame.sprite.Group()
# группа спрайтов для героя
smoky_sprite = pygame.sprite.Group()

# координата первого фона
bg_x = 0
# скорость передвижения фона
bg_speed = 500

# определяем 2 фона
# первый - основной, его видит игрок
# второй - за пределами экрана
# нужен для иллюзии бесконечного мира
background1 = Background(bg_group, 0, 0)
background2 = Background(bg_group, 1270, 0)

# инициализируем камни (препятствия)
# начальная координата любого камня
barrier_x = 1150
# интервал появления камней
barrier_timer = pygame.USEREVENT + 1
pygame.time.set_timer(barrier_timer, 1600)
# список всех существующих камней
barriers_in_game = [Barrier(bg_group, barrier_x)]

# характеристики прыжка
# флаг
is_jump = False
# счетчик прыжков
jump_count = 30

# счетчик анимаций
# нужен для стабильности переключения
# фреймов героя
anim_count = 0

# главный герой
smoky = AnimatedSmoky(smoky_sprite, load_image("images/right/smoky_right_sheet.png"), 3, 1, 200, 495)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # если игрок нажал пробел и прыжок неактивен
        # активируем прыжок
        if not is_jump and pygame.key.get_pressed()[pygame.K_SPACE]:
            is_jump = True

        # если пришло время создавать камень
        if event.type == barrier_timer:
            # создаем камень
            # добавляем его в список существующих
            barrier_x = random.randint(1270, 1590)
            print(barrier_x)
            barriers_in_game.append(Barrier(bg_group, barrier_x))

    screen.fill(pygame.Color("black"))

    # отображаем все
    bg_group.draw(screen)
    smoky_sprite.draw(screen)

    # Сдвиг фона и камня
    # он одинаковый, т.к. камень должен
    # передвигаться параллельно с фоном
    # чтобы игрок видел камень
    # который стоит на месте
    shift = bg_speed / FPS

    if is_jump:
        jump()  # осуществляет прыжок

    # анимация
    if anim_count == 16:
        smoky_sprite.update()
        anim_count = 0

    """MOVE BG"""
    # двигаем спрайты
    background1.move(-shift)
    background2.move(-shift)

    # если первый фон вышел за пределы экрана
    # (правый верхний угол < 0)
    # перемещаем его левый верхний угол
    # в точку 1270, 0
    if background1.check():
        background1.move(1270 * 2)
    # так же со вторым
    if background2.check():
        background2.move(1270 * 2)
    """========"""

    # если камни существуют
    if barriers_in_game:
        # пробегаемся по всем камням
        for barrier in barriers_in_game:
            # проверка пересечения камня и игрока
            if not barrier.check(smoky, shift):
                print("END")
                # игра закончена
                running = False
                continue

    # счетчик
    anim_count += 1

    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
