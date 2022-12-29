import pygame


class Barrier(pygame.sprite.Sprite):
    image = pygame.image.load("data/images/barrier/rocks.png")

    def __init__(self, group, barrier_x):
        super().__init__(group)
        self.image = pygame.transform.scale(Barrier.image.convert_alpha(), (110, 110))
        self.rect = self.image.get_rect()
        self.rect.x = barrier_x
        self.rect.y = 500
        self.mask = pygame.mask.from_surface(self.image)

    def check(self, smoky, shift):
        if pygame.sprite.collide_mask(self, smoky):
            return False
        self.rect = self.rect.move(-shift, 0)
        return True
