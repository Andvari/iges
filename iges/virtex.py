class Virtex:
    def __init__(self, nx, ny, nz):
        self.x = nx
        self.y = ny
        self.z = nz

    def update(self, nx, ny, nz):
        self.x = nx
        self.y = ny
        self.z = nz

    def data(self):
        return self.x, self.y, self.z

