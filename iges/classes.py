class Virtex:
    def __init__(self, nx, ny, nz):
        self.x = nx
        self.y = ny
        self.z = nz

    def update(self, nx, ny, nz):
        self.x = nx
        self.y = ny
        self.z = nz

    def get(self):
        return self.x, self.y, self.z

class Edge:
    def __init__(self, s, e):
        self.p1 = s
        self.p2 = e

    def update(self, s, e):
        self.p1 = s
        self.p2 = e

    def get(self):
        return self.p1, self.p2

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

class Face:
    def __init__(self, e):
        self.e = e

    def update(self, e):
        self.e = e

    def edges(self):
        return self.e

    def virtexes(self):
        r = []
        for v in self.e:
            p1, p2 = v.get()
            r.append(p1)
        return r

    def append(self, e):
        self.e.append(e)

    def remove(self, e):
        for edge in self.e:
            if edge == e:
