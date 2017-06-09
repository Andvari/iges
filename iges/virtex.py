class Virtex:
    def __init__(self, x: int, y: int, z: int):
        self.coordinates = {'X': x, 'Y': y, 'Z': z}

    def update(self, v):
        self.coordinates['X'] = v.value('X')
        self.coordinates['Y'] = v.value('Y')
        self.coordinates['Z'] = v.value('Z')

    def update(self, c: '', bias: int):
        self.coordinates[c] += bias

    def value(self, l: []):
        v = {}
        for c in l:
            v[c] = self.coordinates[c]
        return v

    def value(self, c: ''):
        return self.coordinates[c]

    def value(self):
        return self.coordinates

    def equ(self, v):
        if self.value() == v.value():
            return True

        return False
