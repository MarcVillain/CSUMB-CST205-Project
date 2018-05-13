import numpy as np
from PyQt5.QtWidgets import QLabel

from scipy.ndimage import shift

from pytoshop.objects.tool_o import Tool


class Move(Tool):

    def __init__(self):
        super().__init__()

        self.isPressed = False

        self.top_bar = QLabel('&nbsp;&nbsp;&nbsp;&nbsp;(beta) Click and drag slowly to move the layer around. &nbsp; <b>/!\ Every pixel moved outside the drawing board will be lost /!\</b>')

    def onMousePressed(self, controller, x, y):
        self.isPressed = True

    def onMouseMove(self, controller, fromX, fromY, toX, toY):
        if self.isPressed:
            controller.image.current_layer.rgb = shift(controller.image.current_layer.rgb, (toY - fromY, toX - fromX, 0), cval=0)
            controller.image.current_layer.alpha = shift(controller.image.current_layer.alpha, (toY - fromY, toX - fromX, 0), cval=0)
            controller.image.current_layer.updateDisplay(0, controller.image.height, 0, controller.image.width)
            controller.view.refresh()

    def onMouseReleased(self, controller):
        self.isPressed = False
