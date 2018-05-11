import cv2
import numpy as np
from pytoshop.objects.tool_o import Tool
from pytoshop.views.main.top_bars.top_bar_text import TopBarText

class Text(Tool):
    def __init__(self, main_c, view, width, height, image_name=None):
        super().__init__()
        self.main_c = main_c
        self.view = view
        self.width = width
        self.height = height
        self.text = "Hello World"
        self.fontScale = 2
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.color = (0, 0, 0, 255)
        self.top_bar = TopBarText(self)

    def onMousePressed(self, controller, x0, y0):

        controller.image.current_layer.draw(self.generate(controller, x0, y0), controller.image.width//2, controller.image.height//2)
        controller.view.refresh()

    def onMouseMove(self, controller, x0, y0, x1, y1):
        # main_c.image.top_layer.clear()
        # main_c.image.top_layer.draw(self.generate(), x1, y1)

        #self.main_c.view.refresh()
        pass

    def onMouseReleased(self, controller):
        pass

    def generate(self, controller, x0, y0):
        height = controller.image.height
        if controller.image.height % 2 == 0:
            height -= 1

        width = controller.image.width
        if controller.image.width % 2 == 0:
            width -= 1

        mat = np.full((height, width, 4), 0, np.uint8)

        cv2.putText(mat, self.text, (x0, y0), self.font, self.fontScale, self.color, 1)

        return mat
