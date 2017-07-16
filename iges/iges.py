from solid import Solid
from plane import Plane
from face import Face
from edge import Edge
from line import Line
import math
import copy

from entities import THICKNESS
from point import Point
from vector import Vector

#filename = 'top-champfer.iges'
#filename = 'cube.IGS'
#filename = 'cube_fc.iges'
filename = 'g-part.IGS'
#filename = 'pyram.IGS'

solid = Solid(filename, 0)
solid_ = Solid(filename, 0)

#print("Object:")
#solid_.print()
#print('-----')

#solid.print()
solid.refactor()

exit()
cf = solid.concave_faces()
to_merge = []
for f1, f2 in cf:
    l = f1.intersect_line(f2)
    e1 = Face(f1.edges_along_line(l))
    e2 = Face(f2.edges_along_line(l))

    e1.sort(l.gradient()[0])
    e2.sort(l.gradient()[0])

    v, n = f2.abcd()
    t = THICKNESS / v.lenght()
    for e in e1.edges():
        pieces = e.intersect_pieces(e2)
        faces_to_merge = []
        for piece in pieces:
            v0 = piece.point(0)
            v1 = piece.point(1)
            v2 = piece.point(1) + v.scale(t)
            v3 = piece.point(0) + v.scale(t)
            face = Face([Edge(v0, v1), Edge(v1, v2), Edge(v2, v3), Edge(v3, v0)])
            vv, d = face.abcd()
            vvv, d = f1.abcd()
            if Edge(vvv, vv).is_inner_point(Vertex(0, 0, 0)):
                face.mirror()
            faces_to_merge.append(face)
        to_merge.append((f1, faces_to_merge))

    v, n = f1.abcd()
    t = THICKNESS / v.lenght()
    for e in e2.edges():
        pieces = e.intersect_pieces(e1)
        faces_to_merge = []
        for piece in pieces:
            v0 = piece.point(0)
            v1 = piece.point(1)
            v2 = piece.point(1) + v.scale(t)
            v3 = piece.point(0) + v.scale(t)
            face = Face([Edge(v0, v1), Edge(v1, v2), Edge(v2, v3), Edge(v3, v0)])
            vv, d = face.abcd()
            vvv, d = f2.abcd()
            if Edge(vvv, vv).is_inner_point(Vertex(0, 0, 0)):
                face.mirror()
            faces_to_merge.append(face)
        to_merge.append((f2, faces_to_merge))

to_replace = []
for f, face_to_merge in to_merge:
    f.print()
    print()
    extended_face = copy.deepcopy(f)
    for face in face_to_merge:
        face.print()
        print()
        extended_face.merge(face)
        #extended_face.print()
        #print()
    #print('---')
    to_replace.append((f, extended_face))

'''
for f, ff in to_replace:
    f.print()
    print()
    ff.print()
    print()
'''
