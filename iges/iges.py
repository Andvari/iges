from solid import Solid


#file = open("cube_fc.iges", "r")
#file = open("cube.IGS", "r")

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
    for anomalie in face.anomalies():
        for e in anomalie:
            d = e.dir()
            #print(e.p(0).xyz(), e.p(1).xyz())
            f = solid.ff(face, e)
            if f[0].equ(face):
                f[1].image(f[1].plane()).print()
            if f[1].equ(face):
                f[0].image(f[0].plane()).print()

            '''
            e1 = solid.fe(face, f)
            d1 = e1.dir()

            if d == d1:
                solid_.expand(f, e, d)
            else:
                solid_.expand(f, e, d1)
            '''


