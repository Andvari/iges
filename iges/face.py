class Face:
    def __init__(self, e):
        self.e = e

    def update(self, e):
        self.e = e

    def update(self, n, e):
        self.e[n] = e

    def edges(self):
        return self.e

    def edge(self, n):
        try:
            return self.e[n]
        except:
            pass

    def virtexes(self):
        r = []
        for v in self.e:
            p1, p2 = v.get()
            r.append(p1)
        return r

    def append(self, e):
        self.e.append(e)
