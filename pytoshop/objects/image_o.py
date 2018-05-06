from pytoshop.objects.brush_o import Brush
from pytoshop.objects.layer_o import Layer

import cv2


class Image:

    def __init__(self, width, height, image_name=None):
        self.layers = []
        self.channel_count = 4
        self.width = width
        self.height = height
        self.bytesPerLine = width * self.channel_count

        self.scale, self.min_scale, self.max_scale = 1, 0.5, 2

        self.current_layer = Layer(self)
        self.current_layer.fill([255, 255, 255])
        self.layers.append(self.current_layer)

        self.top_layer = self.newLayer(False)

    def newLayer(self, visible=True):
        bottom_layer = self.layers[-1]
        new_layer = Layer(self, bottom_layer)
        bottom_layer.top_layer = new_layer
        if visible:
            self.layers.append(new_layer)
        return new_layer

    def map(self, x0, y0, width, height):
        x = int(x0 * self.width / width)
        y = int(y0 * self.height / height)
        return x, y
