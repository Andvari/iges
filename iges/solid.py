class Solid:
    def __init__(self, s):
        self.faces = []
        for face in s:
            self.faces.append(face)
        self.i = 0

    def update(self, s):
        self.faces = []
        for face in s:
            self.faces.append(face)
        self.i = 0

    def size(self):
        return len(self.faces)

    def faces(self):
        return self.faces

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.faces):
            self.i += 1
            return self.faces[self.i-1]

        else:
            return StopIteration


