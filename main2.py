import math
import pygame
import sys
import pygame_gui

pygame.init()

size = 800, 600
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Ensayo")


class Laser():
    def __init__(self, x, y, angle):
        super().__init__()
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 1
        self.color = (255, 0, 0)
        self.thickness = 1
        self.length = 100
        self.draw()

    def draw(self):
        pygame.draw.line(screen, self.color, (self.x, self.y), (self.x + self.length * math.cos(
            math.radians(self.angle)), self.y + self.length * math.sin(math.radians(self.angle))), self.thickness)

    def move(self):
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y += self.speed * math.sin(math.radians(self.angle))

    def update(self):
        self.move()
        self.draw()

    def set_angle(self, angle):
        self.angle = angle


class RectLaser(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 1
        self.color = (0, 255, 0)
        self.thickness = 1
        self.length = 100
        self.rect = pygame.Rect(x, y, 0, 0)
        self.draw()

    def draw(self):
        oldX = self.x
        oldY = self.y
        self.x = oldX + self.length * math.cos(math.radians(self.angle))
        self.y = oldY + self.length * math.sin(math.radians(self.angle))
        pygame.draw.polygon(screen, self.color, [
                            (oldX, oldY), (self.x, self.y)], self.thickness)

    def move(self):
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y += self.speed * math.sin(math.radians(self.angle))

    def update(self):
        self.move()
        self.draw()
        self.rect = pygame.Rect(self.x, self.y, 1, 1)

    def set_angle(self, angle):
        self.angle = angle


class Zone(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.draw()

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)


laser = Laser(0, 0, 30)
zone_one = Zone(180, 150, 100, 100, (0, 0, 255))
laser2 = RectLaser(0, 0, 30)
laserFlexivo = None
laserRefractado = None
colision2 = None
# colision = pygame.Rect.collidepoint(zone_one, laser.x, laser.y)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # laser.update()
    zone_one
    colision = pygame.sprite.spritecollide(laser2, [zone_one], False)

    if colision:
        if not colision2 and laserRefractado:
            colision2 = pygame.sprite.spritecollide(
                laserRefractado, [zone_one], False)
        if not laserFlexivo:
            laserFlexivo = RectLaser(laser2.x, laser2.y, 330)
        if laserFlexivo:
            laserFlexivo.update()
        if not laserRefractado:
            laserRefractado = RectLaser(laser2.x, laser2.y, 80)
        if laserRefractado:
            if colision2:
                print("colision")
            else:
                laserRefractado.update()
    else:
        laser2.update()

    pygame.display.update()
