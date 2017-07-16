from entities import equ
import math
from point import Point


class RadiusVector:
    def __init__(self, *args):
        self.__p = Point()
        if args:
            self.__p = args[0]
        return

    def __add__(self, p):
        if type(p) is Point:
            return RadiusVector(Point(self[0] + p[0], self[1] + p[1], self[2] + p[2]))
        elif type(p) is RadiusVector:
            return self + p.__p
        else:
            raise ValueError('RadiusVector __add__(): p no Point or RadiusVector')

    def __delitem__(self, item):
        pass

    def __eq__(self, p):
        return self.__p == p.__p

    def __getitem__(self, item):
        return self.__p[item]

    def __iter__(self):
        return self.__p.__iter__()

    def __len__(self):
        return self.__p.distance(Point(0, 0, 0))

    def __neg__(self):
        return RadiusVector(-self.__p)

    def __next__(self):
        return self.__p.__next__()

    def __setitem__(self, key, value):
        self.__p[key] = value

    def __str__(self):
        return str(self.__p)

    def __sub__(self, p):
        if type(p) is RadiusVector:
            return RadiusVector(Point(p[0]-self[0], p[1]-self[1], p[2]-self[2]))
        else:
            raise ValueError('RadiusVector __sub__(): p is not RadiusVector')

    def scale(self, t):
        x0, y0, z0 = self
        return RadiusVector(x0*t, y0*t, z0*t)

    def smult(self, p):
        x0, y0, z0 = self
        x1, y1, z1 = p
        return x0 * x1 + y0 * y1 + z0 * z1

    def vmult(self, p):
        x0, y0, z0 = self
        x1, y1, z1 = p
        x = y0 * z1 - y1 * z0
        y = -x0 * z1 + x1 * z0
        z = x0 * y1 - x1 * y0
        return RadiusVector(x, y, z)

