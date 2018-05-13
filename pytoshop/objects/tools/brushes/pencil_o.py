import cv2
import numpy as np

from pytoshop.objects.tools.brush_o import Brush
from pytoshop.views.main.top_bars.top_bar_pencil import TopBarPencil


class Pencil(Brush):

    def __init__(self):
        super().__init__()

        self.top_bar = TopBarPencil(self)

    def onMousePressed(self, controller, x0, y0):
        controller.image.current_layer.draw(self.generate(), x0, y0)
        controller.view.refresh()

    def onMouseMove(self, controller, x0, y0, x1, y1):
        if controller.mouse_pressed:
            controller.image.current_layer.drawLine(self.generate(), x0, y0, x1, y1)

        controller.image.top_layer.clear()
        controller.image.top_layer.draw(self.generate(), x1, y1)

        controller.view.refresh()

    def generate(self):
        radius = self.size // 2 - 1
        size = self.size * 2 - 1
        center = (size - 1) // 2

        # Create empty matrix with sharp circle in it
        mat = np.full((size, size, 4), 0, np.uint8)
        r, g, b, a = self.color
        cv2.circle(mat, (center, center), radius, (r, g, b, 255 * self.opacity / 100), -1)

        return mat
