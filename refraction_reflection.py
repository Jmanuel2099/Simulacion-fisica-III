import math
class refraction_reflection:

    # n_a -> refractive index of material a
    # n_b -> refractive index of material b
    #angle_a -> angle of incidence 
    def __init__(self, n_a, n_b, angle_a):
        self.__n_a = n_a
        self.__n_b = n_b
        self.__angle_a = angle_a
        self.angle_refraction = self.__calculate_angle_refraction()

    def __calculate_angle_refraction(self):
        x = (self.__n_a/self.__n_b) * math.sin(self.__degrees_to_radians(self.__angle_a))
        return self.__radians_to_degrees(math.asin(x))

    def __degrees_to_radians(self, angle):
        return ((angle * math.pi) / 180)

    def __radians_to_degrees(self, angle):
        return ((angle * 180) / math.pi)