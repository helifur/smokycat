import os
import random
import sys

import pygame

from data.modules.animated_smoky import AnimatedSmoky
from data.modules.background import Background
from data.modules.barrier import Barrier
from data.modules.point import Point
from data.modules.menu import Menu


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


def terminate():
    pygame.quit()
    sys.exit()


def end():
    size = (WIDTH, HEIGHT)
    end_group = pygame.sprite.Group()

    over_image = pygame.transform.scale(load_image("images/game_over/gameover.png"), (1200, 720))
    over = pygame.sprite.Sprite(end_group)
    over.image = over_image
    over.rect = over.image.get_rect()
    over.rect.topleft = (-1200, 0)

    result = font.render(f"Вы собрали {count_fish} рыбок!", 1, (255, 192, 203))
    result_x = 480
    result_y = 500

    running = True
    v = 400
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame.MOUSEBUTTONDOWN and over.rect.bottomright == size:
                return

        screen.fill(pygame.Color("black"))
        end_group.draw(screen)
        if over.rect.bottomright != size:
            over.rect.left += v / FPS
        else:
            screen.blit(result, (result_x, result_y))

        clock.tick(FPS)
        pygame.display.flip()

    pygame.quit()


def start_screen():
    global FPS, WIDTH, HEIGHT, clock, smoky, is_jump, jump_count, screen, font

    pygame.init()

    FPS = 120
    WIDTH = 1200
    HEIGHT = 720
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Smoky Cat")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 60)
    # меню
    menu = Menu()
    menu.append_option('Играть', lambda: 1)
    menu.append_option('Выйти', quit)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if pygame.key.get_pressed()[pygame.K_UP]:
                menu.switch(-1)

            if pygame.key.get_pressed()[pygame.K_DOWN]:
                menu.switch(1)

            if pygame.key.get_pressed()[pygame.K_RETURN]:
                # если игрок нажал кнопку "Играть"
                if menu.current_option_index == 0:
                    return  # начинаем игру

                menu.select()

        screen.fill((0, 0, 0))

        menu.draw(screen, 550, 300, 75)

        pygame.display.flip()
        clock.tick(FPS)


def game():
    global FPS, WIDTH, HEIGHT, clock, smoky, is_jump, jump_count, screen, font, count_fish

    # счетчик рыбок
    count_fish = 0
    count_text = font.render(str(count_fish), 1, (255, 192, 203))
    count_text_x = 1140
    count_text_y = 20
    screen.blit(count_text, (count_text_x, count_text_y))

    text = font.render("Рыбки:", 1, (255, 192, 203))
    text_x = 980
    text_y = 18
    screen.blit(text, (text_x, text_y))

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

    # создаем очки (рыбки)
    # начальная координата
    point_x = random.randint(barrier_x, barrier_x + random.randint(650, 800))
    # интервал появления тот же, что и для камней
    # список всех существующих монеток
    points_in_game = []

    # характеристики прыжка
    # флаг
    is_jump = False
    # счетчик прыжков
    jump_count = 30
    point = pygame.image.load('data/images/points/fish.png')
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
            # или рыбку
            if event.type == barrier_timer:
                # создаем камень
                # добавляем его в список существующих
                # переопределяем координату камня
                # делаем ее случайной для разнообразия позиций камней
                barrier_x = random.randint(1270, 1590)
                barriers_in_game.append(Barrier(bg_group, barrier_x))
                # то же самое для рыбки
                point_x = random.randint(barrier_x, barrier_x + random.randint(450, 600))

                # # здесь нужно проверить
                # # чтобы новая рыбка не пересекалась
                # # ни с одним из камней
                # # тк это дефект
                if barriers_in_game:
                    for barrier in barriers_in_game:
                        # если рыбка пересекается с одним из камней
                        while pygame.sprite.collide_mask(Point(bg_group, point_x), barrier):
                            # переопределяем координату
                            point_x = random.randint(barrier_x, barrier_x + random.randint(650, 800))

                # добавляем рыбку
                points_in_game.append(Point(bg_group, point_x))

        screen.fill(pygame.Color("black"))

        # отображаем все
        bg_group.draw(screen)
        smoky_sprite.draw(screen)
        screen.blit(count_text, (count_text_x, count_text_y))
        screen.blit(text, (text_x, text_y))

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
                    end()
                    pygame.quit()
                    return "Continue"
                    # игра закончена
                    # running = False
                    # continue

        # все то же, что и с камнями
        if points_in_game:
            for point in points_in_game:
                # проверка пересечения рыбки и игрока
                if not point.check(smoky, shift):
                    # кол-во рыбок +1
                    count_fish += 1
                    # удаляем элемент из списка
                    points_in_game.remove(point)
                    # удаляем его с экрана
                    point.kill()

        # счетчик
        anim_count += 1
        # переопределяем текст с обновлённым балансом
        count_text = font.render(str(count_fish), 1, (255, 192, 203))

        clock.tick(FPS)
        pygame.display.flip()

    pygame.quit()


do = "Continue"
while do == "Continue":
    start_screen()
    do = game()
