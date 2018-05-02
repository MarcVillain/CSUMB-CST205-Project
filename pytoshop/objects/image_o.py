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

        self.top_layer = self.newLayer()

    def load(self, image_name):
        image = cv2.imread(image_name, -1)
        # TODO: 1) Create new layer with image (careful with the size that can be bigger or smaller than the layer)
        #       2) OR apply the image to the current layer (careful again about size)
        pass

    def save(self, location):
        cv2.imwrite(location, self.top_layer.bottom_layer.rgba_display)

    def newLayer(self):
        bottom_layer = self.layers[-1]
        new_layer = Layer(self, bottom_layer)
        bottom_layer.top_layer = new_layer
        self.layers.append(new_layer)
        return new_layer

    def map(self, x0, y0, width, height):
        x = int(x0 * self.width / width)
        y = int(y0 * self.height / height)
        return x, y
