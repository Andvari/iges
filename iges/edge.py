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
