from pytoshop.objects.brush_o import Brush

from math import sqrt


class SquareBrush(Brush):

    def __init__(self):
        super().__init__()

    def draw(self, layer, x0, y0):
        color = self.color
        radius = self.size // 2
        hardness = self.hardness / 100
        opacity = self.opacity / 100

        visited = []

        for pos in range(0, radius + 1):
            dx = pos
            dy = pos
            d = pos / radius
            a = 1 if d < hardness or hardness == 1 else (1 - d) / (1 - hardness)
            a *= opacity

            for p in [-pos, pos]:
                # Right and left sides
                layer.draw(x0+p, y0, color, a)
                for dy in range(1, pos+1):
                    layer.draw(x0+p, y0+dy, color, a)
                    layer.draw(x0+p, y0-dy, color, a)

                # Top and bottom sides
                layer.draw(x0, y0+p, color, a)
                for dx in range(1, pos):
                    layer.draw(x0+dx, y0+p, color, a)
                    layer.draw(x0-dx, y0+p, color, a)