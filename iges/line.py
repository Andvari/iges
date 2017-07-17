from point import Point
#from vertex import Vertex
from radius_vector import RadiusVector


class Line:
    def __init__(self, *args):
        assert args, 'Line __init__(): Line without args'
        assert type(args[0]) is Point, 'Line: __init__()args[0] is not Point'
        assert type(args[1]) is Point or RadiusVector, 'Line __init__(): args[1] is not Point or RadiusVector'
        self.__p = [args[0], args[1]]

    def point(self):
        return self.__p[0]

    def vector(self):
        if type(self.__p[1]) is Point:
            return self[1] - self[0]
        return self[1]

    def __getitem__(self, item):
        assert 0 <= item <= 1, 'Line __getitem__(): item is out f range'
        return self.__p[item]

    def __setitem__(self, key, value):
        assert True, 'Line __setitem__(): operation not permitted'

    def __delitem__(self, key):
        assert True, 'Line __delitem__(): operation not permitted'

    def coincide(self, l):
        assert type(l) is Line or Point, 'Edge coincide(): e not Line or Point'

        if type(l) is Line:
            return self.coincide(l[0]) and self.coincide(l[1])
        else:
            x0, y0, z0 = self.point()
            dx, dy, dz = self.vector()
            x, y, z = l

        if dx:
            if dy:
                if dz:
                    return (x-x0)/dx == (y-y0)/dy and (x-x0)/dx == (z-z0)/dz
                else:
                    return (x-x0)/dx == (y-y0)/dy and z == z0
            else:
                if dz:
                    return (x-x0)/dx == (z-z0)/dz and y == y0
                else:
                    return y == y0 and z == z0
        else:
            if dy:
                if dz:
                    return (y-y0)/dy == (z-z0)/dz and x == x0
                else:
                    return x == x0 and z == z0
            else:
                if dz:
                    return x == x0 and y == y0
                else:
                    return x == x0 and y == y0 and z == z0

        raise ValueError('Line coincide(): unexpected error')

    def intersect_point(self, l):
        assert type(l) is Line, 'Line cross_point(): l is not Line'
        if self.coincide(l) or self.parallel(l):
            return None

    def parallel(self, l):
        assert type(l) is Line, 'Line cross_point(): l is not Line'

    def gradient(self):
        g = []
        if self.vector()[0]:
            g.append(0)
        if self.vector()[1]:
            g.append(1)
        if self.vector()[2]:
            g.append(2)

        return g

    def __str__(self):
        if type(self[1]) is Point:
            return str(self[0]) + ', ' + str(self[1] - self[0])
        else:
            return str(self[0]) + ', ' + str(self[1])
