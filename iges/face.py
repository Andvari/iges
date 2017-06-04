from edge import Edge
from entities import cw, ccw, acw, accw


class Face:
    def __init__(self, f : []):
        self.edges = []
        for e in f:
            self.edges.append(e)

    def __init__(self):
        self.edges = []

    def append(self, e):
        self.edges.append(e)

    def edges(self):
        return self.edges

    def virtexes(self):
        r = []
        for edge in self.edges:
            r.append(edge.p(0))
        return r

    def size(self):
        return len(self.edges)

    def anomalies(self):
        m = []
        for edge in self.edges:
            m.append(edge.dir())

        vote_cw = 0
        vote_ccw = 0
        a_cw = []
        a_ccw = []
        for e in range(len(m)-2):
            route = m[e+0] + m[(e+1) % len(m)] + m[(e+2) % len(m)]
            if route == cw['X'][0] or route == cw['X'][1]:
                vote_cw += 1
            if route == cw['Y'][0] or route == cw['Y'][1]:
                vote_cw += 1
            if route == cw['Z'][0] or route == cw['Z'][1]:
                vote_cw += 1
            if route == ccw['X'][0] or route == ccw['X'][1]:
                vote_ccw += 1
            if route == ccw['Y'][0] or route == ccw['Y'][1]:
                vote_ccw += 1
            if route == ccw['Z'][0] or route == ccw['Z'][1]:
                vote_ccw += 1

            route = m[e+0] + m[(e+1)%len(m)]

            if route == acw['X'][0] or route == acw['X'][1] or route == acw['X'][2] or route == acw['X'][3]:
                a_cw.append((e, e+1))
            if route == acw['Y'][0] or route == acw['Y'][1] or route == acw['Y'][2] or route == acw['Y'][3]:
                a_cw.append((e, e+1))
            if route == acw['Z'][0] or route == acw['Z'][1] or route == acw['Z'][2] or route == acw['Z'][3]:
                a_cw.append((e, e+1))

            if route == accw['X'][0] or route == accw['X'][1] or route == accw['X'][2] or route == accw['X'][3]:
                a_ccw.append((e, e+1))
            if route == accw['Y'][0] or route == accw['Y'][1] or route == accw['Y'][2] or route == accw['Y'][3]:
                a_ccw.append((e, e+1))
            if route == accw['Z'][0] or route == accw['Z'][1] or route == accw['Z'][2] or route == accw['Z'][3]:
                a_ccw.append((e, e+1))

        if vote_cw > vote_ccw:
            return a_cw
        else:
            return a_ccw

    def plane(self):
        xy = 0
        yz = 0
        xz = 0
        for e in self.edges:
            for p in e.plane():
                if p == 'XY':
                    xy += 1
                if p == 'YZ':
                    yz += 1
                if p == 'XZ':
                    xz += 1

        p = ""
        if xy == len(self.edges):
            p += "XY"
        if yz == len(self.edges):
            p += "YZ"
        if xz == len(self.edges):
            p += "XZ"

        return p

    def print(self):
        for e in self.edges:
            e.print()
        print('---------')

    def image(self, p):
        for e in self.edges:
            xmin, xmax, ymin, ymax, img = e.image(p)
            print(xmin, xmax, ymin, ymax)
