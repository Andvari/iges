from entities import *
from lib import *

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

ff = facet_to_facet_matrix(solid, 0)
fe = facet_to_edge_matrix(ff, 0)

i = counter(1)
for facet in solid:
    print("Facet: %d"%i.__next__())
    print("Edges:")
    for p1, p2 in facet:
        print('[%.3f, %.3f, %.3f], [%.3f, %.3f, %.3f] '%(p1['X'], p1['Y'], p1['Z'], p2['X'], p2['Y'], p2['Z']))

    m = []
    for edge in facet:
        m.append(direction(edge))

    vote_cw = 0
    vote_ccw = 0
    a_cw = []
    a_ccw = []
    for e in range(len(m)-2):
        route = m[e+0] + m[(e+1)%len(m)] + m[(e+2)%len(m)]
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
        anomalies = a_cw
        print("Clockwise")
    else:
        anomalies = a_ccw
        print("Counterclockwise")

    print("Anomalies: ", anomalies)
    print("----------------------")
