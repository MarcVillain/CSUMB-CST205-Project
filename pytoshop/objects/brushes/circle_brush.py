import sys
sys.path.append('../../')

from pytoshop.objects.brush_o import Brush

from math import sqrt

class CircleBrush(Brush):

    def __init__(self):
        super().__init__()

    def draw(self, image, x0, y0):
        c = self.color
        r = self.size // 2
        h = self.hardness / 100
        o = self.opacity / 100

        for dy in range(-r, r+1):
            for dx in range(-r, r+1):
                x, y = x0+dx, y0+dy
                if x >= 0 and x < image.width and y >= 0 and y < image.height:
                    d = sqrt((x0-x)**2 + (y0-y)**2) / r
                    if d <= 1:
                        a = 1 if d < h or h == 1 else (1-d)/(1-h) #exp(-7*d)
                        a *= o
                        for i in range(0, 3):
                            val = image.values[y][x][i]*(1-a) + a*c[i]
                            image.values[y][x][i] = val