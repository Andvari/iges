class Virtex:
    def __init__(self, x: float, y: float, z: float):
        self.coordinates = {'X': x, 'Y': y, 'Z': z}

    def update(self, *args):

        if len(args) == 1:
            self.coordinates['X'] = args[0].value('X')
            self.coordinates['Y'] = args[0].value('Y')
            self.coordinates['Z'] = args[0].value('Z')
            return

        self.coordinates[args[0]] += args[1]

    def value(self, *args):
        if len(args) == 0:
            return self.coordinates

        if len(args) == 1:
            return self.coordinates[args[0]]

        v = []
        for a in args:
            v.append(self.coordinates[a])

        return v

    def equ(self, v):
        if self.value() == v.value():
            return True

        return False
