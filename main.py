from turtle import*
import math


def paint():
    title('Ensayo')


def calculate_angle_refraction(n_a, n_b, angle_a):

    x = (n_a/n_b) * math.sin(degrees_to_radians(angle_a))
    print('x ->', x)
    return radians_to_degrees(math.asin(x))


def degrees_to_radians(angle):
    return ((angle * math.pi) / 180)


def radians_to_degrees(angle):
    return ((angle * 180) / math.pi)


if __name__ == '__main__':
    print(calculate_angle_refraction(1.33, 1.52, 60))

