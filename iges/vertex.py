'''
from entities import equ
import math
from point import Point


class Vertex(Point):
    def __init__(self, *args):
        Point.__init__(self, *args)

    def __eq__(self, p):
        x0, y0, z0 = self
        x1, y1, z1 = p
        return equ(x0, x1) and equ(y0, y1) and equ(z0, z1)
'''