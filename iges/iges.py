from solid import Solid
from virtex import Virtex


filename = 'pyram.IGS'

solid = Solid(filename, 0)
solid_ = Solid(filename, 0)

print("Object:")
for face in solid_:
    face.image(face.plane()).print()
    print()
print('---------------')

solid = Solid(filename, 0)

for face in solid:
    for e1, e2 in face.anomalies():
        d = e1.way()
        f = solid.ff(face, e1)
        solid_.expand(f, e1, d, 1)

        d = e2.way()
        f = solid.ff(face, e2)
        solid_.expand(f, e2, d, 1)

top_faces = solid_.faces_by_plane(['XY'])
side_faces = solid_.faces_by_plane(['YZ', 'XZ'])

print(top_faces)
print(side_faces)