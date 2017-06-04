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
        print(self.p1.x, self.p2.x, self.p1.y, self.p2.y, self.p1.z, self.p2.z)
        print(self.plane())
        if p == 'YZ':
            amin = min(self.p(0).y, self.p(1).y)
            amax = max(self.p(0).y, self.p(1).y)
            bmin = min(self.p(0).z, self.p(1).z)
            bmax = max(self.p(0).z, self.p(1).z)
        if p == 'XZ':
            amin = min(self.p(0).x, self.p(1).x)
            amax = max(self.p(0).x, self.p(1).x)
            bmin = min(self.p(0).z, self.p(1).z)
            bmax = max(self.p(0).z, self.p(1).z)
        if p == 'XY':
            amin = min(self.p(0).x, self.p(1).x)
            amax = max(self.p(0).x, self.p(1).x)
            bmin = min(self.p(0).y, self.p(1).y)
            bmax = max(self.p(0).y, self.p(1).y)

        img = [['.' for x in range(int(amax-amin))] for y in range(int(bmax-bmin))]

        k = (bmax - bmin)/(amax - amin)
        b = bmin - k*amin

        for x in range(amax - amin):
            img[int(k*x+b)][int(x)] = '*'

        return amin, amax, bmin, bmax, img
