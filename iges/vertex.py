from entities import equal
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
            return self.__coordinates

        if len(args) == 1:
            return self.__coordinates[args[0]]

        v = []
        for a in args:
            v.append(self.__coordinates[a])

        return v

    def equ(self, v):
        if equal(self.value('X'), v.value('X')):
            if equal(self.value('Y'), v.value('Y')):
                if equal(self.value('Z'), v.value('Z')):
                    return True

        return False

    def print(self):
        print(self.__coordinates['X'], self.__coordinates['Y'], self.__coordinates['Z'], end="")

    def distance(self, v):
        x0 = self.value('X')
        y0 = self.value('Y')
        z0 = self.value('Z')

        x1 = v.value('X')
        y1 = v.value('Y')
        z1 = v.value('Z')

        return math.sqrt((x1-x0)*(x1-x0)+(y1-y0)*(y1-y0)+(z1-z0)*(z1-z0))

    def vect_mult(self, p):
        x0 = self.__coordinates['X']
        y0 = self.__coordinates['Y']
        z0 = self.__coordinates['Z']

        x1 = p.value('X')
        y1 = p.value('Y')
        z1 = p.value('Z')

        x = y0 * z1 - y1 * z0
        y = -x0 * z1 + x1 * z0
        z = x0 * y1 - x1 * y0

        return Vertex(x, y, z)