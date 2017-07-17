from entities import equ
import math


class Point:
    def __init__(self, *args):
        self.iterator = 0
        self.__coordinates = []
        if args:
            self.__coordinates = args
        return

    def __add__(self, p):
        assert type(p) is Point, 'Point __add__(): p is not Point'

        x0, y0, z0 = self
        x1, y1, z1 = p
        return Point(x0+x1, y0+y1, z0+z1)

    def __delitem__(self, key):
        assert True, 'Point __delitem__(): operation not permitted'

    def __eq__(self, p):
        assert type(p) is Point, 'Point __eq__(): p is not Point'
        x0, y0, z0 = self
        x1, y1, z1 = p
        return equ(x0, x1) and equ(y0, y1) and equ(z0, z1)

    def __getitem__(self, item):
        assert 0 <= item <= 2, 'Point __getitem__(): index out of range'
        return self.__coordinates[item]

    def __iter__(self):
        return self

    def __neg__(self):
        return Point(-self.__coordinates[0], -self.__coordinates[1], -self.__coordinates[2])

    def __next__(self):
        if self.iterator < 3:
            self.iterator += 1
            return self.__coordinates[self.iterator-1]
        else:
            self.iterator = 0
            raise StopIteration

    def __setitem__(self, key, value):
        assert 0 <= key <= 1, 'Point __setitem__(): key is out of range'
        self.__coordinates[key] = value

    def __str__(self):
        lx = 5-len(str(self[0])) % 5
        ly = 5-len(str(self[1])) % 5
        s = '{ ' + str(self[0]) + ','
        s += ' '*lx + str(self[1]) + ','
        s += ' '*ly + str(self[2]) + ' }'
        return s

    def __sub__(self, p):
        assert type(p) is Point, 'Point __sub__(): p is not Point'
        x0, y0, z0 = self
        x1, y1, z1 = p
        return Point(x1-x0, y1-y0, z1-z0)

    def distance(self, p):
        assert type(p) is Point, 'Point distance(): p is not Point'
        p1 = p - self
        return math.sqrt(p1[0] * p1[0] + p1[1] * p1[1] + p1[2] * p1[2])

    def midpoint(self, p):
        assert type(p) is Point, 'Point midpoint(): p is not Point'
        return Point((self[0] + p[0]) / 2, (self[1] + p[1]) / 2, (self[2] + p[2]) / 2)
