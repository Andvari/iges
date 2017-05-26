from entities import *

f = open("cube_fc.iges", "r")
# f = open("cube.IGS", "r")


def prefix(l):
    if l > 1:
        print("|  ", end="", sep="")
    if l > 2:
        print("   " * (l - 2), end="", sep="")


def process_entity(l, de, pd, e):
    prefix(l)
    print("+--", "Entity: ", entity[pd[e["Parameter Data"]][1]], sep="")
    # print("DE: ", e)
    # print("PD: ", pd[e[1]])

    if entity[pd[e["Parameter Data"]][1]] == "Color Definition":
        prefix(l + 1)
        print("+--", "Red: ", pd[e["Parameter Data"]][2], "%", sep="")
        prefix(l + 1)
        print("   ", "Green: ", pd[e["Parameter Data"]][3], "%", sep="")
        prefix(l + 1)
        print("   ", "Blue: ", pd[e["Parameter Data"]][4], "%", sep="")

    if entity[pd[e["Parameter Data"]][1]] == "Curve on a Parametric Surface":
        prefix(l + 1)
        print("+--", "Way the curve has been created: ", crtn[pd[e["Parameter Data"]][2]], sep="")
        for eee in de:
            if eee["Sequence Number"] == pd[e["Parameter Data"]][3]:
                process_entity(l + 2, de, pd, eee)
                break
        if pd[e["Parameter Data"]][4] == "0":
            prefix(l + 1)
            print("   ", "Pointer to the curve B definition: Unspecified", sep="")
        for eee in de:
            if eee["Sequence Number"] == pd[e["Parameter Data"]][4]:
                process_entity(l + 2, de, pd, eee)
                break
        for eee in de:
            if eee["Sequence Number"] == pd[e["Parameter Data"]][5]:
                process_entity(l + 2, de, pd, eee)
                break
        prefix(l + 1)
        print("   ", "Preferred representation: ", pref[pd[e["Parameter Data"]][6]], sep="")

    if entity[pd[e["Parameter Data"]][1]] == "Rational B-Spline Surface":
        prefix(l + 1)
        print("+--", "Upper indexes: ", pd[e["Parameter Data"]][2], ", ", pd[e["Parameter Data"]][3], sep="")
        prefix(l + 1)
        print("   ", "Degree of basis function: ", pd[e["Parameter Data"]][4], ", ", pd[e["Parameter Data"]][5], sep="")
        prefix(l + 1)
        print("   ", prop1_[pd[e["Parameter Data"]][6]], sep="")
        prefix(l + 1)
        print("   ", prop2_[pd[e["Parameter Data"]][7]], sep="")
        prefix(l + 1)
        print("   ", prop3_[pd[e["Parameter Data"]][8]], sep="")
        prefix(l + 1)
        print("   ", prop4_[pd[e["Parameter Data"]][9]], sep="")
        prefix(l + 1)
        print("   ", prop5_[pd[e["Parameter Data"]][10]], sep="")
        k1 = int(pd[e["Parameter Data"]][2])
        k2 = int(pd[e["Parameter Data"]][3])
        m1 = int(pd[e["Parameter Data"]][4])
        m2 = int(pd[e["Parameter Data"]][5])

        n1 = 1 + k1 - m1
        n2 = 1 + k2 - m2
        a = n1 + 2 * m1
        b = n2 + 2 * m2
        c = (1 + k1) * (1 + k2)
        prefix(l + 1)
        print("   ", "First knot sequence: ", end="", sep="")
        for i in range(0, a + 1):
            print(pd[e["Parameter Data"]][11 + i], ", ", end="", sep="")
        print()
        prefix(l + 1)
        print("   ", "Second knot sequence: ", end="", sep="")
        for i in range(0, b + 1):
            print(pd[e["Parameter Data"]][11 + (a + 1) + i], ", ", end="", sep="")
        print()
        prefix(l + 1)
        print("   ", "Weights: ", end="", sep="")
        for i in range(0, (k1 + 1) * (k2 + 1)):
            print(pd[e["Parameter Data"]][11 + (a + 1) + (b + 1) + i], ", ", end="", sep="")
        print()
        prefix(l + 1)
        print("   ", "Control points: ", end="", sep="")
        for i in range(0, (k1 + 1) * (k2 + 1)):
            print("[", pd[e["Parameter Data"]][11 + (a + 1) + (b + 1) + (k1 + 1) * (k2 + 1) + i * 3 + 0], ", ", end="", sep="")
            print(pd[e["Parameter Data"]][11 + (a + 1) + (b + 1) + (k1 + 1) * (k2 + 1) + i * 3 + 1], ", ", end="", sep="")
            print(pd[e["Parameter Data"]][11 + (a + 1) + (b + 1) + (k1 + 1) * (k2 + 1) + i * 3 + 2], "], ", end="", sep="")
        print()
        prefix(l + 1)
        print("   ", "Starting/ending parameter values: ", end="", sep="")
        for i in range(0, 4):
            print(pd[e["Parameter Data"]][11 + (a + 1) + (b + 1) + (k1 + 1) * (k2 + 1) + (k1 + 1) * (k2 + 1) * 3 + i], ", ", end="",
                  sep="")
        print()

    if entity[pd[e["Parameter Data"]][1]] == "Rational B-Spline Curve":
        prefix(l + 1)
        print("+--", "Form: ", form[e["Form Number"]], sep="")
        prefix(l + 1)
        print("   ", "Upper index: ", pd[e["Parameter Data"]][2], sep="")
        prefix(l + 1)
        print("   ", "Degree of basis functions: ", pd[e["Parameter Data"]][3], sep="")
        prefix(l + 1)
        print("   ",
              prop1[pd[e["Parameter Data"]][4]],
              prop2[pd[e["Parameter Data"]][5]],
              prop3[pd[e["Parameter Data"]][6]],
              prop4[pd[e["Parameter Data"]][7]], sep="")
        k = int(pd[e["Parameter Data"]][2])
        m = int(pd[e["Parameter Data"]][2])
        n = 1 + k - m
        a = n + 2 * m
        prefix(l + 1)
        print("   ", "Knot sequence: ", end="", sep="")
        for i in range(0, a + 1):
            print(pd[e["Parameter Data"]][8 + i], ", ", end="", sep="")
        print()
        prefix(l + 1)
        print("   ", "Weights: ", end="", sep="")
        for i in range(0, k + 1):
            print(pd[e["Parameter Data"]][8 + (a + 1) + i], ", ", end="", sep="")
        print()
        prefix(l + 1)
        print("   ", "Control points: ", end="", sep="")
        for i in range(0, k + 1):
            print("[", end="", sep="")
            for j in range(0, 3):
                print(pd[e["Parameter Data"]][8 + (a + 1) + (k + 1) + i * 3 + j], " ", end="", sep="")
            print("], ", end="", sep="")
        print()
        prefix(l + 1)
        print("   ", "Starting/ending parameter values: ", pd[e["Parameter Data"]][8 + (a + 1) + (k + 1) + (k + 1) * 3 + 0], ", ",
              pd[e["Parameter Data"]][8 + (a + 1) + (k + 1) + (k + 1) * 3 + 1], sep="")
        prefix(l + 1)
        print("   ", "Unit normal: ", end="", sep="")
        for i in range(0, 3):
            print(pd[e["Parameter Data"]][8 + (a + 1) + (k + 1) + (k + 1) * 3 + 2 + i], ", ", end="", sep="")
        print()

    if entity[pd[e["Parameter Data"]][1]] == "Composite Curve":
        prefix(l + 1)
        print("   ", "Number of entities: ", pd[e["Parameter Data"]][2], sep="")
        for i in range(0, int(pd[e["Parameter Data"]][2])):
            for eee in de:
                if eee["Sequence Number"] == pd[e["Parameter Data"]][3 + i]:
                    process_entity(l + 2, de, pd, eee)
                    break

    if entity[pd[e["Parameter Data"]][1]] == "Line":
        prefix(l + 1)
        print("   ",
              "[", pd[e["Parameter Data"]][2 + 0],
              ",", pd[e["Parameter Data"]][2 + 1],
              ", ",pd[e["Parameter Data"]][2 + 2], "], ",
              "[", pd[e["Parameter Data"]][2 + 3],
              ", ",pd[e["Parameter Data"]][2 + 4],
              ", ",pd[e["Parameter Data"]][2 + 5], "]", sep="")

    if entity[pd[e["Parameter Data"]][1]] == "Plane":
        prefix(l + 1)
        print("+--", "Form: ", form_plane[e["Form Number"]], sep="")
        prefix(l + 1)
        print("   ", "Plane coefficients A, B, C, D: ", pd[e["Parameter Data"]][2 + 0],
              ", ", pd[e["Parameter Data"]][2 + 1],
              ", ", pd[e["Parameter Data"]][2 + 2],
              ", ", pd[e["Parameter Data"]][2 + 3], sep="")
        prefix(l + 1)
        print("   ", "Zero: ", pd[e["Parameter Data"]][2 + 4], sep="")
        prefix(l + 1)
        print("   ", "Coordinates of location point: ", pd[e["Parameter Data"]][2 + 5],
              ", ", pd[e["Parameter Data"]][2 + 6],
              ", ", pd[e["Parameter Data"]][2 + 7], sep="")
        prefix(l + 1)
        print("   ", "Size: ", pd[e["Parameter Data"]][2 + 8], sep="")

    if entity[pd[e["Parameter Data"]][1]] == "Associativity Instance":
        if e["Form Number"] == "1":
            prefix(l + 1)
            print("+--", "Unordered group with back pointers", sep="")
            prefix(l + 1)
            print("   ", "Number of entries: ", pd[e["Parameter Data"]][2], sep="")
            for i in range(0, int(pd[e["Parameter Data"]][2])):
                for eee in de:
                    if eee["Sequence Number"] == pd[e["Parameter Data"]][2 + 1 + i]:
                        process_entity(l + 2, de, pd, eee)
                        break

    if entity[pd[e["Parameter Data"]][1]] == "Trimmed Parametric Surface":
        for eee in de:
            if eee["Sequence Number"] == pd[e["Parameter Data"]][5]:
                process_entity(l + 2, de, pd, eee)
                break
        prefix(l + 1)
        if pd[e["Parameter Data"]][3] == '0':
            print("   ", "The outer boundary is the boundary of D", sep="")
        else:
            print("   ", "The outer boundary is not the boundary of D", sep="")
        prefix(l + 1)
        print("   ", "Number of closed curves which constitute the inner boundary: ", pd[e["Parameter Data"]][4], sep="")
        for eee in de:
            if eee["Sequence Number"] == pd[e["Parameter Data"]][5]:
                process_entity(l + 2, de, pd, eee)
                break
        for i in range(0, int(pd[e["Parameter Data"]][4])):
            process_entity(l + 2, de, pd, pd[e["Parameter Data"]][6 + i])

    '''
    print("Entity Type Number: ", e[0])
    print("Parameter Data: ", e[1])
    print("Structure: ", e[2])
    print("Line Font Pattern: ", e[3])
    print("Level: ", e[4])
    print("View: ", e[5])
    print("Transformation Matrix: ", e[6])
    print("Label Display Assoc.: ", e[7])
    print("Status Number: ", e[8])
    print("Sequence Number: ", e[9])
    print("Line Weight Number: ", e[11])
    print("Color Number: ", e[12])
    print("Parameter Line Count: ", e[13])
    print("Form Number: ", e[14])
    print("Entity Label: ", e[17])
    print("Entity Subscript Number: ", e[18])
    '''

    '''

    if entity[PD_sec[e[1]][1]] == "Curve on a Parametric Surface":
        print("Way the curve has been created: ", CRTN[PD_sec[e[1]][2]])
        print("Pointer to DE of the surface on which the curve lies: ", PD_sec[e[1]][3])
        print("Pointer to DE of the entity that contains definition of curve B: ", PD_sec[e[1]][4])
        print("Pointer to DE of the curve C: ", PD_sec[e[1]][5])
        print("Preferred representation: ", PREF[PD_sec[e[1]][6]])
    '''
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
    '''
    de_subsec = []
    for i in de_section_parser(field):
        if len(de_subsec) != 8:
            de_subsec.append(str(int(i)))
        else:
            de_subsec.append(i)
    de_subsec.append(str(n))
    n += 1
    '''

    de_subsec = {}
    g = de_section_parser(field)
    de_subsec['Entity Type Number'] = (g.__next__())
    de_subsec['Parameter Data'] = (g.__next__())
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
for ee in de_sec:
    if subordinate_entity_switch[ee['Status Number'][2:4]] == "Independent":
        print("#", n, sep="")
        n += 1
        process_entity(level, de_sec, pd_sec, ee)

