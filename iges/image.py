
class Image:
    def __init__(self, l):
        self.points = l

    def print(self):
        xmin =  1e6
        ymin =  1e6
        xmax = -1e6
        ymax = -1e6
        for x, y in self.points:
            xmin = min(xmin, x)
            ymin = min(ymin, y)
            xmax = max(xmax, x)
            ymax = max(ymax, y)
        '''
        xmin = 0
        ymin = 0
        xmax = 10
        ymax = 20

        self.points = []
        self.points.append((xmin, ymin))
        self.points.append((xmin, ymax))
        self.points.append((xmax, ymin))
        self.points.append((xmax, ymax))
        '''

        print(xmax-xmin, "x", ymax-ymin)

        img = [[' ' for x in range(int(xmax-xmin)+1)] for y in range(int(ymax-ymin)+1)]

        for x, y in self.points:
            img[int(y-ymin)][int(x-xmin)] = '*'

        for l in img:
            for c in l:
                print(c, sep ="", end = "")
            print()



