from plane import Plane
from entities import equ, ge, gt, le, lt, inside
from line import Line
from point import Point


class Edge:
    def __init__(self, start: Point, end: Point):
        self.__p = [start, end]

    def update(self, *args):
        if len(args) == 2:
            self.__p[args[0]].update(args[1])
            return

        self.__p[args[0]].update(args[1], args[2])

    def __getitem__(self, item):
        return self.__p[item]

    def __setitem__(self, key, value):
        self.__p[key] = value

    def __delitem__(self, key):
        pass

    def __str__(self):
        l = 6 - len(str(self.__p[0])) % 6
        s = ' '*2 + str(self.__p[0]) + ',' + ' '*l
        s += str(self.__p[1])
        return s

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
        if equ(x0, x1):
            for y in range(int(min(y0, y1)), int(max(y0, y1))+1):
                img.append((x0, float(y)))
            return img

        if equ(y0, y1):
            for x in range(int(min(x0, x1)), int(max(x0, x1))+1):
                img.append((float(x), y0))
            return img

    def reverse(self):
        return Edge(self.__p[1], self.__p[0])

    def __eq__(self, e):
        return (self.point(0) == e.point(0) and self.point(1) == e.point(1)) or \
               (self.point(0) == e.point(1) and self.point(1) == e.point(0))

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

    '''
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

        if equ(a00, a01) and equ(b00, b01):                             # .
            return empty

        if equ(a10, a11) and equ(b10, b11):                             #  .
            return empty

        a = 0
        b = 0

        if equ(a00, a01):                                                 # |
            if equ(a10, a11):                                             #  |
                return empty                                                   # ||
            else:
                if equ(b10, b11):                                         #  -
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
            if equ(b00, b01):                                             # -
                if equ(a10, a11):                                         #  |
                    if inside(b10, b00, b11) and inside(a00, a10, a01):     # -|
                        a, b = a10, b00
                    else:
                        return empty
                else:
                    if equ(b10, b11):                                     #  -
                        return empty                                           # --
                    else:                                                   #  /
                        k, b = self.kb(a10, b10, a11, b11)
                        x = (b00 - b) / k
                        if inside(a00, x, a01):                             # -/
                            a, b = x, b00
                        else:
                            return empty
            else:                                                           # /
                if equ(a10, a11):                                         #  |
                    k, b = self.kb(a00, b00, a01, b01)
                    y = k*b10 + b
                    if inside(b10, y, b11):                                 # /|
                        a, b = a10, y
                    else:
                        return empty
                else:
                    if equ(b10, b11):                                     #  -
                        k, b = self.kb(a00, b00, a01, b01)                  # /-
                        x = (b10-b)/k
                        if inside(a10, x, a11):
                            a, b = x, b10
                        else:
                            return empty
                    else:                                                   #  /
                        k0, b0 = self.kb(a00, b00, a01, b01)                # //
                        k1, b1 = self.kb(a10, b10, a11, b11)
                        if equ(k0, k1):
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
    '''
    '''
    def kb(self, a0, b0, a1, b1):
        return
    '''

    def line(self):
        return Line(self[0], self[1])

    def middle(self):
        return self[0].middle(self[1])

    def opposite_vertex(self, p):
        if self[0] == p:
            return self[1]

        if self[1] == p:
            return self[0]

        return None

    def is_inner_point(self, p: Point):
        g = self.gradient()[0]
        p0, p1 = self

        if not self.coincide(Edge(p0, p)):
            return False

        if (p[g] < p0[g] and p[g] < p1[g]) or (p[g] > p0[g] and p[g] > p1[g]):
            return False

        return True

    def intersect_point(self, param):
        #l1 = Line(self.point(0), self.point(1).vector(self.point(1)))

        if type(param) is Edge:
            l = param.line()
        elif type(param) is Line:
            l = param
        else:
            raise ValueError('Edge intersect_point(): param not Edge or Line')

        x0, y0, z0 = self.line().point()
        x1, y1, z1 = l.point()

        p00, p01, p02 = self.line().vector()
        p10, p11, p12 = l.vector()

        '''
        print(self.line().point(), end ="")
        print(self.line().vector())
        print(l.point(), end="")
        print(l.vector())
        '''

        if p00:
            if p01*p10/p00 - p11:
                s = (y1-y0-(p01*(x1-x0))/p00)/(p01*p10/p00 - p11)
            elif p02*p10/p00 - p12:
                s = (z1-z0-(p02*(x1-x0))/p00)/(p02*p10/p00 - p12)
            else:
                return None

        elif p01:
            if p00*p11/p01 - p10:
                s = (x1-x0-(p00*(y1-y0))/p01)/(p00*p11/p01 - p10)
            elif p02*p11/p01 - p12:
                s = (z1-z0-(p02*(y1-y0))/p01)/(p02*p11/p01 - p12)
            else:
                return None

        elif p02:
            if p00*p12/p02 - p10:
                s = (x1-x0-(p00*(z1-z0))/p02)/(p00*p12/p02 - p10)
            elif p01*p12/p02 - p11:
                s = (y1-y0-(p01*(z1-z0))/p02)/(p01*p12/p02 - p11)
            else:
                return None

        else:
            return None

        x = p10 * s + x1
        y = p11 * s + y1
        z = p12 * s + z1

        #print(Point(x, y, z))
        #print('---')

        return Point(x, y, z)

    def gradient(self):
        return self.line().gradient()

    def dxdydz(self):
        return self.__p[1] - self.__p[0]

    def coincide(self, e):
        return self.line().coincide(e.line())

    def intersect_pieces(self, edges: []):
        g = self.gradient()[0]

        ss = self.point(0).value(g)
        se = self.point(1).value(g)
        pieces = []
        for e in edges:
            ts = e.point(0).value(g)
            te = e.point(1).value(g)

            if ss >= te or se <= ts:
                continue

            if ss >= ts:
                ns = self.point(0)
            else:
                ns = e.point(0)

            if se <= te:
                ks = self.point(1)
            else:
                ks = e.point(1)

            pieces.append(Edge(ns, ks))

        return pieces

    def sorted_along_gradient(self, g):
        s = min(self.point(0).value(g), self.point(1).value(g))
        e = max(self.point(0).value(g), self.point(1).value(g))
        return s, e

    def middle(self):
        p0 = self.__p[0]
        p1 = self.__p[1]
        return Point((p1['X'] - p0['X']) / 2, (p1['Y'] - p0['Y']) / 2, (p1['Z'] - p0['Z']) / 2)
