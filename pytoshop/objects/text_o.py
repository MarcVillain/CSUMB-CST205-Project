import cv2
import numpy as np
from tool_o import Tool

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
        thing = cv2.putText(main_c.image.newLayer(), self.text, (x0, y0), self.font, self.color)
        temp_layer = main_c.image.top_layer
        for row in range(len(main_c.image.top_layer)):
            for column in range(len(main_c.image.top_layer[0])):
                if(thing[row][column] != (255,255,255)):
                    temp_layer[row][column] = thing[row][column]
        main_c.image.top_layer = temp_layer;
        main_c.view.refresh()
