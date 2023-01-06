import pygame


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

    def new_life(self, life_shift, first_life_shift):
        # добавляем новую жизнь
        self.add(Life(life_shift * len(self) + first_life_shift))
        # переопределяем старый список жизней
        self.items = list(self)

    def last_life(self):
        """Метод возвращает и удаляет последнюю жизнь в списке."""
        return self.items.pop(-1)
