import pygame
from data.modules.config import LIFE_SHIFT, FIRST_LIFE_SHIFT, LIVES_TABLE
from data.modules.database import DataBase


class Life(pygame.sprite.Sprite):
    image_active = pygame.image.load("data/images/hearts/heartactive.png")
    image_inactive = pygame.image.load("data/images/hearts/heartinactive.png")

    def __init__(self, x):
        super().__init__()
        self.image = Life.image_active.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 43


class Lives(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        # все существующие жизни в виде списка
        self.items = list(self)

    def new_life(self):
        # добавляем новую жизнь
        self.add(Life(LIFE_SHIFT * len(self) + FIRST_LIFE_SHIFT))
        # переопределяем старый список жизней
        self.items = list(self)

    def setup_lives(self):
        # используем метод get_data с флагом lives, чтобы дать понять
        # методу, что мы используем его для получения кол-ва жизней
        for _ in range(DataBase.get_data(table=LIVES_TABLE)[0]):
            self.new_life()

    def last_life(self):
        """Метод возвращает и удаляет последнюю жизнь в списке."""
        return self.items.pop(-1)
