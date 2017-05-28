from entities import *

def face_to_face_matrix(s, isprint):
    f = [[len(s) for x in range(len(s))] for y in range(len(s))]

    for i in range(len(s)):
        for j in range(i+1, len(s)):
            for k in range(len(s[i])):
                for l in range(len(s[j])):
                    p1, p2 = s[i][k]
                    p3, p4 = s[j][l]
                    if (p1 == p3 and p2 == p4) or (p1 == p4 and p2 == p3):
                        f[i][j] = k
                        f[j][i] = l

    if isprint:
        for row in f:
            print(row)

    return f

def face_to_edge_matrix(s, isprint):
    f = []
    for i in range(len(s)):
        l = []
        for j in range(len(s)):
            if s[i][j] != len(s):
              l.append(j)
        f.append(l)

    if isprint:
        for row in f:
            print(row)

    return f

def prefix(l):
    if l > 1:
        print("|  ", end="", sep="")
    if l > 2:
        print("   " * (l - 2), end="", sep="")


def process_entity(l, de_, pd_, e):
    pd = pd_[e["Parameter Data"]]
    etn = e["Entity Type Number"]
    prefix(l)
    print("+--", "Entity: ", entity[etn], sep="")
    # print("DE: ", e)
    # print("PD: ", pd)

    if entity[etn] == "Color Definition":
        cc1 = pd[2]
        cc2 = pd[3]
        cc3 = pd[4]
        prefix(l + 1)
        print("+--", "Red: ", cc1, "%", sep="")
        prefix(l + 1)
        print("   ", "Green: ", cc2, "%", sep="")
        prefix(l + 1)
        print("   ", "Blue: ", cc3, "%", sep="")
        return 'None', []

    if entity[etn] == "Curve on a Parametric Surface":
        crtn = pd[2]
        sptr = pd[3]
        bptr = pd[4]
        cptr = pd[5]
        pref = pd[6]
        prefix(l + 1)
        print("+--", "Way the curve has been created: ", crtn_str[crtn], sep="")
        for eee in de_:
            if eee["Sequence Number"] == sptr:
                process_entity(l + 2, de_, pd_, eee)
                break
        if bptr == "0":
            prefix(l + 1)
            print("   ", "Pointer to the curve B definition: Unspecified", sep="")
        else:
            for eee in de_:
                if eee["Sequence Number"] == bptr:
                    process_entity(l + 2, de_, pd_, eee)
                    break
        face = ""
        for eee in de_:
            if eee["Sequence Number"] == cptr:
                face = process_entity(l + 2, de_, pd_, eee)
                break
        prefix(l + 1)
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

        prefix(l + 1)
        print("+--", "Upper indexes: ", k1, ", ", k2, sep="")
        prefix(l + 1)
        print("   ", "Degree of basis function: ", m1, ", ", m2, sep="")
        prefix(l + 1)
        print("   ", "Properties: ",
              prop1__str[prop1_], ", ",
              prop2__str[prop2_], ", ",
              prop3__str[prop3_], ", ",
              prop4__str[prop4_], ", ",
              prop5__str[prop5_], sep="")

        prefix(l + 1)
        print("   ", "First knot sequence: ", end="", sep="")
        for knot in s:
            print(knot, ", ", end="", sep="")
        print()

        prefix(l + 1)
        print("   ", "Second knot sequence: ", end="", sep="")
        for knot in t:
            print(knot, ", ", end="", sep="")
        print()

        prefix(l + 1)
        print("   ", "Weights: ", end="", sep="")
        for weight in w:
            print(weight, ", ", end="", sep="")
        print()

        prefix(l + 1)
        print("   ", "Control points: ", end="", sep="")
        for control_point in cp:
            print(control_point, ", ", end="", sep="")
        print()

        prefix(l + 1)
        print("   ", "Starting/ending U parameter values: ", end="", sep="")
        for u_value in u:
            print(u_value, ", ", end="", sep="")
        print()

        prefix(l + 1)
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

        prefix(l + 1)
        print("   ", "Upper index: ", k, sep="")
        prefix(l + 1)
        print("   ", "Degree of basis functions: ", m, sep="")
        prefix(l + 1)
        print("   ", prop1_str[prop1], prop2_str[prop2], prop3_str[prop3], prop4_str[prop4], sep="")

        prefix(l + 1)
        print("   ", "Knot sequence: ", end="", sep="")
        for knot in t:
            print(knot, ", ", end="", sep="")
        print()

        prefix(l + 1)
        print("   ", "Weights: ", end="", sep="")
        for weight in w:
            print(weight, ", ", end="", sep="")
        print()

        prefix(l + 1)
        print("   ", "Control points: ", end="", sep="")
        for control_point in cp:
            print(control_point, ", ", end="", sep="")
        print()

        prefix(l + 1)
        print("   ", "Starting/ending V parameter values: ", end="", sep="")
        for v_value in v:
            print(v_value, ", ", sep="", end="")
        print()

        prefix(l + 1)
        print("   ", "Unit normal: ", norm, sep="")
        return

    if entity[etn] == "Composite Curve":
        n = int(pd[2])
        de = []
        for i in range(n):
            de.append(pd[3+i])

        prefix(l + 1)
        print("   ", "Number of entities: ", n, sep="")
        face = []
        for i in range(n):
            for eee in de_:
                if eee["Sequence Number"] == de[i]:
                    face.append(process_entity(l + 2, de_, pd_, eee))
        return face

    if entity[etn] == "Line":
        if e['Form Number'] == '0':
            p1 = {'X': float(format(float(pd[2]), '.4f')),
                  'Y': float(format(float(pd[3]), '.4f')),
                  'Z': float(format(float(pd[4]), '.4f'))}
            p2 = {'X': float(format(float(pd[5]), '.4f')),
                  'Y': float(format(float(pd[6]), '.4f')),
                  'Z': float(format(float(pd[7]), '.4f'))}
            prefix(l + 1)
            print("   ", "Form: ", e['Form Number'], sep="")
            prefix(l + 1)
            print("   ", p1, p2, sep="")
        else:
            prefix(l + 1)
            print("   ", "Not implemented yet")
        return p1, p2

    if entity[etn] == "Plane":
        if e['Form Number'] == '0':
            a = pd[2]
            b = pd[3]
            c = pd[4]
            d = pd[5]
            ptr = pd[6]
            lp = {'X': pd[7], 'Y': pd[8], 'Z': pd[9]}
            size = pd[10]

            prefix(l + 1)
            print("   ", "Form: ", form_plane_str[e['Form Number']], sep="")

            prefix(l + 1)
            print("   ", "Plane coefficients A, B, C, D: ", a, ", ", b, ", ", c, ", ", d, ", ", sep="")

            prefix(l + 1)
            print("   ", "Zero: ", ptr, sep="")

            prefix(l + 1)
            print("   ", "Coordinates of location point: ", lp, sep="")

            prefix(l + 1)
            print("   ", "Size: ", size, sep="")
        else:
            prefix(l + 1)
            print("   ", "Not implemented yet")
        return

    if entity[etn] == "Associativity Instance":
        if e["Form Number"] == "1":
            n = int(pd[2])
            de = []
            for pointer in range(n):
                de.append(pd[3+pointer])

            prefix(l + 1)
            print("+--", form_associativity_str[e['Form Number']], sep="")

            prefix(l + 1)
            print("   ", "Number of entries: ", n, sep="")
            body = []
            for i in range(n):
                for eee in de_:
                    if eee["Sequence Number"] == de[i]:
                        type, obj = process_entity(l + 2, de_, pd_, eee)
                        if type == 'face':
                            body.append(obj)
                        break
        else:
            prefix(l + 1)
            print("   ", "Not implemented yet")
        return 'Solid', body

    if entity[etn] == "Trimmed Parametric Surface":
        pts = pd[2]
        n1 = pd[3]
        n2 = pd[4]
        pt0 = pd[5]

        for eee in de_:
            if eee["Sequence Number"] == pts:
                process_entity(l + 2, de_, pd_, eee)
                break

        prefix(l + 1)
        if n1 == '0':
            print("   ", "The outer boundary is the boundary of D", sep="")
        else:
            print("   ", "The outer boundary is not the boundary of D", sep="")

        prefix(l + 1)
        print("   ", "Number of closed curves which constitute the inner boundary: ", n2, sep="")

        obj = []
        for eee in de_:
            if eee["Sequence Number"] == pt0:
                obj = process_entity(l + 2, de_, pd_, eee)
                break

        for i in range(int(n2)):
            for eee in de_:
                if eee["Sequence Number"] == pd[6+i]:
                    process_entity(l + 2, de_, pd_, eee)
                    break
        return 'face', obj

    prefix(l + 1)
    print("   ", "Not implemented yet")

                    # print("    "*l,
        # blank_status[e[8][0:2]],
        # subordinate_entity_switch[e[8][2:4]],
        # entity_use_flag[e[8][4:6]],
        # hierarchy[e[8][6:8]])

