from point import Point
#from vertex import Vertex
from radius_vector import RadiusVector


class Line:
    def __init__(self, *args):

        if args:
            if type(args[0]) is Point:
                a = args[0]
            else:
                raise ValueError('Line __init__(): args[0] is not Point')

            if type(args[1]) is Point or type(args[1]) is RadiusVector:
                b = args[1]
            else:
                raise ValueError('Line: args[1] is not Point or RadiusVector')

        self._p = [a, b]
        return

    def point(self):
        return self._p[0]

    def vector(self):
        if type(self._p[1]) is Point:
            return self[1] - self[0]
        return self[1]

    def __getitem__(self, item):
        return self._p[item]

    def __setitem__(self, key, value):
        raise ValueError('Line __setitem__(): operation not permitted')

    def __delitem__(self, key):
        raise ValueError('Line __delitem__(): operation not permitted')

    '''
    def belong(self, p: Vertex):

        x, y, z = p
        x0, y0, z0 = self.point()
        dx, dy, dz = self.vector()

        if dx and dy and dz:
            if (x-x0)/dx == (y-y0)/dy and (y-y0)/dy == (z-z0)/dz:
                return True
            else:
                return False

        if not dx and dy and dz:
            if x == x0 and (y - y0) / dy == (z - z0) / dz:
                return True
            else:
                return False

        if dx and not dy and dz:
            if y == y0 and (x - x0) / dx == (z - z0) / dz:
                return True
            else:
                return False

        if dx and dy and not dz:
            if z == z0 and (x - x0) / dx == (y - y0) / dy:
                return True
            else:
                return False

        if not dx and not dy and dz:
            if x == x0 and y == y0:
                return True
            else:
                return False

        if not dx and dy and not dz:
            if x == x0 and z == z0:
                return True
            else:
                return False

        if dx and not dy and not dz:
            if y == y0 and z == z0:
                return True
            else:
                return False

        if not dx and not dy and not dz:
            if x == x0 and y == y0 and z == z0:
                return True
            else:
                return False
    '''

    def coincide(self, l):

        x0, y0, z0 = self.point()
        dx, dy, dz = self.vector()
        xs, ys, zs = l.point()
        xf, yf, zf = l.vector() + l.point()

        if dx and dy and dz:
            if not (xs - x0)/dx == (ys - y0)/dy or not (ys - y0)/dy == (zs - z0)/dz:
                return False

        if not dx and dy and dz:
            if not xs == x0 or not (ys - y0)/dy == (zs-z0)/dz:
                return False

        if dx and not dy and dz:
            if not ys == y0 or not (xs - x0)/dx == (zs-z0)/dz:
                return False

        if dx and dy and not dz:
            if not zs == z0 or not (xs - x0)/dx == (ys-y0)/dy:
                return False

        if not dx and dy and dz:
            if not xs == x0 or not (ys - y0)/dy == (zs-z0)/dz:
                return False

        if not dx and not dy and dz:
            if not xs == x0 or not ys == y0:
                return False

        if not dx and dy and not dz:
            if not xs == x0 or not zs == z0:
                return False

        if dx and not dy and not dz:
            if not ys == y0 or not zs == z0:
                return False

        if dx and dy and dz:
            if not (xf - x0)/dx == (yf - y0)/dy or not (yf - y0)/dy == (zf - z0)/dz:
                return False

        if not dx and dy and dz:
            if not xf == x0 or not (yf - y0)/dy == (zf-z0)/dz:
                return False

        if dx and not dy and dz:
            if not yf == y0 or not (xf - x0)/dx == (zf-z0)/dz:
                return False

        if dx and dy and not dz:
            if not zf == z0 or not (xf - x0)/dx == (yf-y0)/dy:
                return False

        if not dx and dy and dz:
            if not xf == x0 or not (yf - y0)/dy == (zf-z0)/dz:
                return False

        if not dx and not dy and dz:
            if not xf == x0 or not yf == y0:
                return False

        if not dx and dy and not dz:
            if not xf == x0 or not zf == z0:
                return False

        if dx and not dy and not dz:
            if not yf == y0 or not zf == z0:
                return False

        return True

    def gradient(self):
        g = []
        if self.vector()[0]:
            g.append(0)
        if self.vector()[1]:
            g.append(1)
        if self.vector()[2]:
            g.append(2)

        return g

    def __str__(self):
        if type(self[1]) is Point:
            return str(self[0]) + ', ' + str(self[1] - self[0])
        else:
            return str(self[0]) + ', ' + str(self[1])
