
from entities import *

f = open("cube.IGS", "r")

def process_entity(l, de, pd, e):
    #print("    "*l, l+1)
    print("    "*l, "Entity: ", entity[pd[e[1]][1]])
    print("  "*l, "DE: ", e)
    print("  "*l, "PD: ", pd[e[1]])



    if entity[pd[e[1]][1]] == "Color Definition":
        print("    "*l, "Red: ", pd[e[1]][2], "%")
        print("    "*l, "Green: ", pd[e[1]][3], "%")
        print("    "*l, "Blue: ", pd[e[1]][4], "%")



    if entity[pd[e[1]][1]] == "Curve on a Parametric Surface":
        print("    "*l, "Way the curve has been created: ", CRTN[pd[e[1]][2]])
        print("    "*l, "Pointer to DE of the surface on which the curve lies: ", pd[e[1]][3])
        for ee in de:
            if ee[9] == pd[e[1]][3]:
                process_entity(l+1, de, pd, ee)
                break
        print("    "*l, "Pointer to DE of the entity that contains definition of curve B: ", pd[e[1]][4])
        for ee in de:
            if ee[9] == pd[e[1]][4]:
                process_entity(l+1, de, pd, ee)
                break
        print("    "*l, "Pointer to DE of the curve C: ", pd[e[1]][5])
        for ee in de:
            if ee[9] == pd[e[1]][5]:
                process_entity(l+1, de, pd, ee)
                break
        print("    "*l, "Preferred representation: ", PREF[pd[e[1]][6]])



    if entity[pd[e[1]][1]] == "Rational B-Spline Surface":
        print("    "*l, "Upper index of first sum: ", pd[e[1]][2])
        print("    "*l, "Upper index of second sum: ", pd[e[1]][3])
        print("    "*l, "Degree of first set of basis function: ", pd[e[1]][4])
        print("    "*l, "Degree of second set of basis function: ", pd[e[1]][5])
        print("    "*l, PROP1_[pd[e[1]][6]])
        print("    "*l, PROP2_[pd[e[1]][7]])
        print("    "*l, PROP3_[pd[e[1]][8]])
        print("    "*l, PROP4_[pd[e[1]][9]])
        print("    "*l, PROP5_[pd[e[1]][10]])
        K1 = int(pd[e[1]][2])
        K2 = int(pd[e[1]][3])
        M1 = int(pd[e[1]][4])
        M2 = int(pd[e[1]][5])

        N1 = 1 + K1 - M1
        N2 = 1 + K2 - M2
        A = N1 + 2*M1
        B = N2 + 2*M2
        C = (1+K1)*(1+K2)

    if entity[pd[e[1]][1]] == "Rational B-Spline Curve":
        print("    "*l, "Form: ", FORM[e[14]])
        print("    "*l, "Upper index: ", pd[e[1]][2])
        print("    "*l, "Degree of basis functions: ", pd[e[1]][3])
        print("    "*l, PROP1[pd[e[1]][4]], PROP2[pd[e[1]][5]], PROP3[pd[e[1]][6]], PROP4[pd[e[1]][7]])
        K = int(pd[e[1]][2])
        M = int(pd[e[1]][2])
        N = 1 + K - M
        A = N + 2 * M
        print("    "*l, "Knot sequence: ", end="")
        for i in range(0, A+1):
            print(pd[e[1]][8+i], ", ", end="", sep="")
        print()
        print("    "*l, "Weights: ", end="")
        for i in range(0, K+1):
            print(pd[e[1]][8+(A+1)+i], ", ", end="", sep="")
        print()
        print("    "*l, "Control points: ", end="")
        for i in range(0, K+1):
            print("[", end="", sep="")
            for j in range(0, 3):
                print(pd[e[1]][8+(A+1)+(K+1)+i*3+j], " ", end="", sep="")
            print("], ", end="", sep="")
        print()
        print("    "*l, "Starting/ending parameter values: ", pd[e[1]][8+(A+1)+(K+1)+(K+1)*3+0],pd[e[1]][8+(A+1)+(K+1)+(K+1)*3+1])
        print("    "*l, "Unit normal: ", pd[e[1]][8+(A+1)+(K+1)+(K+1)*3+2],pd[e[1]][8+(A+1)+(K+1)+(K+1)*3+3],pd[e[1]][8+(A+1)+(K+1)+(K+1)*3+4])



    if entity[pd[e[1]][1]] == "Composite Curve":
        print("    "*l, "Number of entities: ", pd[e[1]][2])
        for i in range(0, int(pd[e[1]][2])):
            print("    "*l, "Pointer to the DE of the ", i+1, " entity: ", pd[e[1]][3+i])
            for ee in de:
                if ee[9] == pd[e[1]][3+i]:
                    process_entity(l+1, de, pd, ee)
                    break



    if entity[pd[e[1]][1]] == "Line":
        print("    "*l, "X1: ", pd[e[1]][2+0])
        print("    "*l, "Y1: ", pd[e[1]][2+1])
        print("    "*l, "Z1: ", pd[e[1]][2+2])
        print("    "*l, "X2: ", pd[e[1]][2+3])
        print("    "*l, "Y2: ", pd[e[1]][2+4])
        print("    "*l, "Z2: ", pd[e[1]][2+5])



    if entity[pd[e[1]][1]] == "Trimmed Parametric Surface":
        print("    "*l, "Pointer to thr DE of the surface is to be trimmed: ", pd[e[1]][2])
        for ee in de:
            if ee[9] == pd[e[1]][5]:
                process_entity(l+1, de, pd, ee)
                break
        if pd[e[1]][3] == '0':
            print("    "*l, "The outer boundary is the boundary of D")
        else:
            print("    "*l, "The inner boundary is the boundary of D")
        print("    "*l, "Number of closed curves which constitute the inner boundary: ", pd[e[1]][4])
        print("    "*l, "Pointer to the DE of the curve that constitutes the outer boundary: ", pd[e[1]][5])
        for ee in de:
            if ee[9] == pd[e[1]][5]:
                process_entity(l+1, de, pd, ee)
                break
        for i in range(0, int(pd[e[1]][4])):
            print("    " * l, "Pointer to the DE of the", i, "closed inner boundary curve: ", pd[e[1]][6+i])
            if ee[9] == pd[e[1]][6+i]:
                process_entity(l+1, de, pd, ee)
                break


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
    #print("    "*l, blank_status[e[8][0:2]], subordinate_entity_switch[e[8][2:4]], entity_use_flag[e[8][4:6]], hierarchy[e[8][6:8]])


def status_number_parser(l):
    index = 0
    token = ""

    while index <= 6:
        token = l[index:index+2]
        yield token
        index += 2

def PD_section_parser(l):
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


def DE_section_parser(l):
    index = 0
    token = ""

    while index <= 160-8:
        token = l[index : index + 8]
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

#print(start_sec)

G_sec = []
for p in global_section_parser(global_sec):
    G_sec.append(p)

#print(G_sec)

DE_sec = []
n=0
for field in direcory_entry_sec:
    DE_subsec = []
    for i in DE_section_parser(field):
        DE_subsec.append(i)
    DE_subsec.append(str(n))
    n+=1
    #DE_sec[DE_subsec[9]] = DE_subsec
    DE_sec.append(DE_subsec)

PD_sec = {}
n=0
for field in parameters_data_sec:
    PD_subsec = []
    for i in PD_section_parser(field):
        PD_subsec.append(i)
    PD_subsec.append(str(n))
    n+=1
    PD_sec[PD_subsec[0]] = PD_subsec[1:]

#print(PD_sec)

level=0
n=0
for e in DE_sec:
    if blank_status[e[8][0:2]] == "Visible":
        print("#", n)
        n += 1
        process_entity(level, DE_sec, PD_sec, e)



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
