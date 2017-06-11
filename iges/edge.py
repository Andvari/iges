from virtex import Virtex
from direction import Direction


class Edge:
    def __init__(self, start: Virtex, end: Virtex):
        self.p = []
        self.p.append(start)
        self.p.append(end)

    #def update(self, start: Virtex, end: Virtex):
        #self.p[0].update(start)
        #self.p[1].update(end)

    def update(self, *args):
        self.p[args[0]].update(args[1], args[2])

    def points(self):
        return self.p

    def point(self, n: int):
        return self.p[n]

    def way(self):
        way = []
        if self.p[0].value('X') < self.p[1].value('X'):
            way.append(('X', '+'))
        if self.p[0].value('Y') < self.p[1].value('Y'):
            way.append(('Y', '+'))
        if self.p[0].value('Z') < self.p[1].value('Z'):
            way.append(('Z', '+'))
        if self.p[0].value('X') > self.p[1].value('X'):
            way.append(('X', '-'))
        if self.p[0].value('Y') > self.p[1].value('Y'):
            way.append(('Y', '-'))
        if self.p[0].value('Z') > self.p[1].value('Z'):
            way.append(('Z', '-'))
        return way

    def plane(self):
        p = []
        p0 = self.p[0].value()
        p1 = self.p[1].value()

        if p0['X'] == p1['X']:
            p.append(('Y', 'Z'))
        if p0['Y'] == p1['Y']:
            p.append(('X', 'Z'))
        if p0['Z'] == p1['Z']:
            p.append(('X', 'Y'))

        return p

    def print(self):
        #print(self.way(), " ", end="")
        #for coord, sign in self.way():
        #    print(coord, sign)
        print(self.p[0].value(), self.p[1].value)


    def image(self, p):
        x0 = 0
        y0 = 0
        x1 = 0
        y1 = 0
        if p == 'YZ':
            x0 = self.p[0].value('Y')
            x1 = self.p[1].value('Y')
            y0 = self.p[0].value('Z')
            y1 = self.p[1].value('Z')
        if p == 'XZ':
            x0 = self.p[0].value('X')
            x1 = self.p[1].value('X')
            y0 = self.p[0].value('Z')
            y1 = self.p[1].value('Z')
        if p == 'XY':
            x0 = self.p[0].value('X')
            x1 = self.p[1].value('X')
            y0 = self.p[0].value('Y')
            y1 = self.p[1].value('Y')

        img = []
        if x0 == x1:
            for y in range(int(min(y0, y1)), int(max(y0, y1))+1):
                img.append((x0, float(y)))
            return img

        if y0 == y1:
            for x in range(int(min(x0, x1)), int(max(x0, x1))+1):
                img.append((float(x), y0))
            return img

    def reverse(self):
        return Edge(self.p[1], self.p[0])

    def equ(self, e):
        if e.p[0].equ(self.p[0]) and e.p[1].equ(self.p[1]):
            return True
        if e.p[0].equ(self.p[1]) and e.p[1].equ(self.p[0]):
            return True
        return False

    def expand(self, way: [], bias: int):
        for c, s in way:
            if s == '+':
                self.p[1].update(c, bias)
            if s == '-':
                self.p[0].update(c, bias)

    def move(self, way: [], bias: int):
        for c, s in way:
            self.p[0].update(c, bias)
            self.p[1].update(c, bias)


