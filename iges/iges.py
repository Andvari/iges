from solid import Solid
from vertex import Vertex
from plane import Plane


filename = 'cube.IGS'

solid = Solid(filename, 0)
solid_ = Solid(filename, 0)

print("Object:")
for face in solid_:
    for e in face:
        e.print()
    print('--')

solid = Solid(filename, 0)

for face in solid:
    for e1, e2 in face.anomalies():
        d = e1.way()
        f = solid.ff(face, e1)
        solid_.expand(f, e1, d, 1)

        d = e2.reverse().way()
        f = solid.ff(face, e2)
        solid_.expand(f, e2, d, 1)

print('--------------+')
#top_faces = solid_.parallel_faces([Plane('XZ')])
#side_faces = solid_.parallel_faces([Plane('YZ'), Plane('XZ')])
#print(top_faces)
#print(side_faces)

solid_.optimize(Plane('XY'))

print("Object:")
for face in solid_:
    face.image(Plane('XY')).print()
    print()
