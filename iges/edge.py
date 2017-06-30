from vertex import Vertex
from direction import Direction
from plane import Plane
from entities import equal, inside
from line import Line


class Edge:
    def __init__(self, start: Vertex, end: Vertex):
        self.__p = []
        self.__p.append(start)
        self.__p.append(end)

    def update(self, *args):
        if len(args) == 2:
            self.__p[args[0]].update(args[1])
            return

        self.__p[args[0]].update(args[1], args[2])

    def points(self):
        return self.__p

    def point(self, n: int):
        return self.__p[n]

    def way(self):
        way = []
        if self.__p[0].value('X') < self.__p[1].value('X'):
            way.append(('X', '+'))
        if self.__p[0].value('Y') < self.__p[1].value('Y'):
            way.append(('Y', '+'))
        if self.__p[0].value('Z') < self.__p[1].value('Z'):
            way.append(('Z', '+'))
        if self.__p[0].value('X') > self.__p[1].value('X'):
            way.append(('X', '-'))
        if self.__p[0].value('Y') > self.__p[1].value('Y'):
            way.append(('Y', '-'))
        if self.__p[0].value('Z') > self.__p[1].value('Z'):
            way.append(('Z', '-'))
        return way

    def print(self):
        print("{ ", end="")
        self.__p[0].print()
        print(" }, { ", end="")
        self.__p[1].print()
        print(" }")

    def image(self, p: Plane):
        x0 = 0
        y0 = 0
        x1 = 0
        y1 = 0
        if p.parallel(Plane('YZ')):
            x0 = self.__p[0].value('Y')
            x1 = self.__p[1].value('Y')
            y0 = self.__p[0].value('Z')
            y1 = self.__p[1].value('Z')
        if p.parallel(Plane('XZ')):
            x0 = self.__p[0].value('X')
            x1 = self.__p[1].value('X')
            y0 = self.__p[0].value('Z')
            y1 = self.__p[1].value('Z')
        if p.parallel(Plane('XY')):
            x0 = self.__p[0].value('X')
            x1 = self.__p[1].value('X')
            y0 = self.__p[0].value('Y')
            y1 = self.__p[1].value('Y')

        img = []
        if equal(x0, x1):
            for y in range(int(min(y0, y1)), int(max(y0, y1))+1):
                img.append((x0, float(y)))
            return img

        if equal(y0, y1):
            for x in range(int(min(x0, x1)), int(max(x0, x1))+1):
                img.append((float(x), y0))
            return img

    def reverse(self):
        return Edge(self.__p[1], self.__p[0])

    def equ(self, e):
        if e.p[0].equ(self.__p[0]) and e.p[1].equ(self.__p[1]):
            return True
        if e.p[0].equ(self.__p[1]) and e.p[1].equ(self.__p[0]):
            return True
        return False

    def expand(self, way: [], bias: int):
        for c, s in way:
            if s == '+':
                self.__p[1].update(c, bias)
            if s == '-':
                self.__p[0].update(c, bias)

    def move(self, way: [], bias: int):
        for c, s in way:
            self.__p[0].update(c, bias)
            self.__p[1].update(c, bias)

    def intersect(self, edge, plane):
        empty = Vertex(), ""

        if plane.parallel(Plane('XY')):
            a00, b00 = self.point(0).value('X'), self.point(0).value('Y')
            a01, b01 = self.point(1).value('X'), self.point(1).value('Y')
            a10, b10 = edge.point(0).value('X'), edge.point(0).value('Y')
            a11, b11 = edge.point(1).value('X'), edge.point(1).value('Y')
        if plane.parallel(Plane('YZ')):
            a00, b00 = self.point(0).value('Y'), self.point(0).value('Z')
            a01, b01 = self.point(1).value('Y'), self.point(1).value('Z')
            a10, b10 = edge.point(0).value('Y'), edge.point(0).value('Z')
            a11, b11 = edge.point(1).value('Y'), edge.point(1).value('Z')
        if plane.parallel(Plane('XZ')):
            a00, b00 = self.point(0).value('X'), self.point(0).value('Z')
            a01, b01 = self.point(1).value('X'), self.point(1).value('Z')
            a10, b10 = edge.point(0).value('X'), edge.point(0).value('Z')
            a11, b11 = edge.point(1).value('X'), edge.point(1).value('Z')

        if equal(a00, a01) and equal(b00, b01):                             # .
            return empty

        if equal(a10, a11) and equal(b10, b11):                             #  .
            return empty

        a = 0
        b = 0

        if equal(a00, a01):                                                 # |
            if equal(a10, a11):                                             #  |
                return empty                                                   # ||
            else:
                if equal(b10, b11):                                         #  -
                    if inside(a10, a00, a11) and inside(b00, b10, b01):     # |-
                        a, b = a00, b10
                    else:
                        return empty
                else:                                                       #  /
                    k, b = self.kb(a10, b10, a11, b11)
                    y = k*a00 + b
                    if b00 <= y <= b01:                                     # |/
                        a, b = a00, y
                    else:
                        return empty
        else:
            if equal(b00, b01):                                             # -
                if equal(a10, a11):                                         #  |
                    if inside(b10, b00, b11) and inside(a00, a10, a01):     # -|
                        a, b = a10, b00
                    else:
                        return empty
                else:
                    if equal(b10, b11):                                     #  -
                        return empty                                           # --
                    else:                                                   #  /
                        k, b = self.kb(a10, b10, a11, b11)
                        x = (b00 - b) / k
                        if inside(a00, x, a01):                             # -/
                            a, b = x, b00
                        else:
                            return empty
            else:                                                           # /
                if equal(a10, a11):                                         #  |
                    k, b = self.kb(a00, b00, a01, b01)
                    y = k*b10 + b
                    if inside(b10, y, b11):                                 # /|
                        a, b = a10, y
                    else:
                        return empty
                else:
                    if equal(b10, b11):                                     #  -
                        k, b = self.kb(a00, b00, a01, b01)                  # /-
                        x = (b10-b)/k
                        if inside(a10, x, a11):
                            a, b = x, b10
                        else:
                            return empty
                    else:                                                   #  /
                        k0, b0 = self.kb(a00, b00, a01, b01)                # //
                        k1, b1 = self.kb(a10, b10, a11, b11)
                        if equal(k0, k1):
                            return empty
                        else:
                            a = (b1-b0)/(k0-k1)
                            b = k0*a + b0

        x1 = a00
        y1 = b00
        x2 = a
        y2 = b
        x3 = a11
        y3 = b11

        if ((x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)) / 2 > 0:
            s = '+'
        else:
            s = '-'

        if plane.parallel(Plane('XY')):
            return Vertex(a, b, self.point(0).value('Z')), s

        if plane.parallel(Plane('YZ')):
            return Vertex(self.point(0).value('X'), a, b), s

        if plane.parallel(Plane('XZ')):
            return Vertex(a, self.point(0).value('Y'), b), s

        return empty

    def kb(self, a0, b0, a1, b1):
        return

    def line(self):
        x0 = self.__p[0].value('X')
        y0 = self.__p[0].value('Y')
        z0 = self.__p[0].value('Z')

        x1 = self.__p[1].value('X')
        y1 = self.__p[1].value('Y')
        z1 = self.__p[1].value('Z')

        n = Vertex(x0, y0, z0)
        v = Vertex(x1-x0, y1-y0, z1-z0)
        return Line(n, v)

    def middle(self):
        x0 = self.__p[0].value('X')
        y0 = self.__p[0].value('Y')
        z0 = self.__p[0].value('Z')

        x1 = self.__p[1].value('X')
        y1 = self.__p[1].value('Y')
        z1 = self.__p[1].value('Z')

        return Vertex((x0 + x1)/2, (y0 + y1)/2, (z0 + z1)/2)

