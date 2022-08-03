# from refraction_reflection import refraction_reflection
import pygame
import sys
from elementos.Lanzador import Lanzador
from elementos.Laser import RectLaser
from elementos.ZonaMateria import ZonaMateria
from utils.colors import *
from utils.measures import *

pygame.init()

size = 800, 600
screen = pygame.display.set_mode(size)
# posX = WIDTH // 2
# posY = HEIGHT - 600
pygame.display.set_caption("Reflexion y refracción")  # Nombre de la ventana
# lanzador = pygame.transform.scale(pygame.image.load(
#     "assets/disparador.png").convert_alpha(), (200, 200))
bg = pygame.transform.scale(pygame.image.load(
    "assets/laboratorio.jpg").convert_alpha(), (WIDTH, HEIGHT))
# laser = RectLaser(posX, posY+200, 90)
materia = ZonaMateria()
Lanzador = Lanzador()
all_sprites = pygame.sprite.Group()
all_sprites.add(materia)
all_sprites.add(Lanzador)
laserFlexivo = None
laserRefractado = None

while True:
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    colision = pygame.sprite.collide_rect(Lanzador.laser, materia)
    all_sprites.update()
    if colision:
        if not laserFlexivo:
            laserFlexivo = RectLaser(Lanzador.laser.x, Lanzador.laser.y, 45)
        if laserFlexivo:
            laserFlexivo.update()
        if not laserRefractado:
            laserRefractado = RectLaser(Lanzador.laser.x, Lanzador.laser.y, 80)
    else:
        Lanzador.laser.update(screen)
    all_sprites.draw(screen)
    pygame.display.update()
