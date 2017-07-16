from entities import equ
import math
from point import Point
from radius_vector import RadiusVector
from line import Line


class Vector:
    def __init__(self, *args):
        self.__start_point = Point()
        self.__radius_vector = RadiusVector()

        if args:
            if type(args[0]) is Point:
                self.__start_point = args[0]
            else:
                raise ValueError('Vector: args[0] is not Point')
            if type(args[1]) is RadiusVector:
                self.__radius_vector = args[1]
            elif type(args[1]) is Point or args[1]:
                self.__radius_vector = args[1] - args[0]
            else:
                raise ValueError('Vector: args[1] is non RadiusVector non Point')
        return

    def __add__(self, p):
        if type(p) is Vector:
            return Vector(self.__start_point, self.__radius_vector + p.__radius_vector)
        else:
            raise ValueError('Vector __add__(): p is not Vector')

    def __eq__(self, p):
        if type(p) is Vector:
            return self.__start_point == p.__start_point and self.__radius_vector == p.__radius_vector
        else:
            raise ValueError('Vector __equ__(): p is not Vector')

    def __iter__(self):
        return self.__p.__iter__()

    def __len__(self):
        return self.__p.distance(Point(0, 0, 0))

    def __neg__(self):
        return Vector(self.__start_point, -self.__radius_vector)

    def __next__(self):
        return self.__p.__next__()

    def __str__(self):
        return str(self.__start_point) + str(self.__radius_vector)

    def __sub__(self, p):
        if p is Vector:
            return Vector(self.__start_point, self.__radius_vector - p.__radius_vector)
        return

    def line(self):
        return Line(self.__start_point, self.__radius_vector)

    def scale(self, t):
        x0, y0, z0 = self.__radius_vector
        return Vector(self.__start_point, self.__radius_vector.scale(t))

    def smult(self, p):
        if type(p) is Vector:
            x0, y0, z0 = self.__radius_vector
            x1, y1, z1 = p.__radius_vector
            return x0 * x1 + y0 * y1 + z0 * z1
        else:
            raise ValueError('Vector smult(): p is not Vector')

    def vmult(self, p):
        if type(p) is Vector:
            x0, y0, z0 = self.__radius_vector
            x1, y1, z1 = p.__radius_vector
            x = y0 * z1 - y1 * z0
            y = -x0 * z1 + x1 * z0
            z = x0 * y1 - x1 * y0
            return Vector(self.__radius_vector, RadiusVector(x, y, z))
        else:
            raise ValueError('Vector smult(): p is not Vector')
