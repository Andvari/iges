from entities import *
from lib import *
from virtex import Virtex
from edge import Edge
from face import Face


#file = open("cube_fc.iges", "r")
#file = open("cube.IGS", "r")
file = open("g-part.IGS", "r")

start_sec, global_sec, direcory_entry_sec, parameters_data_sec, terminate_sec = sections_detect(file)

# print(start_sec)

g_sec = []
for p in global_section_parser(global_sec):
    g_sec.append(p)

# print(G_sec)

de_sec = []
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
n = counter(0)
for field in parameters_data_sec:
    pd_subsec = []
    for i in pd_section_parser(field):
        try:
            int(i)
            pd_subsec.append(str(int(i)))
        except:
            pd_subsec.append(i)
    pd_subsec.append(str(n.__next__()))
    pd_sec[pd_subsec[0]] = pd_subsec[1:]

# print(pd_sec)

solid = solid_detect(de_sec, pd_sec)
solid_ = solid_detect(de_sec, pd_sec)

ff = face_to_face_matrix(solid, 0)
fe = face_to_edge_matrix(ff, 0)

for face in solid:
    for anomalie in face.anomalies():
        for e in anomalie:
            d = e.dir()
            f = solid.ff(face, e)
            e1 = solid.fe(face, f)
            d1 = e1.dir()

            if d == d1:
                solid_.expand(f, e, d)
            else:
                solid_.expand(f, e, d1)



