from pytoshop.objects.layer_o import Layer

import cv2


class Image:

    def __init__(self, width, height, image_name=None):
        self.layers = []
        self.channel_count = 4
        self.width = width
        self.height = height
        self.bytesPerLine = width * self.channel_count

        self.current_layer = first_layer = Layer(self)
        self.layers.append(first_layer)
        if image_name is not None:
            first_layer.load(cv2.imread(image_name))

        self.top_layer = self.newLayer()

    def newLayer(self):
        bottom_layer = self.layers[-1]
        new_layer = Layer(self, bottom_layer)
        bottom_layer.top_layer = new_layer
        self.layers.append(new_layer)
        return new_layer

    def drawBrush(self, brush, x0, y0):
        brush.draw(self.top_layer, x0, y0)

    def draw(self, brush, x0, y0):
        brush.draw(self.current_layer, x0, y0)

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

        D = 2 * dy - dx
        y = 0

        for x in range(dx + 1):
            brush.draw(self.current_layer, x0 + x * xx + y * yx, y0 + x * xy + y * yy)
            if D >= 0:
                y += 1
                D -= 2 * dx
            D += 2 * dy
