import cv2
import numpy as np
from pytoshop.objects.layer_o import Layer


class Text(Layer):

    def __init__(self, main_c, view, width, height, image_name=None):
        super().__init__(main_c, view, width, height, image_name)
        self.text = "Hello World"
        self.fontScale = 2
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.color = (0,0,0)

        cv2.putText(self.image, self.text, (10,500), self.font, self.fontScale, self.color)
