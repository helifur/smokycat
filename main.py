import os
import pygame


class Background(pygame.sprite.Sprite):
    image = pygame.image.load("data/images/background/background.jpg")

    def __init__(self):
        super().__init__()
        self.image = Background.image


class AnimatedSmoky(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = pygame.transform.scale(self.frames[self.cur_frame], (124, 124))
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns, sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = pygame.transform.scale(self.frames[self.cur_frame], (124, 124))


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

all_sprites = pygame.sprite.Group()

background_sprite = pygame.sprite.Group()
background_image = Background()

bg_x = 0
bg_speed = 200

# счетчик анимаций
# нужен для стабильности переключения
# фреймов героя
anim_count = 0

smoky = AnimatedSmoky(load_image("images/right/smoky_right_sheet.png"), 3, 1, 200, 495)
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

    all_sprites.draw(screen)

    # анимация
    if anim_count == 8:
        all_sprites.update()
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
