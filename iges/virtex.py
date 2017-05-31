class Virtex:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def update(self, nx, ny, nz):
        self.x = nx
        self.y = ny
        self.z = nz

    def xyz(self):
        return self.x, self.y, self.z

    def x(self):
        return self.x

    def y(self):
        return self.y

    def z(self):
        return self.z
