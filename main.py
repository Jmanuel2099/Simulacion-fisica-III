from refraction_reflection import refraction_reflection
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((700,500))

if __name__ == '__main__':
    x = refraction_reflection(1.32, 1.52, 60)
    print(x.angle_refraction)
    # main()  
    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             sys.exit()    