'''
i = 0
for e in PD_sec:
    if True:
        print(i, entity[PD_sec[e][1]])
        i+=1
        print(PD_sec[e])

        print("Entity Type Number: ",       DE_sec[PD_sec[e][0]][0])
        print("Parameter Data: ",           DE_sec[PD_sec[e][0]][1])
        print("Structure: ",                DE_sec[PD_sec[e][0]][2])
        print("Line Font Pattern: ",        DE_sec[PD_sec[e][0]][3])
        print("Level: ",                    DE_sec[PD_sec[e][0]][4])
        print("View: ",                     DE_sec[PD_sec[e][0]][5])
        print("Transformation Matrix: ",    DE_sec[PD_sec[e][0]][6])
        print("Label Display Assoc.: ",     DE_sec[PD_sec[e][0]][7])
        print("Status Number: ",            DE_sec[PD_sec[e][0]][8])
        print("Sequence Number: ",          DE_sec[PD_sec[e][0]][9])
        print("Line Weight Number: ",       DE_sec[PD_sec[e][0]][11])
        print("Color Number: ",             DE_sec[PD_sec[e][0]][12])
        print("Parameter Line Count: ",     DE_sec[PD_sec[e][0]][13])
        print("Form Number: ",              DE_sec[PD_sec[e][0]][14])
        print("Entity Label: ",             DE_sec[PD_sec[e][0]][17])
        print("Entity Subscript Number: ",  DE_sec[PD_sec[e][0]][18])

        bs = DE_sec[PD_sec[e][0]][8][0:2]
        ses = DE_sec[PD_sec[e][0]][8][2:4]
        euf = DE_sec[PD_sec[e][0]][8][4:6]
        h = DE_sec[PD_sec[e][0]][8][6:8]

        print(blank_status[bs])
        print(subordinate_entity_switch[ses])
        print(entity_use_flag[euf])
        print(hierarchy[h])
        print("-------------------------")
'''
'''
for e in PD_sec:
    if e[0] == "110":
        print
    print(entity[e[0]])
'''
