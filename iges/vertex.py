from entities import equal


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
        print(self.__coordinates['X'], self.__coordinates['Y'], self.__coordinates['Z'])
