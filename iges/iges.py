from solid import Solid


#file = open("cube_fc.iges", "r")
#file = open("cube.IGS", "r")
file = open("g-part.IGS", "r")

solid = Solid(file, 1)

for face in solid:
    print(face)
#solid_ = Solid(file, 0)

'''
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
'''


