import cv2
import numpy as np

from pytoshop.utils.color import color_add


class Layer:

    def __init__(self, image, bottom_layer=None):
        self.image = image
        self.top_layer = None

        self.values = np.full((image.height, image.width, image.channel_count), 0, np.uint8)
        self.display_values = np.copy(self.values if bottom_layer is None else bottom_layer.display_values)

    def load(self, image):
        for j, row in enumerate(image):
            for i, col in enumerate(row):
                self.draw(i, j, (col[2], col[1], col[0]))

    """
    def add(self, layer):
        for j in range(self.height):
            for i in range(self.width):
                r0, g0, b0, a0 = self.values[j][i]
                r1, g1, b1, a1 = layer.values[j][i]

                if a1 == 255:
                    self.values[j][i] = [r1, g1, b1, a1]
                    continue

                a0P, a1P = a0 / 255, a1 / 255

                r2 = (r0 * a0P + r1 * a1P) / (a0P + a1P)
                g2 = (g0 * a0P + g1 * a1P) / (a0P + a1P)
                b2 = (b0 * a0P + b1 * a1P) / (a0P + a1P)
                a2 = a0 + a1

                a2 = 255 if a2 > 255 else a2

                self.values[j][i] = [r2, g2, b2, a2]
    """

    def draw(self, x, y, color, alpha=1):
        # Draw on layer
        self.values[y][x] = color_add(self.values[y][x], color, alpha)

        # Draw on display layer
        new_color = color_add(self.display_values[y][x], color, alpha)
        self.display_values[y][x] = new_color

        # Draw on top layer
        if self.top_layer is not None:
            self.top_layer.drawDisplay(x, y, (new_color[0], new_color[1], new_color[2]), new_color[3])

    def drawDisplay(self, x, y, color, alpha):
        if self.values[y][x][3] == 1:
            return

        # Draw on display layer
        new_color = color_add(self.values[y][x], color, alpha)
        self.display_values[y][x] = new_color

        # Draw on top layer
        if self.top_layer is not None:
            self.top_layer.drawDisplay(x, y, (new_color[0], new_color[1], new_color[2]), new_color[3])

#    def erase(self, x, y, alpha):
#        value = self.values[y][x]
#
#        self.values[y][x][3] -= alpha * 255
#        self.values[y][x][3] = 0 if self.values[y][x][3] < 0 else self.values[y][x][3]
#
#        self.draw(x, y, (value[0], value[1], value[2]), value[3])

    def canDrawAt(self, x, y):
        return 0 < x < self.image.width and 0 < y < self.image.height
