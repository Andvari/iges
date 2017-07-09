from vertex import Vertex


class Line:
    def __init__(self, *args):

        if len(args) == 0:
            self.__n = Vertex()
            self.__v = Vertex()
            return

        self.__n, self.__v = (args[0], args[1])

    def point(self):
        return self.__n

    def vector(self):
        return self.__v

    def belong(self, p: Vertex):

        x, y, z = p.value()
        x0, y0, z0 = self.point().value()
        dx, dy, dz = self.vector().value()

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

    def coincide(self, l):

        x0, y0, z0 = self.point()
        dx, dy, dz = self.vector()
        xs, ys, zs = l.point()
        xf, yf, zf = l.point() + l.vector()

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

    def print(self):
        print("{ ", end="")
        self.__n.print()
        print(" }, { ", end="")
        self.__v.print()
        print(" }")



