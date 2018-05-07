from pytoshop.objects.brush_o import Brush

from math import floor
import cv2
import numpy as np
import timeit


class CircleBrush(Brush):

    def __init__(self):
        super().__init__()

    def generate(self):
        radius = self.size // 2 - 1
        size = self.size * 2 - 1
        print('SIZE: ', size)
        center = (size-1) // 2

        # Create empty matrix with sharp circle in it
        mat = np.full((size, size, 4), 0, np.uint8)
        cv2.circle(mat, (center, center), radius, (0, 0, 0, 255), -1)

        # Apply gaussian blur filter to the matrix
        gaussRadius = self.size - int((self.size - 3) * self.hardness / 100)
        gaussRadius += 1 - gaussRadius % 2
        mat = cv2.GaussianBlur(mat, (gaussRadius, gaussRadius), 0)

        return mat
