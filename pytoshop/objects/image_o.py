import numpy as np

import cv2

from pytoshop.objects.layer_o import Layer
from pytoshop.utils.color_u import rgb_to_rgba


class Image:

    def __init__(self, width, height, image_name=None):
        self.channel_count = 4
        self.width = width
        self.height = height
        self.bytesPerLine = width * self.channel_count

        self.scale, self.min_scale, self.max_scale = 1, 0.5, 2.5

        self.current_layer = Layer(self, pos=0)
        self.current_layer.fill([255, 255, 255])
        # TODO remove this line, it's for test
        self.current_layer.load_image('pytoshop/objects/test.png')

        self.top_layer = Layer(self, self.current_layer, None)
        self.current_layer.top_layer = self.top_layer

        self.bottom_layer = Layer(self, None, self.current_layer)
        self.bottom_layer.fill_checker((255, 255, 255), (205, 205, 205), 5)
        self.current_layer.bottom_layer = self.bottom_layer
        self.current_layer.top_layer = self.top_layer

    def addLayer(self):
        # Create new layer
        new_pos = self.current_layer.pos + 1
        new_layer = Layer(self, self.current_layer, self.current_layer.top_layer, new_pos)

        # Update top layers pos
        top_layer = self.current_layer.top_layer
        while top_layer is not None and top_layer.pos != -1:
            top_layer.pos += 1
            top_layer = top_layer.top_layer

        # Insert new layer
        self.current_layer.top_layer.bottom_layer = new_layer
        self.current_layer.top_layer = new_layer
        self.current_layer = new_layer

        return new_layer

    def map(self, x0, y0, width, height):
        x = int(x0 * self.width / width)
        y = int(y0 * self.height / height)
        return x, y

    def load(self, main_v, location):
        image = cv2.cvtColor(cv2.imread(location, -1), cv2.COLOR_BGR2RGBA)
        self.addLayer()
        main_v.layers.addLayer(self.current_layer)
        self.current_layer.draw(image, self.width//2, self.height//2)

    def save(self, location):
        cv2.imwrite(location + ".png", cv2.cvtColor(self.top_layer.bottom_layer.rgba_display, cv2.COLOR_RGBA2BGRA))
