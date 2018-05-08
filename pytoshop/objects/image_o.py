from pytoshop.objects.layer_o import Layer


class Image:

    def __init__(self, width, height, image_name=None):
        self.layers = []
        self.channel_count = 4
        self.width = width
        self.height = height
        self.bytesPerLine = width * self.channel_count

        self.scale, self.min_scale, self.max_scale = 1, 0.5, 2

        self.current_layer = Layer(self, pos=0)
        self.current_layer.fill([255, 255, 255])
        self.layers.append(self.current_layer)

        self.top_layer = Layer(self, self.current_layer, None)
        self.bottom_layer = Layer(self, None, self.current_layer)

        self.bottom_layer.fill_checker((255, 255, 255), (205, 205, 205), 5)
        self.current_layer.bottom_layer = self.bottom_layer

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
