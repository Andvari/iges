from point import Point
from radius_vector import RadiusVector


class Line:
    def __init__(self, *args):
        assert 1 <= len(args) <= 2, 'Line __init__(): bad arguments'

        self.__p = []
        if type(args[0]) is Point and type(args[1]) is Point:
            self.__p.append(args[0])
            self.__p.append(args[1])
        elif type(args[0]) is Point and type(args[1]) is RadiusVector:
            self.__p.append(args[0])
            self.__p.append(args[0] + args[1])
        elif type(args[0]) is RadiusVector and type(args[1]) is Point:
            self.__p.append(args[1])
            self.__p.append(args[1] + args[0])
        else:
            assert True, 'Line __init__(): bad arguments'
        assert not self.__p[0] == self.__p[1], 'Line __init__(): no such line'

    def point(self):
        return self[0]

    def vector(self):
        return self[1] - self[0]

    def __getitem__(self, item):
        assert 0 <= item <= 1, 'Line __getitem__(): item is out f range'
        return self.__p[item]

    def __setitem__(self, key, value):
        assert True, 'Line __setitem__(): operation not permitted'

    def __delitem__(self, key):
        assert True, 'Line __delitem__(): operation not permitted'

    def coincide(self, l):
        assert type(l) is Line or Point, 'Edge coincide(): l not Line or Point'

        if type(l) is Line:
            return self.coincide(l[0]) and self.coincide(l[1])
        else:
            x0, y0, z0 = self.point()
            dx, dy, dz = self.vector()
            t = self.t(l)
            if Point(x0+dx*t, y0+dy*t, z0+dz*t) == l:
                return True
            return False

    def intersect_point(self, l):
        assert type(l) is Line, 'Line cross_point(): l is not Line'

        x0, y0, z0 = self.point()
        dx0, dy0, dz0 = self.vector()

        x1, y1, z1 = l.point()
        dx1, dy1, dz1 = l.vector()

        t = 0
        if dy0*dx1 - dy1:
            t = (y1-y0*dx0-dy0*(x1-x0))/(dy0*dx1-dy1)
        elif dz0*dx1 - dz1:
            t = (z1-z0*dx0-dz0*(x1-x0))/(dz0*dx1-dz1)
        elif dx0*dy1 - dx1:
            t = (x1-x0*dy0-dx0*(y1-y0))/(dx0*dy1-dx1)
        elif dz0*dy1 - dz1:
            t = (z1-z0*dy0-dz0*(y1-y0))/(dz0*dy1-dz1)
        elif dx0*dz1 - dx1:
            t = (x1-x0*dz0-dx0*(z1-z0))/(dx0*dz1-dx1)
        elif dy0*dz1 - dy1:
            t = (y1-y0*dz0-dy0*(z1-z0))/(dy0*dz1-dy1)
        else:
            return None

        p = Point(x1+dx1*t, y1+dy1*t, z1+dz1*t)

        if self.coincide(p) and l.coincide(p):
            return p

        return None

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
        return str(self.point()) + ', ' + str(self.vector())

    def t(self, p):
        if self.vector()[0]:
            return (p[0] - self.point()[0])/self.vector()[0]
        elif self.vector()[1]:
            return (p[1] - self.point()[1])/self.vector()[1]
        elif self.vector()[2]:
            return (p[2] - self.point()[2])/self.vector()[2]

        raise ValueError('Line t(): unexpected error')
