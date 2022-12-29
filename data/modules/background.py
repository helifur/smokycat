import pygame


class Background(pygame.sprite.Sprite):
    image = pygame.image.load("data/images/background/background.jpg")

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = Background.image.convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, x):
        self.rect = self.rect.move(x, 0)

    def check(self):
        if self.rect.x <= -1270:
            return True
