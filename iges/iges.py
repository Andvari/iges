from entities import *

#f = open("cube_fc.iges", "r")

f = open("cube.IGS", "r")


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
        facet = ""
        for eee in de_:
            if eee["Sequence Number"] == cptr:
                facet = process_entity(l + 2, de_, pd_, eee)
                break
        prefix(l + 1)
        print("   ", "Preferred representation: ", pref_str[pref], sep="")
        return facet

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
        for i in range(0, a + 1):
            s.append(pd[11+i])

        t = []
        for i in range(0, b + 1):
            t.append(pd[11 + (a + 1) + i])

        w = []
        for i in range(0, (k1 + 1) * (k2 + 1)):
            w.append(pd[11 + (a + 1) + (b + 1) + i])

        cp = []
        for i in range(0, (k1 + 1) * (k2 + 1)):
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
        for i in range(0, a + 1):
            t.append(pd[8 + i])

        w = []
        for i in range(0, k + 1):
            w.append(pd[8 + (a + 1) + i])

        cp = []
        for i in range(0, k + 1):
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
        for i in range(0, n):
            de.append(pd[3+i])

        prefix(l + 1)
        print("   ", "Number of entities: ", n, sep="")
        facet = []
        for i in range(0, n):
            for eee in de_:
                if eee["Sequence Number"] == de[i]:
                    facet.append(process_entity(l + 2, de_, pd_, eee))
        return facet

    if entity[etn] == "Line":
        if e['Form Number'] == '0':
            p1 = {'X': pd[2], 'Y': pd[3], 'Z': pd[4]}
            p2 = {'X': pd[5], 'Y': pd[6], 'Z': pd[7]}
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
            for pointer in range(0, n):
                de.append(pd[3+pointer])

            prefix(l + 1)
            print("+--", form_associativity_str[e['Form Number']], sep="")

            prefix(l + 1)
            print("   ", "Number of entries: ", n, sep="")
            body = []
            for i in range(0, n):
                for eee in de_:
                    if eee["Sequence Number"] == de[i]:
                        type, obj = process_entity(l + 2, de_, pd_, eee)
                        if type == 'Facet':
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

        for i in range(0, int(n2)):
            for eee in de_:
                if eee["Sequence Number"] == pd[6+i]:
                    process_entity(l + 2, de_, pd_, eee)
                    break
        return 'Facet', obj

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


start_sec = ""
global_sec = ""
direcory_entry_sec = []
parameters_data_sec = []
terminate_sec = ""
field = ""
pfield = ""
pstr = ""
ppstr = ""
iDE = 0
iPD = 0
for line in f:
    if line[72] == 'S':
        start_sec += line[:72]

    if line[72] == 'G':
        global_sec += line[:72]

    if line[72] == 'D':
        if iDE == 0:
            field = line.replace("\n", "")
        else:
            direcory_entry_sec.append(field + line.replace("\n", ""))
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
            parameters_data_sec.append(pstr + ppstr + pfield + line[:64].lstrip().rstrip())
            pfield = ""
            iPD = 0

    if line[72] == "T":
        terminate_sec = line
        break

# print(start_sec)

g_sec = []
for p in global_section_parser(global_sec):
    g_sec.append(p)

# print(G_sec)

de_sec = []
n = 0
for field in direcory_entry_sec:
    de_subsec = {}
    g = de_section_parser(field)
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
n = 0
for field in parameters_data_sec:
    pd_subsec = []
    for i in pd_section_parser(field):
        try:
            int(i)
            pd_subsec.append(str(int(i)))
        except:
            pd_subsec.append(i)
    pd_subsec.append(str(n))
    n += 1
    pd_sec[pd_subsec[0]] = pd_subsec[1:]

# print(pd_sec)

level = 1
n = 0
solid = []
for ee in de_sec:
    if subordinate_entity_switch_str[ee['Status Number'][2:4]] == "Independent":
        print("#", n, sep="")
        n += 1
        type, obj = process_entity(level, de_sec, pd_sec, ee)
        if type == 'None':
            continue
        if type == 'Solid':
            solid = obj
        if type == 'Facet':
            solid.append(obj)

for facet in solid:
    for edge in facet:
        p1, p2 = edge
        print(p1, p2)
    print()
