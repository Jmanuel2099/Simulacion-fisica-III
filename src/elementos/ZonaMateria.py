import pygame

from utils.measures import *

class ZonaMateria(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(
            "assets/materias/agua_dulce.jpg").convert_alpha(), (600, 150))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 80

    def changeMaterial(self, material):
        self.material = material
        self.draw()