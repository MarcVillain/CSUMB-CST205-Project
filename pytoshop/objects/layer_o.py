import cv2
import numpy as np

from pytoshop.utils.blend_u import normal, blend
from pytoshop.utils.color import color_add_rgb
from pytoshop.utils.color import color_add_rgba


class Layer:

    def __init__(self, image, bottom_layer=None, top_layer=None):
        self.image = image
        self.bottom_layer = bottom_layer
        self.top_layer = top_layer

        self.blend_mode = normal

        self.rgb = np.full((image.height, image.width, 3), 0, np.uint8)
        self.alpha = np.full((image.height, image.width, 1), 0)

        if bottom_layer is None:
            self.rgba_display = np.full((image.height, image.width, 4), 0, np.uint8)
        else:
            self.rgba_display = np.copy(bottom_layer.rgba_display)

    def draw(self, rgb, alpha, x0, y0):
        size = len(rgb)
        r = size // 2

        distTop, distBottom = y0 - r, y0 + r + 1
        padTop, padBottom = max(0, distTop), min(self.image.height - 1, distBottom)

        distLeft, distRight = x0 - r, x0 + r + 1
        padLeft, padRight = max(0, distLeft), min(self.image.width - 1, distRight)

        top_color = self.rgb[padTop:padBottom, padLeft:padRight]
        top_alpha = self.alpha[padTop:padBottom, padLeft:padRight]
        bcg_color = rgb[padTop - distTop:size - (distBottom - padBottom), padLeft - distLeft:size - (distRight - padRight)]
        bcg_alpha = alpha[padTop - distTop:size - (distBottom - padBottom), padLeft - distLeft:size - (distRight - padRight)]

        self.rgb[padTop:padBottom, padLeft:padRight], self.alpha[padTop:padBottom, padLeft:padRight] = blend(top_color, top_alpha, bcg_color, bcg_alpha, self.blend_mode)

        r, g, b = cv2.split(self.rgb)
        a = (cv2.split(self.alpha)[0]*255).astype(np.uint8)

        self.rgba_display = cv2.merge((r, g, b, a))

