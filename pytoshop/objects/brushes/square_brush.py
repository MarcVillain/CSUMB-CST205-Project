import sys
sys.path.append('../..')

from pytoshop.objects.brush_o import Brush

from math import sqrt

class SquareBrush(Brush):

    def __init__(self):
        super().__init__()

    def draw(self, image, x0, y0):
        c = self.color
        r = self.size // 2
        h = self.hardness / 100
        o = self.opacity / 100

        visited = []

        for pos in range(0, r+1):
            dx = pos
            dy = pos
            d = pos / r
            for x in range(x0-dx, x0+dy+1):
                for y in range(y0-dx, y0+dy+1):
                    if x >= 0 and x < image.width and y >= 0 and y < image.height and (x, y) not in visited:
                        visited.append((x, y))
                        a = 1 if d < h or h == 1 else (1-d)/(1-h) #exp(-7*d)
                        a *= o
                        for i in range(0, 3):
                            val = image.values[y][x][i]*(1-a) + a*c[i]
                            image.values[y][x][i] = val