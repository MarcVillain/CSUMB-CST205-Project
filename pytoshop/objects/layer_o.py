import cv2
import numpy as np

from pytoshop.utils.color import color_add_rgb
from pytoshop.utils.color import color_add_rgba


class Layer:

    def __init__(self, image, bottom_layer=None):
        self.image = image
        self.bottom_layer = bottom_layer
        self.top_layer = None

        self.values = np.full((image.height, image.width, image.channel_count), 0, np.uint8)
        self.display_values = np.copy(self.values if bottom_layer is None else bottom_layer.display_values)

    def load(self, image):
        for j, row in enumerate(image):
            for i, col in enumerate(row):
                self.draw(i, j, (col[2], col[1], col[0]))

    def draw(self, x, y, color, alpha=1):
        # Draw on layer
        self.values[y][x] = color_add_rgb(self.values[y][x], color, alpha)

        # Draw on display layer
        self.display_values[y][x] = color_add_rgb(self.display_values[y][x], color, alpha)

        # Draw on top layer
        if self.top_layer is not None:
            self.top_layer.drawDisplay(x, y, self.display_values[y][x])

    def drawDisplay(self, x, y, color):
        if self.values[y][x][3] == 255:
            return

        # Draw on display layer
        new_color = color_add_rgba(color, self.values[y][x])
        self.display_values[y][x] = new_color

        # Draw on top layer
        if self.top_layer is not None:
            self.top_layer.drawDisplay(x, y, self.display_values[y][x])

    def erase(self, x, y, alpha=1):
        value = self.values[y][x]
        if value[3] == 0:
            return
        self.values[y][x][3] *= 1 - alpha

        if self.bottom_layer is not None:
            self.display_values[y][x] = color_add_rgba(self.bottom_layer.display_values[y][x], self.values[y][x])
        else:
            self.display_values[y][x] = self.values[y][x]

        if self.top_layer is not None:
            self.top_layer.drawDisplay(x, y, self.display_values[y][x])

    def canDrawAt(self, x, y):
        return 0 < x < self.image.width and 0 < y < self.image.height
