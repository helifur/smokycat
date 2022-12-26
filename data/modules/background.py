import pygame


class Background(pygame.sprite.Sprite):
    image = pygame.image.load("data/images/background/background.jpg")

    def __init__(self):
        super().__init__()
        self.image = Background.image