def status_number_parser(l):
    index = 0

    while index <= 6:
        token = l[index:index + 2]
        yield token
        index += 2


def pd_section_parser(l):
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


def de_section_parser(l):
    index = 0

    while index <= 160 - 8:
        token = l[index: index + 8]
        if token == "        ":
            token = "0"
        if token[0] == "D":
            token = token[1:]
        yield token.lstrip()
        index += 8


def global_section_parser(l):
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

def solid_detect(de, pd):
    level = 1
    n = 0
    s = []
    for ee in de:
        if subordinate_entity_switch_str[ee['Status Number'][2:4]] == "Independent":
            print("#", n, sep="")
            n += 1
            type, obj = process_entity(level, de, pd, ee)
            if type == 'None':
                continue
            if type == 'Solid':
                s = obj
            if type == 'face':
                s.append(obj)

    return s


def sections_detect(f):
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
    for line in f:
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

def direction(e):
    p1, p2 = e
    if p1['X'] < p2['X']:
        return 'X+'
    if p1['Y'] < p2['Y']:
        return 'Y+'
    if p1['Z'] < p2['Z']:
        return 'Z+'
    if p1['X'] > p2['X']:
        return 'X-'
    if p1['Y'] > p2['Y']:
        return 'Y-'
    if p1['Z'] > p2['Z']:
        return 'Z-'

def counter(v):
    i = v
    while True:
        yield i
        i += 1
