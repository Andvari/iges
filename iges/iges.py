from solid import Solid
from virtex import Virtex


#file = open("cube_fc.iges", "r")
#file = open("cube.IGS", "r")


solid = Solid("g-part-fc.IGS", 0)
solid_ = Solid("g-part-fc.IGS", 0)


for face in solid_:
    face.image(face.plane()).print()
    print()


solid = Solid("g-part-fc.IGS", 0)

i=0
for face in solid:
    i+=1
    for e1, e2 in face.anomalies():
        d = e1.way()
        f = solid.ff(face, e1)
        solid_.expand(f, e1, d, 1)

        d = e2.way()
        f = solid.ff(face, e2)
        f.image(f.plane()).print()
        solid_.expand(f, e2, d, 1)

for face in solid_:
    face.image(face.plane()).print()
    print()


