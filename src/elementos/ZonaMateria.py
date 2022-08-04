import pygame

from utils.measures import *


class ZonaMateria(pygame.sprite.Sprite):
    materials = [
        {
            "name": "agua_dulce",
            "image": "assets/materias/agua_dulce.jpg"
        },
        {
            "name": "agua_salada",
            "image": "assets/materias/agua_salada.jpg"
        }
    ]

    def __init__(self):
        super().__init__()
        self.pos = 0
        self.image = pygame.transform.scale(pygame.image.load(
            self.materials[self.pos].get("image")).convert_alpha(), (600, 150))
        self.rect = self.image.get_rect()
        self.anterior = 0
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 80

    def update(self):
        # print("actual ",self.pos)
        # print("anterior ",self.anterior)
        keystate = pygame.key.get_pressed()
        # -----------X-----------------
        self.anterior = self.pos
        if keystate[pygame.K_a]:
            self.pos -= 1
        if keystate[pygame.K_d]:
            self.pos += 1
        if self.pos != self.anterior:
            material = {}
            if self.pos >= len(self.materials):
                self.pos = 0
            if self.pos < 0:
                self.pos = len(self.materials) - 1
            self.anterior = self.pos
            material = self.materials[self.pos]
            self.image = pygame.transform.scale(pygame.image.load(
                material.get("image")).convert_alpha(), (600, 150))
