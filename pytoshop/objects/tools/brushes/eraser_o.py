import cv2
import numpy as np

from pytoshop.objects.tools.brush import Brush


class Eraser(Brush):

    def __init__(self):
        super().__init__()

    def onMousePressed(self, controller, x0, y0):
        controller.image.current_layer.erase(self.generate(), x0, y0)
        controller.view.refresh()

    def onMouseMove(self, controller, x0, y0, x1, y1):
        if controller.mouse_pressed:
            controller.image.current_layer.eraseLine(self.generate(), x0, y0, x1, y1)

        controller.image.top_layer.clear()
        controller.image.top_layer.draw(self.generateContour(), x1, y1)

        controller.view.refresh()

    def generate(self):
        radius = self.size // 2 - 1
        size = self.size * 2 - 1
        center = (size - 1) // 2

        # Create empty matrix with sharp circle in it
        mat = np.full((size, size, 4), 0, np.uint8)
        r, g, b = self.color
        cv2.circle(mat, (center, center), radius, (r, g, b, 255 * self.opacity / 100), -1)

        # Apply gaussian blur filter to the matrix
        gaussRadius = self.size - int((self.size - 3) * self.hardness / 100)
        gaussRadius += 1 - gaussRadius % 2
        mat = cv2.GaussianBlur(mat, (gaussRadius, gaussRadius), 0)

        return mat

    def generateContour(self):
        radius = self.size // 2 - 1
        size = self.size * 2 - 1
        center = (size - 1) // 2

        # Create empty matrix with sharp circle in it
        mat = np.full((size, size, 4), 0, np.uint8)
        r, g, b = self.color
        cv2.circle(mat, (center, center), radius, (0, 0, 0, 255), 1)

        return mat
