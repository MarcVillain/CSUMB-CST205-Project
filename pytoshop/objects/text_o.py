import cv2
import numpy as np
from pytoshop.objects.tool_o import Tool

class Text(Tool):
    def __init__(self, main_c, view, width, height, image_name=None):
        super().__init__(main_c, view, width, height, image_name)
        self.text = "Hello World"
        self.fontScale = 2
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.color = (0,0,0)

    def onMousePressed(self, controller, x0, y0):
        main_c.image.current_layer.draw(self.generate(x0, y0), x0, y0)
        main_c.view.refresh()

    def onMouseMoved(self, controller, x0, y0, x1, y1):
        # main_c.image.top_layer.clear()
        # main_c.image.top_layer.draw(self.generate(), x1, y1)

        main_c.view.refresh()

    def onMouseReleased(self, controller):
        pass

    def generate(self, x0, y0):
        mat = np.full((size, size, 4), 0, np.uint8)
        
        cv2.putText(mat, self.text, (x0, y0), self.font, self.color)

        return mat
