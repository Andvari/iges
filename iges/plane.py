from vertex import Vertex
from entities import *
import math
from line import Line


class Plane:
    def __init__(self, *args):
        self.__p = []

        if args[0] == 'XY':
            self.__p.append(Vertex(0, 0, 0))
            self.__p.append(Vertex(1, 0, 0))
            self.__p.append(Vertex(0, 1, 0))
            return

        if args[0] == 'YZ':
            self.__p.append(Vertex(0, 0, 0))
            self.__p.append(Vertex(0, 1, 0))
            self.__p.append(Vertex(0, 0, 1))
            return

        if args[0] == 'XZ':
            self.__p.append(Vertex(0, 0, 0))
            self.__p.append(Vertex(1, 0, 0))
            self.__p.append(Vertex(0, 0, 1))
            return

        if len(args[0]) == 3:
            for v in args[0]:
                self.__p.append(v)

        return

    def coincide(self, plane):
        (a0, b0, c0), d0 = self.abcd()
        (a1, b1, c1), d1 = plane.abcd()

        k = []
        if equ(a1, 0):
            if not equ(a0, 0):
                return False
        else:
            k.append(a0/a1)

        if equ(b1, 0):
            if not equ(b0, 0):
                return False
        else:
            k.append(b0/b1)

        if equ(c1, 0):
            if not equ(c0, 0):
                return False
        else:
            k.append(c0/c1)

        if equ(d1, 0):
            if not equ(d0, 0):
                return False
        else:
            k.append(d0/d1)

        if len(k) == 1:
            return True

        for i in range(1, len(k)):
            if not equ(k[i-1], k[i]):
                return False

        return True

    def parallel(self, p):
        (a0, b0, c0), d0 = self.abcd()
        (a1, b1, c1), d1 = p.abcd()

        k = []
        if equ(a1, 0):
            if not equ(a0, 0):
                return False
        else:
            k.append(a0/a1)

        if equ(b1, 0):
            if not equ(b0, 0):
                return False
        else:
            k.append(b0/b1)

        if equ(c1, 0):
            if not equ(c0, 0):
                return False
        else:
            k.append(c0/c1)

        if len(k) == 1:
            return True

        for i in range(1, len(k)):
            if not equ(k[i-1], k[i]):
                return False

        return True

    def abcd(self):

        v = Vertex(0, 0, 0)
        d = 0
        p = self.__p
        p.append(self.__p[0])
        p.append(self.__p[1])

        for i in range(1, len(p)-1):
            x0, y0, z0 = p[i-1].value()
            x1, y1, z1 = p[i].value()
            x2, y2, z2 = p[i+1].value()

            k1 = (z2 - z0) * (y1 - y0) - (z1 - z0) * (y2 - y0)
            k2 = (z2 - z0) * (x1 - x0) - (z1 - z0) * (x2 - x0)
            k3 = (y2 - y0) * (x1 - x0) - (y1 - y0) * (x2 - x0)

            t = Vertex(k1, -k2, k3)
            v += t

            d += -k1*x0 + k2*y0 - k3*z0

        return v, d

    def print(self):
        v, d = self.abcd()
        for point in self.__p:
            print(point.value('X'), point.value('Y'), point.value('Z'))
        a, b, c = v.value()
        print("abcd: ", a, b, c, d)
        print('--------------')

    def intersect_line(self, p):

        (a1, b1, c1), d1 = self.abcd()
        (a2, b2, c2), d2 = p.abcd()

        v = Vertex(b1 * c2 - b2 * c1, -(a1 * c2 - a2 * c1), a1 * b2 - a2 * b1)

        if abs(a1*b2 - a2*b1):
            y = (d2 * a1 - d1 * a2) / (b1 * a2 - b2 * a1)
            x = (d2 * b1 - d1 * b2) / (a1 * b2 - a2 * b1)
            z = 0
        elif abs(a1*c2 - a2*c1):
            z = (d2 * a1 - d1 * a2) / (c1 * a2 - c2 * a1)
            x = (d2 * c1 - d1 * c2) / (a1 * c2 - a2 * c1)
            y = 0
        elif abs(c1*b2 - c2*b1):
            z = (d2 * b1 - d1 * b2) / (c1 * b2 - c2 * b1)
            y = (d2 * c1 - d1 * c2) / (b1 * c2 - b2 * c1)
            x = 0
        else:
            return None

        return Line(Vertex(x, y, z), v)

    def angle(self, l: Line, p2: Vertex):

        v, d = self.abcd()
        x0, y0, z0 = l.point() + v

        x1, y1, z1 = p2

        l = Line(Vertex(x0, y0, z0), Vertex(x1-x0, y1-y0, z1-z0))

        p = self.intersect_point(l)

        if p is not None:
            x, y, z = p.value()

            l1 = Vertex(x0, y0, z0).distance(Vertex(x1, y1, z1))
            l2 = Vertex(x0, y0, z0).distance(Vertex(x, y, z))

            if l1 > l2:
                return 'Concave'
            else:
                return 'Convex'

        return 'Concave'

    '''
    def vector(self):
        a, b, c, d = self.abcd()
        return Vertex(a, b, c)
    '''

    def intersect_point(self, l: Line):

        x1, y1, z1 = l.point().value()
        l, m, n = l.vector().value()

        v, d = self.abcd()

        a, b, c = v.value()

        d1 = l*a + m*b + n*c

        if not d1:
            return None

        x2 = ((m*b + n*c)*x1 - l*b*y1 - l*c*z1 - l*d)/d1
        y2 = (-m*a*x1 + (l*a + n*c)*y1 - m*c*z1 - m*d)/d1
        z2 = (-n*a*x1 - n*b*y1 + (l*a + m*b)*z1 - n*d)/d1

        return Vertex(x2, y2, z2)

    def coincide_abcd(self, p: Vertex):

        x0, y0, z0 = p.value()
        x1, y1, z1 = self.__p[0].value()
        v, d = self.abcd()

        l, m, n = v.value()

        if not x0*l + y0*m + z0*n + d:
            return None

        d = l*l + m*m + n*n

        if not d:
            return None

        x2 = ((m*m + n*n)*x1 - l*m*y1 - l*n*z1 + l*(l*x0 + m*y0 + n*z0))/d
        y2 = (-l*m*x1 + (l*l + n*n)*y1 - m*n*z1 + m*(l*x0 + m*y0 + n*z0))/d
        z2 = (-l*n*x1 - m*n*y1 + (l*l + m*m)*z1 + n*(l*x0 + m*y0 + n*z0))/d

        d0 = self.__p[0].distance(Vertex(x2, y2, z2))
        d1 = math.sqrt(d)
        d01 = Vertex(x2, y2, z2).distance(v)

        return not (gt(d01, d0) and gt(d01, d1))
