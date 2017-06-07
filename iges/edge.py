from virtex import Virtex

class Edge:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def update(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def update(self, n, p):
        if n == 0:
            self.p1 = p
        if n == 1:
            self.p2 = p

    def pp(self):
        return self.p1, self.p2

    def p(self, n):
        if n == 0:
            return self.p1
        if n == 1:
            return self.p2

    def dir(self):
        d = ""
        if self.p1.x < self.p2.x:
            d += "X+"
        if self.p1.y < self.p2.y:
            d += "Y+"
        if self.p1.z < self.p2.z:
            d += "Z+"
        if self.p1.x > self.p2.x:
            d += "X-"
        if self.p1.y > self.p2.y:
            d += "Y-"
        if self.p1.z > self.p2.z:
            d += "Z-"
        return d

    def plane(self):
        p = []
        xs, ys, zs = self.p1.xyz()
        xe, ye, ze = self.p2.xyz()

        if xs == xe:
            p.append('YZ')
        if ys == ye:
            p.append('XZ')
        if zs == ze:
            p.append('XY')

        return p

    def print(self):
        print(self.dir(), " ", end="")
        if self.dir()[0] == 'X':
            print(self.p2.x - self.p1.x)
        if self.dir()[0] == 'Y':
            print(self.p2.y - self.p1.y)
        if self.dir()[0] == 'Z':
            print(self.p2.z - self.p1.z)

    def image(self, p):
        x0 = 0
        y0 = 0
        x1 = 0
        y1 = 0
        if p == 'YZ':
            x0 = self.p(0).y
            x1 = self.p(1).y
            y0 = self.p(0).z
            y1 = self.p(1).z
        if p == 'XZ':
            x0 = self.p(0).x
            x1 = self.p(1).x
            y0 = self.p(0).z
            y1 = self.p(1).z
        if p == 'XY':
            x0 = self.p(0).x
            x1 = self.p(1).x
            y0 = self.p(0).y
            y1 = self.p(1).y

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
        return Edge(self.p2, self.p1)

    def equ(self, e):
        if e.p(0).xyz() == self.p(0).xyz():
            if e.p(1).xyz() == self.p(1).xyz():
                return True

        if e.p(0).xyz() == self.p(1).xyz():
            if e.p(1).xyz() == self.p(0).xyz():
                return True

        return False


            # todo: diagonal lines