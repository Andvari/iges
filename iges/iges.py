from solid import Solid
from vertex import Vertex
from plane import Plane
from face import Face
from edge import Edge
import math
'''
v1 = Vertex(1, 0, 0)
v3 = Vertex(0, 1, 0)
v2 = Vertex(0, 0, 1)
f1 = Face([Edge(v1, v2), Edge(v2, v3), Edge(v3, v1)])
p1 = f1.plane()
a, b, c, d = p1.abcd()
print("f1 a,b,c,d: ", a, b, c, d)

v1 = Vertex(0, 0, 0)
v3 = Vertex(1, 0, 0)
v2 = Vertex(0, 0, 1)
f2 = Face([Edge(v1, v2), Edge(v2, v3), Edge(v3, v1)])
p2 = f2.plane()
a, b, c, d = p2.abcd()
print("f2 a,b,c,d: ", a, b, c, d)

l = p1.intersect(p2)

if l:
    print("n: ", end = "")
    l.point().print()
    print("v: ", end = "")
    l.vector().print()
else:
    print("Planes not intersects")

p = f2.point_out_of_line(l)

if p:
    print("Point out of line: ", p.value())
    g = p1.angle(l, p)

print(g)


while True:
    pass
'''
filename = 'cube.IGS'

solid = Solid(filename, 0)
solid_ = Solid(filename, 0)
'''
print("Object:")
for face in solid_:
    for e in face:
        e.print()
    print('--')
'''
solid = Solid(filename, 0)

k=1
for i in range(solid.size()):
    for j in range(i+1, solid.size()):
        print(k)
        k+=1
        for e in solid.faces(i):
            e.print()
        print('--')
        for e in solid.faces(j):
            e.print()
        a,b,c,d = solid.faces(j).plane().abcd()
        solid.faces(i).hull(solid.faces(j))
        print('----')


print('--------------+')
#top_faces = solid_.parallel_faces([Plane('XZ')])
#side_faces = solid_.parallel_faces([Plane('YZ'), Plane('XZ')])
#print(top_faces)
#print(side_faces)

'''
solid_.optimize(Plane('XY'))

print("Object:")
for face in solid_:
    face.image(Plane('XY')).print()
    print()
'''