from pytoshop.objects.brush_o import Brush

from math import floor
import cv2
import numpy as np


class CircleBrush(Brush):

    def __init__(self):
        super().__init__()

    def draw(self, layer, point):
        x0, y0 = point
        radius = self.size // 2 - 1
        size = self.size * 2 - 1
        center = (size-1) // 2

        mat = np.full((size, size, 4), 0, np.uint8)
        cv2.circle(mat, (center, center), radius, (0, 0, 0, 255), -1)

        gaussRadius = self.size - int((self.size - 3) * self.hardness / 100)
        gaussRadius += 1 - gaussRadius % 2
        mat = cv2.GaussianBlur(mat, (gaussRadius, gaussRadius), 0)

        r = size // 2
        padTop = 0 if y0-r < 0 else y0-r
        padBottom = layer.image.height if y0+r+1 > layer.image.height else y0+r+1
        layer.display_values[padTop:padBottom, x0-r:x0+r+1] = mat[padTop-(y0-r):padBottom+(y0+r+1), 0:len(mat)]

        # for j in range(len(mat)):
        #     for i in range(len(mat[0])):
        #         print(str(mat[j][i][3]).rjust(3), end=" ")
        #     print()

        #for j in range(size):
        #    for i in range(size):
        #        x, y = x0+i-center, y0+j-center
        #        if layer.canDrawAt(x, y):
        #            layer.drawDisplay(x, y, mat[j][i])

#        color = self.color
#        radius = self.size // 2
#        hardness = self.hardness / 100
#        opacity = self.opacity / 100
#
#        # Drawing middle lines
#        for i, j in [0, 1], [1, 0]:
#            for delta in range(-radius, radius + 1):
#                x, y = x0 + delta*i, y0 + delta*j
#
#                d = ((x0 - x) ** 2 + (y0 - y) ** 2) / (radius * radius)
#                if d <= 1:
#                    a = 1 if d < hardness or hardness == 1 else (1 - d) / (1 - hardness)  # exp(-7*d)
#                    a *= opacity
#                    if layer.canDrawAt(x, y):
#                        layer.draw(x, y, color, a)
#
#        # Drawing outer circle
#        for dy in range(1, radius + 1):
#            for dx in range(1, radius + 1):
#                xA, yA = x0 + dx, y0 + dy
#                xB, yB = x0 - dx, y0 + dy
#                xC, yC = x0 + dx, y0 - dy
#                xD, yD = x0 - dx, y0 - dy
#
#                d = ((x0 - xA) ** 2 + (y0 - yA) ** 2) / (radius*radius)
#                if d <= 1:
#                    a = 1 if d < hardness or hardness == 1 else (1 - d) / (1 - hardness)  # exp(-7*d)
#                    a *= opacity
#                    if layer.canDrawAt(xA, yA):
#                        layer.draw(xA, yA, color, a)
#                    if layer.canDrawAt(xB, yB):
#                        layer.draw(xB, yB, color, a)
#                    if layer.canDrawAt(xC, yC):
#                        layer.draw(xC, yC, color, a)
#                    if layer.canDrawAt(xD, yD):
#                        layer.draw(xD, yD, color, a)
#