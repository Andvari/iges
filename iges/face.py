from edge import Edge
from entities import cw, ccw, acw, accw
from entities import ORIENTATION_CW, ORIENTATION_CCW, ORIENTATION_UNKNOWN
from image import Image
from vertex import Vertex
from direction import Direction
from plane import Plane
from line import Line
#from entities import equ, ge, gt, le, lt


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

    def vertexes(self):
        r = []
        for e in self.__edges:
            r.append(e.point(0))
        return r

    def size(self):
        return len(self.__edges)

    def __eq__(self, f):

        if not self.size() == f.size():
            return False

        for p in self.vertexes():
            found = False
            for pp in f.vertexes():
                if p == pp:
                    found = True
                    break
            if not found:
                return False

        return True

    def plane(self):
        return Plane([self.__edges[0].point(0), self.__edges[0].point(1), self.__edges[1].point(1)])

    def mirror(self):
        ne = []
        for e in self.__edges:
            ne.append(e.reverse())
        self.__edges = list(reversed(ne))

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

    '''
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
    '''

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

    '''
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
    '''

    def point_out_of_line(self, l: Line):
        for p in self.vertexes():
            if not l.belong(p):
                return p
        return None

    def hull(self, f):
        for e in self.edges():
            for ee in f.edges():
                if e.coincide(ee):
                    ff = Face([e, ee])
                    ff.sort(e.gradient()[0])
                    p11 = ff.edges()[0].point(0).value(e.gradient()[0])
                    p12 = ff.edges()[0].point(1).value(e.gradient()[0])
                    p21 = ff.edges()[1].point(0).value(e.gradient()[0])
                    if p11 <= p21 < p12:
                        return self.plane().angle(e.line(), f.point_out_of_line(e.line()))
        return None

    def intersect_line(self, f):
        return self.plane().intersect_line(f.plane())

    def intersect_point(self, l):
        ip = self.plane().intersect_point(l)
        if ip is not None:
            if self.is_inner_point(ip):
                return ip
        return None

    def edges_along_line(self, l: Line):
        edges = []
        for e in self.__edges:
            if e.line().coincide(l):
                edges.append(e)

        return edges

    def cross_points(self, param):

        if type(param) is Edge:
            l = param.line()
        elif type(param) is Line:
            l = param
        else:
            print('Type not defined')

        ip = []
        for e in self.__edges:
            p = e.intersect_point(l)
            if p is not None:
                p0, p1 = e.points()

                if p == p0:
                    e1, e2 = self.edges_with_common_vertex(p0)
                    p0n = e1.opposite_vertex(p0)
                    p1 = e2.opposite_vertex(p0)
                    p0 = p0n
                elif p == p1:
                    e1, e2 = self.edges_with_common_vertex(p1)
                    p0n = e1.opposite_vertex(p1)
                    p1 = e2.opposite_vertex(p1)
                    p0 = p0n

                ppp = Edge(p0, p1).intersect_point(l)
                if ppp is not None:
                    if Edge(p0, p1).is_inner_point(ppp):
                        found = False
                        for pp in ip:
                            if pp == p:
                                found = True
                                break
                        if not found:
                            ip.append(p)

        if type(param) is Edge:
            for p in ip:
                if e.is_inner_point(p):
                    return p
            return None
        return ip

    def inner_point(self):
        p0 = self.vertexes()[0]
        if self.size() == 3:
            p1 = self.vertexes()[1].middle(self.vertexes()[2])
        else:
            p1 = max(self.vertexes(), key=lambda x: x.distance(p0))

        ip = self.cross_points(Line(p0, p0.vector(p1)))
        t0 = min(ip, key=lambda x: x.distance(ip[0]))
        ip.remove(t0)
        t1 = min(ip, key=lambda x: x.distance(ip[0]))

        return t0.middle(t1)

    def edges_with_common_vertex(self, p: Vertex):
        ee = []
        for e in self.__edges:
            if e.point(0) == p or e.point(1) == p:
                ee.append(e)
        return ee[0], ee[1]

    def is_inner_point(self, p: Vertex):
        p0 = self.vertexes()[0]
        if p == p0:
            p0 = max(self.vertexes(), key=lambda x: x.distance(p0))

        ip = self.cross_points(Line(p0, p0.vector(p)))
        ip.sort(key=lambda x: x.distance(p0))

        if ip:
            r = True
            for i in range(1, len(ip)):
                if Edge(ip[i-1], ip[i]).is_inner_point(p):
                    break
                r = not r

            return r

        return False

    def coincide_abcd(self, p: Vertex):
        return self.plane().coincide_abcd(p)

    def sort(self, sort_direction):

        for i in range(len(self.__edges)):
            e = self.__edges[i]
            if e.point(0).value(sort_direction) >= e.point(1).value(sort_direction):
                self.__edges[i] = e.reverse()

        self.edges().sort(key=lambda x: x.point(0).value(sort_direction))

        return

    def abcd(self):
        return self.plane().abcd()

    def merge(self, face):
        nf1 = Face()
        v, n = self.abcd()
        for e in self.edges():
            p0, p1 = e.points()
            if face.is_inner_point(p0) and face.is_inner_point(p1):
                continue

            if not face.is_inner_point(p0) and not face.is_inner_point(p1):
                nf1.append(e)
                continue

            cp = face.cross_points(e)

            if type(cp) is Vertex:
                face.print()
                e.print()
                cp.print(' cp\n')
                if not face.is_inner_point(p0):
                    nf1.append(Edge(p0, cp))
                    continue

                if not face.is_inner_point(p1):
                    nf1.append(Edge(cp, p1))

        nf2 = Face()
        v, n = face.abcd()
        for e in face.edges():
            g = e.gradient()[0]
            p0, p1 = e.points()
            if self.is_inner_point(p0) and self.is_inner_point(p1):
                continue

            if not self.is_inner_point(p0) and not self.is_inner_point(p1):
                nf2.append(e)
                continue

            cp = self.cross_points(e)

            if type(cp) is Vertex:
                #self.print()
                #e.print()
                #cp.print(' cp\n')
                if not self.is_inner_point(p0):
                    nf2.append(Edge(p0, cp))
                    continue

                if not self.is_inner_point(p1):
                    nf2.append(Edge(cp, p1))

        v, n = self.abcd()
        vv, n = nf2.abcd()
        if Edge(v, vv).is_inner_point(Vertex(0, 0, 0)):
            nf2.mirror()

        print('-')
        for e in nf1:
            e.print()
        print('--')
        for e in nf2:
            e.print()
        print('---')
        return nf1
