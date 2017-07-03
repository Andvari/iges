from entities import equ
import math


class Vertex:
    def __init__(self, *args):

        if len(args) == 0:
            self.__coordinates = {}
            return

        self.__coordinates = {'X': args[0], 'Y': args[1], 'Z': args[2]}

    def update(self, *args):

        if len(args) == 1:
            self.__coordinates['X'] = args[0].value('X')
            self.__coordinates['Y'] = args[0].value('Y')
            self.__coordinates['Z'] = args[0].value('Z')
            return

        self.__coordinates[args[0]] += args[1]

    def value(self, *args):
        if len(args) == 0:
            return self.__coordinates['X'], self.__coordinates['Y'], self.__coordinates['Z']

        if len(args) == 1:
            return self.__coordinates[args[0]]

        v = []
        for a in args:
            v.append(self.__coordinates[a])

        return v

    def __eq__(self, p):
        x0, y0, z0 = self.value()
        x1, y1, z1 = p.value()
        return equ(x0, x1) and equ(y0, y1) and equ(z0, z1)

    def print(self, *args):
        e = ""
        if len(args):
            e = args[0]
        print(self.__coordinates['X'], self.__coordinates['Y'], self.__coordinates['Z'], ', ', end=e)

    def distance(self, p):
        x0, y0, z0 = self.value()
        x1, y1, z1 = p.value()

        return math.sqrt((x1-x0)*(x1-x0)+(y1-y0)*(y1-y0)+(z1-z0)*(z1-z0))

    def vect_mult(self, p):
        x0, y0, z0 = self.value()
        x1, y1, z1 = p.value()

        x = y0 * z1 - y1 * z0
        y = -x0 * z1 + x1 * z0
        z = x0 * y1 - x1 * y0

        return Vertex(x, y, z)

    def scalar_mult(self, p):
        x0, y0, z0 = self.value()
        x1, y1, z1 = p.value()

        return x0 * x1 + y0 * y1 + z0 * z1

    def vector(self, p):
        x0, y0, z0 = self.value()
        x1, y1, z1 = p.value()

        return Vertex(x1-x0, y1-y0, z1-z0)

    def middle(self, p):
        x0, y0, z0 = self.value()
        x1, y1, z1 = p.value()

        return Vertex((x0+x1)/2, (y0+y1)/2, (z0+z1)/2)

    def __add__(self, p):
        x0, y0, z0 = self.value()
        x1, y1, z1 = p.value()
        return Vertex(x0+x1, y0+y1, z0+z1)

    def __neg__(self):
        x, y, z = self.value()
        return Vertex(-x, -y, -z)

    def norm(self):
        power = self.value('X')*self.value('X')+self.value('Y')*self.value('Y')+self.value('Z')*self.value('Z')
        norm = math.sqrt(power)

        if norm:
            self.__coordinates['X'] /= norm
            self.__coordinates['Y'] /= norm
            self.__coordinates['Z'] /= norm
