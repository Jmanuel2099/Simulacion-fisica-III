import math
import pygame

from utils.measures import HEIGHT


class RectLaser():
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 1
        self.color = (255, 0, 0)
        self.thickness = 3
        self.length = HEIGHT
        self.rect = pygame.Rect(x, y, 0, 0)

    def draw(self, screen):
        oldX = self.x
        oldY = self.y
        self.x = oldX + self.length * math.cos(math.radians(self.angle))
        self.y = oldY + self.length * math.sin(math.radians(self.angle))
        pygame.draw.polygon(screen, self.color, [
                            (oldX, oldY), (self.x, self.y)], self.thickness)
        
    def move(self):
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y += self.speed * math.sin(math.radians(self.angle))

    def update(self, screen):
        self.move()
        self.draw(screen)
        self.rect = pygame.Rect(self.x, self.y, 1, 1)

    def set_angle(self, angle):
        self.angle = angle

    def updateValues(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle