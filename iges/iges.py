from solid import Solid
from virtex import Virtex


#file = open("cube_fc.iges", "r")
#file = open("cube.IGS", "r")

a = {}
a['X'] = 0
a['Y'] = 1
a['Z'] = 2
b = {}
b['X'] = 0

print(a==b)

while True:
    pass

solid = Solid("g-part.IGS", 0)
solid_ = Solid("g-part.IGS", 0)

'''
for face in solid:
    face.image(face.plane()).print()
    print()
'''
solid = Solid("g-part.IGS", 0)

'''
ff = face_to_face_matrix(solid, 0)
fe = face_to_edge_matrix(ff, 0)
'''
for face in solid:
    for e1, e2 in face.anomalies():
        print(e1, e2)
        d = e1.dir()
        f = solid.ff(face, e1)
        solid_.expand(f, e1, d, 1)

        d = e2.dir()
        f = solid.ff(face, e2)
        solid_.expand(f, e2, d, 1)




