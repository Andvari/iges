from virtex import Virtex

class Direction:
    def __init__(self, p1: Virtex, p2: Virtex):
        self.ways = []
        if p1.x() < p2.x():
            self.ways.append(('X', '+'))
        if p1.y() < p2.y():
            self.ways.append(('Y', '+'))
        if p1.z() < p2.z():
            self.ways.append(('Z', '+'))
        if p1.x() > p2.x():
            self.ways.append(('X', '-'))
        if p1.y() > p2.y():
            self.ways.append(('Y', '-'))
        if p1.z() > p2.z():
            self.ways.append(('Z', '-'))

