from turtle import*
import math
import turtle


def draw():
    title('Ensayo')
    bgcolor('gray')
    setup(1000, 600, 0, 0)

def draw_zone_one():
    setworldcoordinates(500, 300, 300, 0)
    fillcolor('blue')
    begin_fill()
    for i in range(4):
        forward(100)
        right(90)
    end_fill()


def calculate_angle_refraction(n_a, n_b, angle_a):
    x = (n_a/n_b) * math.sin(degrees_to_radians(angle_a))
    print('x ->', x)
    return radians_to_degrees(math.asin(x))

def degrees_to_radians(angle):
    return ((angle * math.pi) / 180)

def radians_to_degrees(angle):
    return ((angle * 180) / math.pi)


if __name__ == '__main__':
    draw()
    draw_zone_one()
    mainloop()

