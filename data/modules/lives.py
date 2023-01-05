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
        self.add(life1)

    def add_elem(self):
        self.add(Life(LIFE_SHIFT * len(self) + FIRST_LIFE_SHIFT))
