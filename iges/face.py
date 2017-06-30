from edge import Edge
from entities import cw, ccw, acw, accw
from entities import ORIENTATION_CW, ORIENTATION_CCW, ORIENTATION_UNKNOWN
from image import Image
from vertex import Vertex
from direction import Direction
from plane import Plane
from line import Line


class Face:
    def __init__(self, *args):
        self.i = 0
        self.__edges = []
        self.orient = ORIENTATION_UNKNOWN
        if len(args) == 0:
            return

        if len(args) == 1:
            i = 0
            for e in args[0]:
                i += 1
                self.__edges.append(e)

    def append(self, e: Edge):
        self.__edges.append(e)

    def edges(self):
        return self.__edges

    def virtexes(self):
        r = []
        for edge in self.__edges:
            r.append(edge.p(0))
        return r

    def size(self):
        return len(self.__edges)

    def orientation(self):
        m = []
        for edge in self.__edges:
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
        for edge in self.__edges:
            c, s = edge.way()[0]
            m.append(c+s)

        a_cw = []
        a_ccw = []
        for e in range(len(m)-2):
            route = m[e+0] + m[(e+1)%len(m)]

            if route == acw['X'][0] or route == acw['X'][1] or route == acw['X'][2] or route == acw['X'][3]:
                a_cw.append((self.__edges[e], self.__edges[e+1]))
            if route == acw['Y'][0] or route == acw['Y'][1] or route == acw['Y'][2] or route == acw['Y'][3]:
                a_cw.append((self.__edges[e], self.__edges[e+1]))
            if route == acw['Z'][0] or route == acw['Z'][1] or route == acw['Z'][2] or route == acw['Z'][3]:
                a_cw.append((self.__edges[e], self.__edges[e+1]))

            if route == accw['X'][0] or route == accw['X'][1] or route == accw['X'][2] or route == accw['X'][3]:
                a_ccw.append((self.__edges[e], self.__edges[e+1]))
            if route == accw['Y'][0] or route == accw['Y'][1] or route == accw['Y'][2] or route == accw['Y'][3]:
                a_ccw.append((self.__edges[e], self.__edges[e+1]))
            if route == accw['Z'][0] or route == accw['Z'][1] or route == accw['Z'][2] or route == accw['Z'][3]:
                a_ccw.append((self.__edges[e], self.__edges[e+1]))

        if self.orient == ORIENTATION_CW:
            return a_cw
        else:
            return a_ccw

    def plane(self):
        return Plane([self.__edges[0].point(0), self.__edges[0].point(1), self.__edges[1].point(1)])

    def mirror(self):
        t = list(reversed(self.__edges))
        self.__edges = t
        for e in self.__edges:
            e.reverse()

    def print(self, *args):

        if len(args) == 0:
            for e in self.__edges:
                e.print()
            return
        self.__edges[args[0]].print()

    def image(self, p):
        img = []
        for e in self.__edges:
            img += e.image(p)
        return Image(img)

    def equ(self, face):
        if len(self.__edges) != len(face.edges()):
            return False

        n = 0
        for i in range(len(self.edges())):
            for j in range(len(face.edges())):
                if self.edges()[i].equ(face.edges()[j]):
                    n += 1
                    break

        if n == len(self.__edges):
            return True

        return False

    def expand(self, edge: Edge, way: Direction, d: int):
        if len(self.__edges) == 0:
            return

        for i in range(len(self.__edges)):
            if self.__edges[i].equ(edge):
                idx = i
                break

        if self.__edges[idx].way() == way:
            x = self.__edges[idx].point(1).value('X')
            y = self.__edges[idx].point(1).value('Y')
            z = self.__edges[idx].point(1).value('Z')
            for c, s in way:
                if s == '-':
                    d = -d
                self.__edges[(idx + 0) % len(self.__edges)].update(1, c, d)
                self.__edges[(idx + 1) % len(self.__edges)].update(0, c, d)
                self.__edges[(idx + 1) % len(self.__edges)].update(1, c, d)
                self.__edges[(idx + 2) % len(self.__edges)].update(0, c, d)
        else:
            x = self.__edges[idx].point(0).value('X')
            y = self.__edges[idx].point(0).value('Y')
            z = self.__edges[idx].point(0).value('Z')
            for c, s in way:
                if s == '-':
                    d = -d
                self.__edges[(idx - 0) % len(self.__edges)].update(0, c, d)
                self.__edges[(idx - 1) % len(self.__edges)].update(1, c, d)
                self.__edges[(idx - 1) % len(self.__edges)].update(0, c, d)
                self.__edges[(idx - 2) % len(self.__edges)].update(1, c, d)

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.__edges):
            self.i += 1
            return self.__edges[self.i-1]

        else:
            self.i = 0
            raise StopIteration

    def coordinate(self, p):
        m = -1e6
        for e in self.__edges:
            m = max(m, e.point(0).value(p))
            m = max(m, e.point(1).value(p))
        return m

    def intersect(self, face):
        if not self.plane().coincide(face.plane()):
            return []

        if self.orientation() == ORIENTATION_CW:
            sign_in = '-'
            sign_out = '+'
        else:
            sign_in = '+'
            sign_out = '-'

        m = len(self.edges())
        mm = len(face.edges())

        cross_points = []
        v_in = Vertex()
        v_out = Vertex()
        chain = []
        chains = []
        for i in range(m):
            for j in range(mm):
                v_in, s = self.__edges[i].intersect(face.edges_[j], face.plane())
                if s == sign_out:
                    chain = []
                    exit_flag = False
                    for k in range(mm):
                        chain.append(face.edges_[(j + k) % mm])
                        for l in range(m):
                            v_out, s = self.__edges[(i+l) % m].intersect(face.edges_[(j+k) % mm], face.plane())
                            if s == sign_in:
                                if chain:
                                    chains.append((v_in, v_out, chain))
                                exit_flag = True
                                break
                        if exit_flag:
                            break
        return chains

    def point_out_of_line(self, l: Line):
        for p in self.__edges:
            if not l.belong(p.point(0)):
                return p.point(0)
            if not l.belong(p.point(1)):
                return p.point(1)

        print("No points founded")

    def hull(self, f):
        p1 = self.plane()
        p1.print()
        p2 = f.plane()
        p2.print()
        l = p1.intersect(p2)
        if l:
            l.print()
            p = f.point_out_of_line(l)
            return p1.angle(l, p)
        return "Planes is parallel"

    def intersect_line(self, f):
        return self.plane().intersect(f.plane())

    def coincide_edges(self, l: Line):
        edges = []
        for e in self.__edges:
            if e.line().coincide(l):
                edges.append(e)
        return edges

    def inside_point(self):

        e = self.__edges[0]
        m = e.middle()
        l = Line(m, e.line().vector().vect_mult(self.plane().vector()))

        ip = []
        for e in self.__edges:
            if not e.line().coincide(l):
                p = e.line().intersect(l)
                p0 = e.point(0)
                p1 = e.point(1)

                d0 = p.distance(p0)
                d1 = p.distance(p1)
                d01 = p0.distance(p1)

                if d01 >= d0 and d01 >= d1:
                    ip.append(p)

                if ip:
                    xmin = 1e9
                    t1 = Vertex()
                    for p in ip:
                        if xmin >= p.value('X'):
                            xmin = p.value('X')
                            t1 = p
                    ip.remove(t1)

                    xmin = 1e9
                    t2 = Vertex()
                    for p in ip:
                        if xmin >= p.value('X'):
                            xmin = p.value('X')
                            t2 = p

                    x0 = t1.value('X')
                    y0 = t1.value('Y')
                    z0 = t1.value('Z')

                    x1 = t2.value('X')
                    y1 = t2.value('Y')
                    z1 = t2.value('Z')

                    return Vertex((x0+x1)/2, (y0+y1)/2, (z0+z1)/2)

        return None

    def is_inside_point(self, p: Vertex):
        pass

