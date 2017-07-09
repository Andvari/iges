from solid import Solid
from vertex import Vertex
from plane import Plane
from face import Face
from edge import Edge
import math

#filename = 'top-champfer.iges'
#filename = 'cube.IGS'
#filename = 'cube_fc.iges'
#filename = 'g-part.IGS'
filename = 'pyram.IGS'

solid = Solid(filename, 0)
solid_ = Solid(filename, 0)

#print("Object:")
#solid_.print()
#print('-----')

solid.refactor()
solid.run()
