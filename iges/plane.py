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
        a0, b0, c0, d0 = self.abcd()
        a1, b1, c1, d1 = plane.abcd()

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
        v0, d0 = self.abcd()
        v1, d1 = p.abcd()

        a0, b0, c0 = v0.value()
        a1, b1, c1 = v1.value()

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

        x0, y0, z0 = self.__p[0].value()
        x1, y1, z1 = self.__p[1].value()
        x2, y2, z2 = self.__p[2].value()

        k1 = (z2 - z0) * (y1 - y0) - (z1 - z0) * (y2 - y0)
        k2 = (z2 - z0) * (x1 - x0) - (z1 - z0) * (x2 - x0)
        k3 = (y2 - y0) * (x1 - x0) - (y1 - y0) * (x2 - x0)

        a = k1
        b = -k2
        c = k3
        d = -k1*x0 + k2*y0 - k3*z0

        return Vertex(a, b, c), d

    def print(self):
        v, d = self.abcd()
        for point in self.__p:
            print(point.value('X'), point.value('Y'), point.value('Z'))
        a, b, c = v.value()
        print("abcd: ", a, b, c, d)
        print('--------------')

    def intersect_line(self, p):

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
                    return None

        return Line(n, v)

    def angle(self, l: Line, p2: Vertex):

        a, b, c, d = self.abcd()

        x0 = a + l.point().value('X')
        y0 = b + l.point().value('Y')
        z0 = c + l.point().value('Z')

        x1, y1, z1 = p2.value()

        l = Line(Vertex(x0, y0, z0), Vertex(x1-x0, y1-y0, z1-z0))

        p = self.intersect_point(l)

        if p:
            x, y, z = p.value()

            l1 = Vertex(x0, y0, z0).distance(Vertex(x1, y1, z1))
            l2 = Vertex(x0, y0, z0).distance(Vertex(x, y, z))

            if l1 > l2:
                return 'Concave'
            else:
                return 'Convex'

        return 'Concave'

    def vector(self):
        a, b, c, d = self.abcd()
        return Vertex(a, b, c)

    def intersect_point(self, l: Line):

        v, d = self.abcd()
        v1 = l.vector()
        a, b, c = v.value()

        if abs(v.scalar_mult(v1)) < PRECISION:
            return None

        x0, y0, z0 = l.point().value()
        dx, dy, dz = l.vector().value()

        if dx and dy and dz:
            y = (a*y0*dx/dy - a*x0 + c*y0*dz/dy - c*z0 - d)/(a*dx/dy + b + c*dz/dy)
            x = (y-y0)*dx/dy + x0
            z = (y-y0)*dz/dy + z0

        if not dx and dy and dz:
            x = x0
            z = (-a*x0 + z0*b*dy/dz - b*y0 - d)/(b*dy/dz + c)
            y = (z-z0)*dy/dz + y0

        if dx and not dy and dz:
            y = y0
            z = (z0*a*dz/dz - a*x0 - b*y0 - d)/(a*dx/dz + c)
            x = (z-z0)*dx/dz + x0

        if dx and dy and not dz:
            z = z0
            y = (y0*a*dx/dy - a*x0 - c*z0 - d)/(a*dx/dy + b)
            x = (y-y0)*dx/dy + x0

        if not dx and not dy and dz:
            x = x0
            y = y0
            z = -(a*x0 + b*y0 + d)/c

        if not dx and dy and not dz:
            x = x0
            z = z0
            y = -(a * x0 + c * z0 + d) / b

        if dx and not dy and not dz:
            y = y0
            z = z0
            x = -(b * y0 + c * z0 + d) / a

        if not dx and not dy and not dz:
            x = x0
            y = y0
            z = z0

        return Vertex(x, y, z)
