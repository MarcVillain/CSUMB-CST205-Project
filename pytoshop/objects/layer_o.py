import numpy as np

from pytoshop.utils.blend_u import normal, blend
from pytoshop.utils.color_u import rgb_to_rgba, rgba_to_rgb
from pytoshop.utils.matrix_u import intersect, intersect_both
from pytoshop.views.main.layers_v import LayersItem


class Layer:

    def __init__(self, image, bottom_layer=None, top_layer=None, pos=-1):
        self.pos = pos
        self.image = image
        self.bottom_layer = bottom_layer
        self.top_layer = top_layer
        self.location = 0, 0

        self.blend_mode = normal
        self.x, self.y = 0, 0

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

    def draw(self, rgba, x0, y0, centered=True):
        x = x0 - len(rgba[0])//2 if centered else x0
        y = y0 - len(rgba) // 2 if centered else y0

        top_pos, bcg_pos = intersect_both(rgba, self.rgba_display, x, y)

        if top_pos is None or bcg_pos is None:
            return

        rgb, alpha = rgba_to_rgb(rgba)

        top_color = rgb[top_pos[1]:top_pos[3], top_pos[0]:top_pos[2]]
        top_alpha = alpha[top_pos[1]:top_pos[3], top_pos[0]:top_pos[2]]
        bcg_color = self.rgb[bcg_pos[1]:bcg_pos[3], bcg_pos[0]:bcg_pos[2]]
        bcg_alpha = self.alpha[bcg_pos[1]:bcg_pos[3], bcg_pos[0]:bcg_pos[2]]

        new_rgb, new_alpha = blend(top_color, top_alpha, bcg_color, bcg_alpha)

        self.rgb[bcg_pos[1]:bcg_pos[3], bcg_pos[0]:bcg_pos[2]] = new_rgb
        self.alpha[bcg_pos[1]:bcg_pos[3], bcg_pos[0]:bcg_pos[2]] = new_alpha

        self.updateDisplay(bcg_pos[1], bcg_pos[3], bcg_pos[0], bcg_pos[2])

    def erase(self, rgba, x0, y0, centered=True):
        x = x0 - len(rgba[0]) // 2 if centered else x0
        y = y0 - len(rgba) // 2 if centered else y0

        top_pos, bcg_pos = intersect_both(rgba, self.rgba_display, x, y)

        if top_pos is None or bcg_pos is None:
            return

        rgb, alpha = rgba_to_rgb(rgba)

        new_array = np.array(self.alpha[bcg_pos[1]:bcg_pos[3], bcg_pos[0]:bcg_pos[2]]) - np.array(alpha[top_pos[1]:top_pos[3], top_pos[0]:top_pos[2]])
        new_array[new_array < 0] = 0
        self.alpha[bcg_pos[1]:bcg_pos[3], bcg_pos[0]:bcg_pos[2]] = new_array

        self.updateDisplay(bcg_pos[1], bcg_pos[3], bcg_pos[0], bcg_pos[2])

    def drawLine(self, rgba, x0, y0, x1, y1):
        """
        Bresenham's algorithm
        """
        dx = x1 - x0
        dy = y1 - y0

        if dx == 0 and dy == 0:
            return

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

    def eraseLine(self, rgba, x0, y0, x1, y1):
        """
        Bresenham's algorithm
        """
        dx = x1 - x0
        dy = y1 - y0

        if dx == 0 and dy == 0:
            return

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
            self.image.current_layer.erase(rgba, x0 + x * xx + y * yx, y0 + x * xy + y * yy)
            if D >= 0:
                y += 1
                D -= 2 * dx
            D += 2 * dy

    def updateDisplay(self, start_y, end_y, start_x, end_x):
        if self.bottom_layer is not None:
            rgb_bottom, alpha_bottom = rgba_to_rgb(self.bottom_layer.rgba_display[start_y:end_y, start_x:end_x])
            new_rgb, new_alpha = blend(self.rgb[start_y:end_y, start_x:end_x], self.alpha[start_y:end_y, start_x:end_x], rgb_bottom, alpha_bottom, self.blend_mode)
            self.rgba_display[start_y:end_y, start_x:end_x] = rgb_to_rgba(new_rgb, new_alpha)
        else:
            self.rgba_display[start_y:end_y, start_x:end_x] = rgb_to_rgba(self.rgb[start_y:end_y, start_x:end_x], self.alpha[start_y:end_y, start_x:end_x])

        if self.top_layer is not None:
            self.top_layer.updateDisplay(start_y, end_y, start_x, end_x)

    def fill_checker(self, colorA, colorB, size):
        color = (colorA, colorB)
        colorID = 0
        for j in range(self.image.height):
            for i in range(self.image.width):
                if (i+1) % size == 0:
                    colorID = (colorID + 1) % 2

                for k in range(3):
                    self.rgb[j][i][k] = color[colorID][k]
                self.alpha[j][i][0] = 1

            if (j+1) % size == 0:
                colorID = (colorID + 1) % 2

        self.updateDisplay(0, self.image.height, 0, self.image.width)
