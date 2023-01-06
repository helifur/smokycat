import pygame
from data.modules.config import LIFE_SHIFT, FIRST_LIFE_SHIFT


class Life(pygame.sprite.Sprite):
    image_active = pygame.image.load("data/images/hearts/heartactive.png")
    image_inactive = pygame.image.load("data/images/hearts/heartinactive.png")

    def __init__(self, x):
        super().__init__()
        self.image = Life.image_active.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 10


class Lives(pygame.sprite.Group):
    def __init__(self, life1):
        super().__init__()
        # добавляем первую жизнь
        self.add(life1)
        # все существующие жизни в виде списка
        self.items = list(self)

    def new_life(self):
        # добавляем новую жизнь
        self.add(Life(LIFE_SHIFT * len(self) + FIRST_LIFE_SHIFT))
        # переопределяем старый список жизней
        self.items = list(self)

    def last_life(self):
        """Метод возвращает и удаляет последнюю жизнь в списке."""
        return self.items.pop(-1)
