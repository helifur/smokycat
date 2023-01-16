import pygame
from data.modules.database import DataBase


class Point(pygame.sprite.Sprite):
    image = pygame.image.load("data/images/points/fish.png")
    current_price = DataBase.get_data(table="fish")[0]

    def __init__(self, group, point_x):
        super().__init__(group)
        self.image = Point.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = point_x
        self.rect.y = 550
        self.mask = pygame.mask.from_surface(self.image)

    def check(self, smoky, shift):
        if pygame.sprite.collide_mask(self, smoky):
            return False
        self.rect = self.rect.move(-shift, 0)
        return True
