from pytoshop.objects.brush_o import Brush

from math import sqrt


class EraserBrush(Brush):

    def __init__(self):
        super().__init__()

    def draw(self, layer, x0, y0):
        radius = self.size // 2
        hardness = self.hardness / 100
        opacity = self.opacity / 100

        for dy in range(-radius, radius + 1):
            for dx in range(-radius, radius + 1):
                x, y = x0 + dx, y0 + dy
                if layer.canDrawAt(x, y):
                    d = sqrt((x0 - x) ** 2 + (y0 - y) ** 2) / radius
                    if d <= 1:
                        a = 1 if d < hardness or hardness == 1 else (1 - d) / (1 - hardness)  # exp(-7*d)
                        a *= opacity
                        layer.erase(x, y, a)
