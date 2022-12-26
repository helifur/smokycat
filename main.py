import os
import pygame

from data.modules.animated_smoky import AnimatedSmoky
from data.modules.background import Background


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


pygame.init()

FPS = 60
WIDTH = 1200
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smoky Cat")
clock = pygame.time.Clock()

smoky_sprite = pygame.sprite.Group()

background_image = Background()

bg_x = 0
bg_speed = 200

# счетчик анимаций
# нужен для стабильности переключения
# фреймов героя
anim_count = 0

smoky = AnimatedSmoky(smoky_sprite, load_image("images/right/smoky_right_sheet.png"), 3, 1, 200, 495)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(pygame.Color("black"))

    # отображаем 2 фона
    # первый - основной, его видит игрок
    # второй - за пределами экрана
    # нужен для иллюзии бесконечного мира
    screen.blit(background_image.image, (bg_x, 0))
    screen.blit(background_image.image, (bg_x + 1270, 0))

    smoky_sprite.draw(screen)

    # анимация
    if anim_count == 8:
        smoky_sprite.update()
        anim_count = 0

    # двигаем фон
    bg_x -= bg_speed / FPS
    # если фон вышел за экран
    if -1274 <= bg_x <= -1268:
        bg_x = 0

    # счетчик
    anim_count += 1

    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
