class Edge:
    def __init__(self, s, e):
        self.p1 = s
        self.p2 = e

    def update(self, s, e):
        self.p1 = s
        self.p2 = e

    def update(self, n, e):
        if n == 0:
            p1 = e
        if n == 2:
            p2 = e

    def data(self):
        return self.p1, self.p2

    def data(self, n):
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
