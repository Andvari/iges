from vertex import Vertex
from edge import Edge
from face import Face
from direction import Direction
from entities import *
from plane import Plane

import os
import sys


class Solid:
    def __init__(self, fname, log):
        f = open(fname, "r")

        self.i = 0
        if log == 0:
            save_stdout = sys.stdout
            sys.stdout = open(os.devnull, "w")

        start_sec, global_sec, direcory_entry_sec, parameters_data_sec, terminate_sec = self.sections_detect(f)

        # print(start_sec)

        g_sec = []
        for p in self.global_section_parser(global_sec):
            g_sec.append(p)

        # print(G_sec)

        de_sec = []
        for field in direcory_entry_sec:
            de_subsec = {}
            g = self.de_section_parser(field)
            de_subsec['Entity Type Number'] = (g.__next__())
            de_subsec['Parameter Data'] = g.__next__()
            de_subsec['Structure'] = (g.__next__())
            de_subsec['Line Font Pattern'] = (g.__next__())
            de_subsec['Level'] = (g.__next__())
            de_subsec['View'] = (g.__next__())
            de_subsec['Transformation Matrix'] = (g.__next__())
            de_subsec['Label Display Assoc.'] = (g.__next__())
            de_subsec['Status Number'] = (g.__next__())
            de_subsec['Sequence Number'] = str(int(g.__next__()))
            de_subsec['Entity Type Number'] = (g.__next__())
            de_subsec['Line Weight Number'] = (g.__next__())
            de_subsec['Color Number'] = (g.__next__())
            de_subsec['Parameter Line Count'] = (g.__next__())
            de_subsec['Form Number'] = (g.__next__())
            de_subsec['Reserved'] = (g.__next__())
            de_subsec['Reserved'] = (g.__next__())
            de_subsec['Entity Label'] = (g.__next__())
            de_subsec['Entity Subscript Number'] = (g.__next__())
            de_subsec['Sequence Number2'] = str(int(g.__next__()))

            de_sec.append(de_subsec)

        pd_sec = {}
        n = self.counter(0)
        for field in parameters_data_sec:
            pd_subsec = []
            for i in self.pd_section_parser(field):
                try:
                    int(i)
                    pd_subsec.append(str(int(i)))
                except:
                    pd_subsec.append(i)
            pd_subsec.append(str(n.__next__()))
            pd_sec[pd_subsec[0]] = pd_subsec[1:]

        # print(pd_sec)

        self.faces_ = self.solid_detect(de_sec, pd_sec)

        if log == 0:
            sys.stdout = save_stdout

        f.close()

    def sections_detect(self, content):
        ss = ""
        gs = ""
        des = []
        pds = []
        ts = ""
        field = ""
        pfield = ""
        pstr = ""
        ppstr = ""
        iDE = 0
        iPD = 0
        for line in content:
            if line[72] == 'S':
                ss += line[:72]

            if line[72] == 'G':
                gs += line[:72]

            if line[72] == 'D':
                if iDE == 0:
                    field = line.replace("\n", "")
                else:
                    des.append(field + line.replace("\n", ""))
                iDE = 1 - iDE

            if line[72] == "P":
                if line.find(";") == -1:
                    pfield += line[0:64].lstrip().rstrip()
                    if iPD == 0:
                        pstr = line[73:80].lstrip() + ","
                        ppstr = line[65:72].lstrip() + ","
                    iPD += 1
                else:
                    if iPD == 0:
                        pstr = line[74:80].lstrip() + ","
                        ppstr = line[65:72].lstrip() + ","
                    pds.append(pstr + ppstr + pfield + line[:64].lstrip().rstrip())
                    pfield = ""
                    iPD = 0

            if line[72] == "T":
                ts = line
                break

        return ss, gs, des, pds, ts

    def update(self, s):
        self.faces = []
        for face in s:
            self.faces.append(face)
        self.i = 0

    def size(self):
        return len(self.faces)

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.faces_):
            self.i += 1
            return self.faces_[self.i-1]

        else:
            self.i = 0
            raise StopIteration

    def global_section_parser(self, l):
        index = 0
        token = ""

        while l[index] != ';':
            if l[index] == ',':
                yield token.lstrip()
                index += 1
                token = ""
                continue
            else:
                if l[index] == 'H':
                    index += 1
                    new_index = index + int(token)
                    token = l[index:new_index]
                    index = new_index
                    continue

            token += l[index]
            index += 1

        yield token.lstrip()

    def de_section_parser(self, l):
        index = 0

        while index <= 160 - 8:
            token = l[index: index + 8]
            if token == "        ":
                token = "0"
            if token[0] == "D":
                token = token[1:]
            yield token.lstrip()
            index += 8

    def pd_section_parser(self, l):
        index = 0
        token = ""

        while True:
            if l[index] == ';':
                break
            if l[index] == ',':
                if len(token) == 0:
                    token = "0"
                yield token
                token = ""
                index += 1
                continue
            token += l[index]
            index += 1

        if len(token) == 0:
            token = "0"

        yield token

    def counter(self, v):
        i = v
        while True:
            yield i
            i += 1

    def process_entity(self, l, de_, pd_, e):
        pd = pd_[e["Parameter Data"]]
        etn = e["Entity Type Number"]
        self.prefix(l)
        print("+--", "Entity: ", entity[etn], sep="")
        # print("DE: ", e)
        # print("PD: ", pd)

        if entity[etn] == "Color Definition":
            cc1 = pd[2]
            cc2 = pd[3]
            cc3 = pd[4]
            self.prefix(l + 1)
            print("+--", "Red: ", cc1, "%", sep="")
            self.prefix(l + 1)
            print("   ", "Green: ", cc2, "%", sep="")
            self.prefix(l + 1)
            print("   ", "Blue: ", cc3, "%", sep="")
            return 'None', []

        if entity[etn] == "Curve on a Parametric Surface":
            crtn = pd[2]
            sptr = pd[3]
            bptr = pd[4]
            cptr = pd[5]
            pref = pd[6]
            self.prefix(l + 1)
            print("+--", "Way the curve has been created: ", crtn_str[crtn], sep="")
            for eee in de_:
                if eee["Sequence Number"] == sptr:
                    self.process_entity(l + 2, de_, pd_, eee)
                    break
            if bptr == "0":
                self.prefix(l + 1)
                print("   ", "Pointer to the curve B definition: Unspecified", sep="")
            else:
                for eee in de_:
                    if eee["Sequence Number"] == bptr:
                        self.process_entity(l + 2, de_, pd_, eee)
                        break
            face = Face()
            for eee in de_:
                if eee["Sequence Number"] == cptr:
                    face = self.process_entity(l + 2, de_, pd_, eee)
                    break
            self.prefix(l + 1)
            print("   ", "Preferred representation: ", pref_str[pref], sep="")
            return face

        if entity[etn] == "Rational B-Spline Surface":
            k1 = int(pd[2])
            k2 = int(pd[3])
            m1 = int(pd[4])
            m2 = int(pd[5])
            prop1_ = pd[6]
            prop2_ = pd[7]
            prop3_ = pd[8]
            prop4_ = pd[9]
            prop5_ = pd[10]

            n1 = 1 + k1 - m1
            n2 = 1 + k2 - m2
            a = n1 + 2 * m1
            b = n2 + 2 * m2
            c = (1 + k1) * (1 + k2)

            s = []
            for i in range(a + 1):
                s.append(pd[11+i])

            t = []
            for i in range(b + 1):
                t.append(pd[11 + (a + 1) + i])

            w = []
            for i in range((k1 + 1) * (k2 + 1)):
                w.append(pd[11 + (a + 1) + (b + 1) + i])

            cp = []
            for i in range((k1 + 1) * (k2 + 1)):
                xyz = {'X': (pd[11 + (a + 1) + (b + 1) + (k1 + 1)*(k2 + 1) + i * 3 + 0]),
                       'Y': (pd[11 + (a + 1) + (b + 1) + (k1 + 1)*(k2 + 1) + i * 3 + 1]),
                       'Z': (pd[11 + (a + 1) + (b + 1) + (k1 + 1)*(k2 + 1) + i * 3 + 2])}
                cp.append(xyz)

            u = [pd[11 + (a + 1) + (b + 1) + (k1 + 1) * (k2 + 1) + (k1 + 1) * (k2 + 1) * 3 + 0],
                 pd[11 + (a + 1) + (b + 1) + (k1 + 1) * (k2 + 1) + (k1 + 1) * (k2 + 1) * 3 + 1]]

            v = [pd[11 + (a + 1) + (b + 1) + (k1 + 1) * (k2 + 1) + (k1 + 1) * (k2 + 1) * 3 + 2],
                 pd[11 + (a + 1) + (b + 1) + (k1 + 1) * (k2 + 1) + (k1 + 1) * (k2 + 1) * 3 + 3]]

            self.prefix(l + 1)
            print("+--", "Upper indexes: ", k1, ", ", k2, sep="")
            self.prefix(l + 1)
            print("   ", "Degree of basis function: ", m1, ", ", m2, sep="")
            self.prefix(l + 1)
            print("   ", "Properties: ",
                  prop1__str[prop1_], ", ",
                  prop2__str[prop2_], ", ",
                  prop3__str[prop3_], ", ",
                  prop4__str[prop4_], ", ",
                  prop5__str[prop5_], sep="")

            self.prefix(l + 1)
            print("   ", "First knot sequence: ", end="", sep="")
            for knot in s:
                print(knot, ", ", end="", sep="")
            print()

            self.prefix(l + 1)
            print("   ", "Second knot sequence: ", end="", sep="")
            for knot in t:
                print(knot, ", ", end="", sep="")
            print()

            self.prefix(l + 1)
            print("   ", "Weights: ", end="", sep="")
            for weight in w:
                print(weight, ", ", end="", sep="")
            print()

            self.prefix(l + 1)
            print("   ", "Control points: ", end="", sep="")
            for control_point in cp:
                print(control_point, ", ", end="", sep="")
            print()

            self.prefix(l + 1)
            print("   ", "Starting/ending U parameter values: ", end="", sep="")
            for u_value in u:
                print(u_value, ", ", end="", sep="")
            print()

            self.prefix(l + 1)
            print("   ", "Starting/ending V parameter values: ", end="", sep="")
            for v_value in v:
                print(v_value, ", ", end="", sep="")
            print()
            return

        if entity[etn] == "Rational B-Spline Curve":
            k = int(pd[2])
            m = int(pd[3])
            n = 1 + k - m
            a = n + 2 * m

            prop1 = pd[4]
            prop2 = pd[5]
            prop3 = pd[6]
            prop4 = pd[7]

            t = []
            for i in range(a + 1):
                t.append(pd[8 + i])

            w = []
            for i in range(k + 1):
                w.append(pd[8 + (a + 1) + i])

            cp = []
            for i in range(k + 1):
                xyz = {'X': pd[8 + (a + 1) + (k + 1) + i * 3 + 0],
                       'Y': pd[8 + (a + 1) + (k + 1) + i * 3 + 1],
                       'Z': pd[8 + (a + 1) + (k + 1) + i * 3 + 2]}
                cp.append(xyz)

            v = [pd[8 + (a + 1) + (k + 1) + (k + 1) * 3 + 0],
                 pd[8 + (a + 1) + (k + 1) + (k + 1) * 3 + 1]]

            norm = {
                'X': pd[8 + (a + 1) + (k + 1) + (k + 1) * 3 + 2],
                'Y': pd[8 + (a + 1) + (k + 1) + (k + 1) * 3 + 3],
                'Z': pd[8 + (a + 1) + (k + 1) + (k + 1) * 3 + 4]}

            self.prefix(l + 1)
            print("   ", "Upper index: ", k, sep="")
            self.prefix(l + 1)
            print("   ", "Degree of basis functions: ", m, sep="")
            self.prefix(l + 1)
            print("   ", prop1_str[prop1], prop2_str[prop2], prop3_str[prop3], prop4_str[prop4], sep="")

            self.prefix(l + 1)
            print("   ", "Knot sequence: ", end="", sep="")
            for knot in t:
                print(knot, ", ", end="", sep="")
            print()

            self.prefix(l + 1)
            print("   ", "Weights: ", end="", sep="")
            for weight in w:
                print(weight, ", ", end="", sep="")
            print()

            self.prefix(l + 1)
            print("   ", "Control points: ", end="", sep="")
            for control_point in cp:
                print(control_point, ", ", end="", sep="")
            print()

            self.prefix(l + 1)
            print("   ", "Starting/ending V parameter values: ", end="", sep="")
            for v_value in v:
                print(v_value, ", ", sep="", end="")
            print()

            self.prefix(l + 1)
            print("   ", "Unit normal: ", norm, sep="")
            return

        if entity[etn] == "Composite Curve":
            n = int(pd[2])
            de = []
            for i in range(n):
                de.append(pd[3+i])

            self.prefix(l + 1)
            print("   ", "Number of entities: ", n, sep="")
            face = []
            for i in range(n):
                for eee in de_:
                    if eee["Sequence Number"] == de[i]:
                        face.append(self.process_entity(l + 2, de_, pd_, eee))
            return face

        if entity[etn] == "Line":
            if e['Form Number'] == '0':
                p1 = Vertex(float(format(float(pd[2]), '.4f')),
                            float(format(float(pd[3]), '.4f')),
                            float(format(float(pd[4]), '.4f')))
                p2 = Vertex(float(format(float(pd[5]), '.4f')),
                            float(format(float(pd[6]), '.4f')),
                            float(format(float(pd[7]), '.4f')))
                self.prefix(l + 1)
                print("   ", "Form: ", e['Form Number'], sep="")
                self.prefix(l + 1)
                print("   ", p1.value(), p2.value(), sep="")
            else:
                self.prefix(l + 1)
                print("   ", "Not implemented yet")
            return Edge(p1, p2)

        if entity[etn] == "Plane":
            if e['Form Number'] == '0':
                a = pd[2]
                b = pd[3]
                c = pd[4]
                d = pd[5]
                ptr = pd[6]
                lp = {'X': pd[7], 'Y': pd[8], 'Z': pd[9]}
                size = pd[10]

                self.prefix(l + 1)
                print("   ", "Form: ", form_plane_str[e['Form Number']], sep="")

                self.prefix(l + 1)
                print("   ", "Plane coefficients A, B, C, D: ", a, ", ", b, ", ", c, ", ", d, ", ", sep="")

                self.prefix(l + 1)
                print("   ", "Zero: ", ptr, sep="")

                self.prefix(l + 1)
                print("   ", "Coordinates of location point: ", lp, sep="")

                self.prefix(l + 1)
                print("   ", "Size: ", size, sep="")
            else:
                self.prefix(l + 1)
                print("   ", "Not implemented yet")
            return

        if entity[etn] == "Associativity Instance":
            if e["Form Number"] == "1":
                n = int(pd[2])
                de = []
                for pointer in range(n):
                    de.append(pd[3+pointer])

                self.prefix(l + 1)
                print("+--", form_associativity_str[e['Form Number']], sep="")

                self.prefix(l + 1)
                print("   ", "Number of entries: ", n, sep="")
                body = []
                for i in range(n):
                    for eee in de_:
                        if eee["Sequence Number"] == de[i]:
                            typ, obj = self.process_entity(l + 2, de_, pd_, eee)
                            if typ == 'face':
                                body.append(Face(obj))
                            break
            else:
                self.prefix(l + 1)
                print("   ", "Not implemented yet")
            return 'Solid', body

        if entity[etn] == "Trimmed Parametric Surface":
            pts = pd[2]
            n1 = pd[3]
            n2 = pd[4]
            pt0 = pd[5]

            for eee in de_:
                if eee["Sequence Number"] == pts:
                    self.process_entity(l + 2, de_, pd_, eee)
                    break

            self.prefix(l + 1)
            if n1 == '0':
                print("   ", "The outer boundary is the boundary of D", sep="")
            else:
                print("   ", "The outer boundary is not the boundary of D", sep="")

            self.prefix(l + 1)
            print("   ", "Number of closed curves which constitute the inner boundary: ", n2, sep="")

            obj = []
            for eee in de_:
                if eee["Sequence Number"] == pt0:
                    obj = self.process_entity(l + 2, de_, pd_, eee)
                    break

            for i in range(int(n2)):
                for eee in de_:
                    if eee["Sequence Number"] == pd[6+i]:
                        self.process_entity(l + 2, de_, pd_, eee)
                        break
            return 'face', obj

        self.prefix(l + 1)
        print("   ", "Not implemented yet")

        # print("    "*l,
        # blank_status[e[8][0:2]],
        # subordinate_entity_switch[e[8][2:4]],
        # entity_use_flag[e[8][4:6]],
        # hierarchy[e[8][6:8]])

    def prefix(self, l):
        if l > 1:
            print("|  ", end="", sep="")
        if l > 2:
            print("   " * (l - 2), end="", sep="")

    def solid_detect(self, de, pd):
        level = 1
        n = 0
        s = []
        for ee in de:
            if subordinate_entity_switch_str[ee['Status Number'][2:4]] == "Independent":
                print("#", n, sep="")
                n += 1
                typ, obj = self.process_entity(level, de, pd, ee)
                if typ == 'None':
                    continue
                if typ == 'Solid':
                    s = obj
                if typ == 'face':
                    s.append(Face(obj))

        return s

    def ff(self, face: Face, edge: Edge):
        for f in self.faces_:
            for e in f:
                if e.equ(edge):
                    if f.equ(face):
                        continue
                    else:
                        return f

        return Face()

    def expand(self, face: Face, edge: Edge, way: Direction, d: int):
        for f in self.faces_:
            if f.equ(face):
                f.expand(edge, way, d)
                break

    def faces(self):
        return self.faces_

    def coincide_faces(self, planes):
        f = []
        for plane in planes:
            for face in self.faces_:
                if face.plane().coincide(plane):
                    f.append(face)
        return f

    def parallel_faces(self, planes):
        f = []
        for plane in planes:
            for face in self.faces_:
                if face.plane().parallel(plane):
                    f.append(face)
        return f

    def remove(self, face):
        updated = []
        for i in range(len(self.faces_)):
            if not self.faces_[i].equ(face):
                updated.append(self.faces_[i])
        self.faces_ = updated

    def replace(self, face_out, face_in):
        self.delete(face_out)
        self.faces_.append(face_in)

    def optimize(self, plane):
        to_remove = []
        to_append = []
        for i in range(len(self.faces_)):
            if self.faces_[i].plane().parallel(plane):
                for j in range(i+1, len(self.faces_)):
                    if self.faces_[i].orientation() == self.faces_[j].orientation():
                        f = Face()
                        for v1, v2, chain in self.faces_[i].intersect(self.faces_[j]):
                            for k in range(len(chain)):
                                if k == 0:
                                    chain[k].update(0, v1)
                                if k == len(chain)-1:
                                    chain[k].update(1, v2)
                                f.append(chain[k])
                        for v1, v2, chain in self.faces_[j].intersect(self.faces_[i]):
                            for k in range(len(chain)):
                                if k == 0:
                                    chain[k].update(0, v1)
                                if k == len(chain)-1:
                                    chain[k].update(1, v2)
                                f.append(chain[k])

                        if f.size():
                            to_remove.append(self.faces_[i])
                            to_remove.append(self.faces_[j])
                            to_append.append(f)

        for face in to_remove:
            self.remove(face)

        for face in to_append:
            self.faces_.append(face)


