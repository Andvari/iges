from vertex import Vertex
from entities import *
import math


class Plane:
    def __init__(self, *args):
        self.p = []

        if args[0] == 'XY':
            self.p.append(Vertex(0, 0, 0))
            self.p.append(Vertex(1, 0, 0))
            self.p.append(Vertex(0, 1, 0))
            return

        if args[0] == 'YZ':
            self.p.append(Vertex(0, 0, 0))
            self.p.append(Vertex(0, 1, 0))
            self.p.append(Vertex(0, 0, 1))
            return

        if args[0] == 'XZ':
            self.p.append(Vertex(0, 0, 0))
            self.p.append(Vertex(1, 0, 0))
            self.p.append(Vertex(0, 0, 1))
            return

        if len(args[0]) == 3:
            for v in args[0]:
                self.p.append(v)

        return

    def coincide(self, plane):
        a0, b0, c0, d0 = self.abcd()
        a1, b1, c1, d1 = plane.abcd()

        k = []
        if equal(a1, 0):
            if not equal(a0, 0):
                return False
        else:
            k.append(a0/a1)

        if equal(b1, 0):
            if not equal(b0, 0):
                return False
        else:
            k.append(b0/b1)

        if equal(c1, 0):
            if not equal(c0, 0):
                return False
        else:
            k.append(c0/c1)

        if equal(d1, 0):
            if not equal(d0, 0):
                return False
        else:
            k.append(d0/d1)

        if len(k) == 1:
            return True

        for i in range(1, len(k)):
            if not equal(k[i-1], k[i]):
                return False

        return True

    def parallel(self, plane):
        a0, b0, c0, d0 = self.abcd()
        a1, b1, c1, d1 = plane.abcd()

        k = []
        if equal(a1, 0):
            if not equal(a0, 0):
                return False
        else:
            k.append(a0/a1)

        if equal(b1, 0):
            if not equal(b0, 0):
                return False
        else:
            k.append(b0/b1)

        if equal(c1, 0):
            if not equal(c0, 0):
                return False
        else:
            k.append(c0/c1)

        if len(k) == 1:
            return True

        for i in range(1, len(k)):
            if not equal(k[i-1], k[i]):
                return False

        return True

    def abcd(self):
        x0 = self.p[0].value('X')
        x1 = self.p[1].value('X')
        x2 = self.p[2].value('X')

        y0 = self.p[0].value('Y')
        y1 = self.p[1].value('Y')
        y2 = self.p[2].value('Y')

        z0 = self.p[0].value('Z')
        z1 = self.p[1].value('Z')
        z2 = self.p[2].value('Z')

        k1 = (z2 - z0) * (y1 - y0) - (z1 - z0) * (y2 - y0)
        k2 = (z2 - z0) * (x1 - x0) - (z1 - z0) * (x2 - x0)
        k3 = (y2 - y0) * (x1 - x0) - (y1 - y0) * (x2 - x0)

        a = k1
        b = -k2
        c = k3
        d = -k1*x0 + k2*y0 - k3*z0

        return a, b, c, d

    def print(self):
        a, b, c, d = self.abcd()
        for point in self.p:
            print(point.value('X'), point.value('Y'), point.value('Z'))
        print("abcd: ", a, b, c, d)
        print('--------------')

    def intersect(self, p):

        a1, b1, c1, d1 = self.abcd()
        a2, b2, c2, d2 = p.abcd()

        v = Vertex(b1 * c2 - b2 * c1, -(a1 * c2 - a2 * c1), a1 * b2 - a2 * b1)
        det = a1*b2 - a2*b1
        if det:
            n = Vertex((d2*b1 - d1*b2)/det, -(d2*a1 - d1*a2)/det, 0)
        else:
            det = a1*c2 - a2*c1
            if det:
                n = Vertex((d2 * c1 - d1 * c2) / det, -(d2 * a1 - d1 * a2) / det, 0)
            else:
                det = b1*c2 - b2*c1
                if det:
                    n = Vertex((d2 * c1 - d1 * c2) / det, -(d2 * b1 - d1 * b2) / det, 0)
                else:
                    return None, None

        return n, v

    def angle(self, p):

        a1, b1, c1, d1 = self.abcd()
        a2, b2, c2, d2 = p.abcd()

        #g = math.acos((a1*a2+b1*b2+c1*c2)/(math.sqrt(a1*a1 + b1*b1 + c1*c1) * math.sqrt(a2*a2 + b2*b2 + c2*c2)))
        #return 180.*g/math.pi

        ps = a1*b2 - a2*b1 + b1*c2 - b1*c2 + c1*a2 - c2*a1
        s = a1*a2 + b1*b2 + c1*c2

        print(ps)
        print(s)

        return ps/s
