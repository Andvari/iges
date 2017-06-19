from edge import Edge
from entities import cw, ccw, acw, accw
from entities import ORIENTATION_CW, ORIENTATION_CCW, ORIENTATION_UNKNOWN
from image import Image
from virtex import Virtex
from direction import Direction
from plane import Plane

class Face:
    def __init__(self, *args):
        self.i = 0
        self.edges_ = []
        self.orient = ORIENTATION_UNKNOWN
        if len(args) == 0:
            return

        if len(args) == 1:
            i = 0
            for e in args[0]:
                i += 1
                self.edges_.append(e)

    def append(self, e: Edge):
        self.edges_.append(e)

    def edges(self):
        return self.edges_

    def virtexes(self):
        r = []
        for edge in self.edges_:
            r.append(edge.p(0))
        return r

    def size(self):
        return len(self.edges_)

    def orientation(self):
        m = []
        for edge in self.edges_:
            c, s = edge.way()[0]
            m.append(c+s)

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

        if vote_cw > vote_ccw:
            self.orient = ORIENTATION_CW
        else:
            self.orient = ORIENTATION_CCW

        return self.orient

    def anomalies(self):

        if self.orient == ORIENTATION_UNKNOWN:
            self.orientation()

        m = []
        for edge in self.edges_:
            c, s = edge.way()[0]
            m.append(c+s)

        a_cw = []
        a_ccw = []
        for e in range(len(m)-2):
            route = m[e+0] + m[(e+1)%len(m)]

            if route == acw['X'][0] or route == acw['X'][1] or route == acw['X'][2] or route == acw['X'][3]:
                a_cw.append((self.edges_[e], self.edges_[e+1]))
            if route == acw['Y'][0] or route == acw['Y'][1] or route == acw['Y'][2] or route == acw['Y'][3]:
                a_cw.append((self.edges_[e], self.edges_[e+1]))
            if route == acw['Z'][0] or route == acw['Z'][1] or route == acw['Z'][2] or route == acw['Z'][3]:
                a_cw.append((self.edges_[e], self.edges_[e+1]))

            if route == accw['X'][0] or route == accw['X'][1] or route == accw['X'][2] or route == accw['X'][3]:
                a_ccw.append((self.edges_[e], self.edges_[e+1]))
            if route == accw['Y'][0] or route == accw['Y'][1] or route == accw['Y'][2] or route == accw['Y'][3]:
                a_ccw.append((self.edges_[e], self.edges_[e+1]))
            if route == accw['Z'][0] or route == accw['Z'][1] or route == accw['Z'][2] or route == accw['Z'][3]:
                a_ccw.append((self.edges_[e], self.edges_[e+1]))

        if self.orient == ORIENTATION_CW:
            return a_cw
        else:
            return a_ccw

    def plane(self):
        return Plane([self.edges_[0].point(0), self.edges_[0].point(1), self.edges_[1].point(1)])

    def mirror(self):
        t = list(reversed(self.edges_))
        self.edges_ = t
        for e in self.edges_:
            e.reverse()

    def print(self):
        for e in self.edges_:
            e.print()
        print('---------')

    def image(self, p):
        img = []
        for e in self.edges_:
            img += e.image(p)
        return Image(img)

    def equ(self, face):
        if len(self.edges_) != len(face.edges()):
            return False

        n = 0
        for i in range(len(self.edges())):
            for j in range(len(face.edges())):
                if self.edges()[i].equ(face.edges()[j]):
                    n += 1
                    break

        if n == len(self.edges_):
            return True

        return False

    def expand(self, edge: Edge, way: Direction, d: int):
        if len(self.edges_) == 0:
            return

        for i in range(len(self.edges_)):
            if self.edges_[i].equ(edge):
                idx = i
                break

        if self.edges_[idx].way() == way:
            x = self.edges_[idx].point(1).value('X')
            y = self.edges_[idx].point(1).value('Y')
            z = self.edges_[idx].point(1).value('Z')
            for c, s in way:
                if s == '-':
                    d = -d
                self.edges_[(idx + 0) % len(self.edges_)].update(1, c, d)
                self.edges_[(idx + 1) % len(self.edges_)].update(0, c, d)
                self.edges_[(idx + 1) % len(self.edges_)].update(1, c, d)
                self.edges_[(idx + 2) % len(self.edges_)].update(0, c, d)
        else:
            x = self.edges_[idx].point(0).value('X')
            y = self.edges_[idx].point(0).value('Y')
            z = self.edges_[idx].point(0).value('Z')
            for c, s in way:
                if s == '-':
                    d = -d
                self.edges_[(idx - 0) % len(self.edges_)].update(0, c, d)
                self.edges_[(idx - 1) % len(self.edges_)].update(1, c, d)
                self.edges_[(idx - 1) % len(self.edges_)].update(0, c, d)
                self.edges_[(idx - 2) % len(self.edges_)].update(1, c, d)

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.edges_):
            self.i += 1
            return self.edges_[self.i-1]

        else:
            self.i = 0
            raise StopIteration

    def coordinate(self, p):
        m = -1e6
        for e in self.edges_:
            m = max(m, e.point(0).value(p))
            m = max(m, e.point(1).value(p))
        return m

    def cross(self, face):
        if not self.plane().coincide(face.plane()):
            return {}

        i=1
        cross_points = []
        for e in self.edges_:
            j=1
            print(i,)
            for ee in face.edges():
                print("  ", j)
                j += 1
                if e.cross(ee, face.plane()):
                    cross_points.append(e.cross(ee, face.plane()))
            i += 1

        return cross_points
