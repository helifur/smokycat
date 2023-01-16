import pygame
from data.modules.config import BARRIER_SIZE_X, BARRIER_SIZE_Y


class Barrier(pygame.sprite.Sprite):
    image = pygame.image.load("data/images/barrier/rocks.png")

    def __init__(self, group, barrier_x):
        super().__init__(group)
        self.image = pygame.transform.scale(Barrier.image.convert_alpha(), (BARRIER_SIZE_X, BARRIER_SIZE_Y))
        self.rect = self.image.get_rect()
        self.rect.x = barrier_x
        self.rect.y = 500
        self.mask = pygame.mask.from_surface(self.image)

    def check(self, smoky):
        """Метод возвращает True или False в зависимости от того,
        было ли пересечение объекта с самим Barrier."""
        return pygame.sprite.collide_mask(self, smoky)

    def move(self, shift):
        """Метод двигает Barrier на shift влево по оси X."""
        self.rect = self.rect.move(-shift, 0)
