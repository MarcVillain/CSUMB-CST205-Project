import numpy as np
import cv2
import math

class Image:

    def __init__(self, width, height, image_name=None):
        channels_count = 3

        if image_name == None:
            self.values = np.full((height, width, channels_count), 255, np.uint8)
        else:
            self.values = imread(image_name)

        self.width = width
        self.height = height
        self.bytesPerLine = width * channels_count

    def draw(self, brush, x0, y0):
        brush.draw(self, x0, y0)

    def drawLine(self, brush, x0, y0, x1, y1):
        """
        Bresenham's algorithm
        """
        dx = x1 - x0
        dy = y1 - y0

        xsign = 1 if dx > 0 else -1
        ysign = 1 if dy > 0 else -1

        dx = abs(dx)
        dy = abs(dy)

        if dx > dy:
            xx, xy, yx, yy = xsign, 0, 0, ysign
        else:
            dx, dy = dy, dx
            xx, xy, yx, yy = 0, ysign, xsign, 0

        D = 2*dy - dx
        y = 0

        for x in range(dx + 1):
            brush.draw(self, x0 + x*xx + y*yx, y0 + x*xy + y*yy)
            if D >= 0:
                y += 1
                D -= 2*dx
            D += 2*dy