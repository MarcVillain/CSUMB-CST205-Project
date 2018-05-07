import cv2
import numpy as np

from pytoshop.utils.blend_u import normal, blend
from pytoshop.utils.color_u import color_add_rgb, rgb_to_rgba, rgba_to_rgb
from pytoshop.utils.color_u import color_add_rgba


class Layer:

    def __init__(self, image, bottom_layer=None, top_layer=None, pos=-1):
        self.pos = pos
        self.image = image
        self.bottom_layer = bottom_layer
        self.top_layer = top_layer

        self.blend_mode = normal
        self.name = 'None'

        self.clear()

    def fill(self, color):
        self.rgb = np.full((self.image.height, self.image.width, 3), color, np.uint8)
        self.alpha = np.full((self.image.height, self.image.width, 1), 1.)

        self.updateDisplay(0, self.image.height, 0, self.image.width)

    def clear(self):
        self.rgb = np.full((self.image.height, self.image.width, 3), 0, np.uint8)
        self.alpha = np.full((self.image.height, self.image.width, 1), 0.)
        self.rgba_display = np.full((self.image.height, self.image.width, 4), 0, np.uint8)

        self.updateDisplay(0, self.image.height, 0, self.image.width)

    def applyFilter(self, filter_func):
        self.rgb = filter_func(self.rgb)
        self.updateDisplay(0, self.image.height, 0, self.image.width)

    def draw(self, rgba, x0, y0):
        print('x0:', x0, 'y0: ', y0)
        rgb, alpha = rgba_to_rgb(rgba)

        size = len(rgb)
        r = size // 2

        distTop, distBottom = y0 - r, y0 + r + 1
        padTop, padBottom = max(0, distTop), min(self.image.height, distBottom)

        distLeft, distRight = x0 - r, x0 + r + 1
        padLeft, padRight = max(0, distLeft), min(self.image.width, distRight)

        out_top = max(0, r - y0)
        out_bottom = max(0, y0 - self.image.height + 1 + r)
        out_left = max(0, r - x0)
        out_right = max(0, x0 - self.image.width + 1 + r)

        top_start_y = out_top
        top_end_y = size - out_bottom
        top_start_x = out_left
        top_end_x = size - out_right

        bcg_start_y = max(0, y0 - r)
        bcg_end_y = min(self.image.height, y0 + r + 1)
        bcg_start_x = max(0, x0 - r)
        bcg_end_x = min(self.image.width, x0 + r + 1)

        if (top_start_x == top_end_x or top_start_y == top_end_y or bcg_start_x == bcg_end_x or bcg_start_y == bcg_end_y or top_start_x < 0 or top_end_x < 0 or top_start_y < 0 or top_end_y < 0 or bcg_start_x < 0 or bcg_end_x < 0 or bcg_start_y < 0 or bcg_end_y < 0):
            return # Out of drawing bounds

        top_color = rgb[top_start_y:top_end_y, top_start_x:top_end_x]
        top_alpha = alpha[top_start_y:top_end_y, top_start_x:top_end_x]
        bcg_color = self.rgb[bcg_start_y:bcg_end_y, bcg_start_x:bcg_end_x]
        bcg_alpha = self.alpha[bcg_start_y:bcg_end_y, bcg_start_x:bcg_end_x]

        new_rgb, new_alpha = blend(top_color, top_alpha, bcg_color, bcg_alpha)

        self.rgb[bcg_start_y:bcg_end_y, bcg_start_x:bcg_end_x] = new_rgb
        self.alpha[bcg_start_y:bcg_end_y, bcg_start_x:bcg_end_x] = new_alpha

        self.updateDisplay(bcg_start_y, bcg_end_y, bcg_start_x, bcg_end_x)

    def drawLine(self, rgba, x0, y0, x1, y1):
        """
        Bresenham's algorithm
        """
        # TODO: Generate and blur a real line instead of doing something like this...
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
            self.image.current_layer.draw(rgba, x0 + x * xx + y * yx, y0 + x * xy + y * yy)
            if D >= 0:
                y += 1
                D -= 2 * dx
            D += 2 * dy

    def updateDisplay(self, padTop, padBottom, padLeft, padRight):
        if self.bottom_layer is not None:
            rgb_bottom, alpha_bottom = rgba_to_rgb(self.bottom_layer.rgba_display[padTop:padBottom, padLeft:padRight])
            new_rgb, new_alpha = blend(self.rgb[padTop:padBottom, padLeft:padRight], self.alpha[padTop:padBottom, padLeft:padRight], rgb_bottom, alpha_bottom, self.blend_mode)
            self.rgba_display[padTop:padBottom, padLeft:padRight] = rgb_to_rgba(new_rgb, new_alpha)
        else:
            self.rgba_display[padTop:padBottom, padLeft:padRight] = rgb_to_rgba(self.rgb[padTop:padBottom, padLeft:padRight], self.alpha[padTop:padBottom, padLeft:padRight])

        if self.top_layer is not None:
            self.top_layer.updateDisplay(padTop, padBottom, padLeft, padRight)
