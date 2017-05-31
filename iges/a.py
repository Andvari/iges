class A:
    def __init__(self):
        self.v = 0

    def set(self, v):
        self.v = v

    def get(self):
        return self.v

class B:
    def __init__(self):
        self.v = A()

    def set(self, v):
        self.v.set(v)

    def get(self):
        return self.v

    def getv(self):
        return self.v.get()