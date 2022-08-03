import pygame
from elementos.Laser import RectLaser
# from elementos.Laser import RectLaser

from utils.colors import *
from utils.measures import *

# IMAGE = pygame.image.load("assets/disparador.png").convert_alpha()


class Lanzador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(
            "assets/disparador.png").convert_alpha(), (200, 200))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 400
        self.speed_x = 0
        self.speed_angle = 0
        self.angle = 90
        self.laser = RectLaser(self.rect.centerx, self.rect.bottom, self.angle)

    def update(self):
        self.speed_angle = 0
        self.speed_x = 0
        keystate = pygame.key.get_pressed()
        #-----------X-----------------  
        if keystate[pygame.K_LEFT]:
            self.speed_x = -1
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 1
        self.rect.x += self.speed_x
        #-----------ANGLE-----------------
        if keystate[pygame.K_UP]:
            self.speed_angle = 1
        if keystate[pygame.K_DOWN]:
            self.speed_angle = -1
        self.angle += self.speed_angle
        #------------Validaciones X----------------------
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        #------------Validaciones ANGULO----------------------
        if self.angle > 180:
            self.angle = 180
        if self.angle < 0:
            self.angle = 0
        self.laser = RectLaser(self.rect.centerx, self.rect.bottom, self.angle)
