from pytoshop.objects.brush_o import Brush

from math import floor
import cv2
import numpy as np
import timeit


class CircleBrush(Brush):

    def __init__(self):
        super().__init__()

    def draw(self, layer, point):
        start = timeit.default_timer()
        x0, y0 = point
        radius = self.size // 2 - 1
        size = self.size * 2 - 1
        center = (size-1) // 2

        # Create empty matrix with sharp circle in it
        mat = np.full((size, size, 4), 0, np.uint8)
        cv2.circle(mat, (center, center), radius, (0, 0, 0, 255), -1)

        # Apply gaussian blur filter to the matrix
        gaussRadius = self.size - int((self.size - 3) * self.hardness / 100)
        gaussRadius += 1 - gaussRadius % 2
        mat = cv2.GaussianBlur(mat, (gaussRadius, gaussRadius), 0)

        r, g, b, a = cv2.split(mat)
        rgb = cv2.merge((r, g, b))
        alpha = a[..., None]

        # Draw the brush on the layer
        layer.draw(rgb, alpha, x0, y0)
