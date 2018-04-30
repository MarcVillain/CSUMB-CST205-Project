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

        self.clear()

    def clear(self):
        self.rgb = np.full((self.image.height, self.image.width, 3), 0, np.uint8)
        self.alpha = np.full((self.image.height, self.image.width, 1), 0)

        if self.bottom_layer is None:
            self.rgba_display = np.full((self.image.height, self.image.width, 4), 0, np.uint8)
        else:
            self.rgba_display = np.copy(self.bottom_layer.rgba_display)

    def draw(self, rgba, x0, y0):
        r, g, b, a = cv2.split(rgba)
        rgb = cv2.merge((r, g, b))
        alpha = a[..., None]

        size = len(rgb)
        r = size // 2

        distTop, distBottom = y0 - r, y0 + r + 1
        padTop, padBottom = max(0, distTop), min(self.image.height - 1, distBottom)

        distLeft, distRight = x0 - r, x0 + r + 1
        padLeft, padRight = max(0, distLeft), min(self.image.width - 1, distRight)

        top_color = rgb[padTop - distTop:size - (distBottom - padBottom), padLeft - distLeft:size - (distRight - padRight)]
        top_alpha = alpha[padTop - distTop:size - (distBottom - padBottom), padLeft - distLeft:size - (distRight - padRight)]
        bcg_color = self.rgb[padTop:padBottom, padLeft:padRight]
        bcg_alpha = self.alpha[padTop:padBottom, padLeft:padRight]

        new_rgb, new_alpha = blend(top_color, top_alpha, bcg_color, bcg_alpha, self.blend_mode)

        self.rgb[padTop:padBottom, padLeft:padRight] = new_rgb
        self.alpha[padTop:padBottom, padLeft:padRight] = new_alpha

        r, g, b = cv2.split(new_rgb)
        a = (cv2.split(np.uint8(new_alpha*255))[0])

        self.rgba_display[padTop:padBottom, padLeft:padRight] = cv2.merge((r, g, b, a))
