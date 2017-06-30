from solid import Solid
from vertex import Vertex
from plane import Plane
from face import Face
from edge import Edge
import math


n1 = Vertex(0, 0, 0)
v1 = Vertex(1, 1, 1)

n2 = Vertex(0, 0, 0)
v2 = Vertex(0, 0, 1)



while True:
    pass

filename = 'top-champfer.iges'
#filename = 'cube.IGS'

solid = Solid(filename, 0)
solid_ = Solid(filename, 0)

print("Object:")
solid_.print()
print('-----')

solid.run()
