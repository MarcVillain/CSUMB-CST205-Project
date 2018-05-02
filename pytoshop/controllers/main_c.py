import numpy as np

from pytoshop.objects.brushes.circle_brush import CircleBrush
from pytoshop.objects.brushes.eraser_brush import EraserBrush

from pytoshop.objects.image_o import Image
from pytoshop.objects.text_o import Text


class DrawingBoardController:

    def __init__(self, main_c, view, width, height, image_name=None):
        self.main_c = main_c
        self.view = view
        self.lastPoint = None

        self.image = Image(width, height, image_name)
        self.view.display(self.image)

        self.pressing = False

        self.test_switch = 0
        self.test_switch_2 = 0
        self.test_switch_3 = 0

    def onMousePressed(self, event):
        if self.main_c.command_pressed:
            self.main_c.onMousePressed(event.globalPos())
        else:
            self.lastPoint = self.image.map(event.x(), event.y(), self.view.width(), self.view.height())
            self.image.draw(self.view.brush, self.lastPoint)
            self.view.display(self.image)
        self.pressing = True

    def onMouseMove(self, event):
        if self.pressing and self.main_c.command_pressed:
            self.main_c.onMouseMove(event.globalPos())
        elif self.lastPoint is not None:  # If pressing
            endPoint = self.image.map(event.x(), event.y(), self.view.width(), self.view.height())
            self.image.drawLine(self.view.brush, self.lastPoint, endPoint)
            self.lastPoint = endPoint
            self.view.display(self.image)
        else:
            self.main_c.view.hideCursor()
            self.image.top_layer.clear()
            startPoint = self.image.map(event.x(), event.y(), self.view.width(), self.view.height())
            self.image.drawBrush(self.view.brush, startPoint)
            self.view.display(self.image)

    def onMouseReleased(self, event):
        if self.main_c.command_pressed:
            self.main_c.onMouseReleased()
        else:
            self.lastPoint = None
        self.pressing = False

    def switchLayer(self):
        if self.test_switch == 0:
            self.view.brush.color = (255, 0, 0)
            self.image.current_layer = self.image.layers[0]
            self.test_switch = 1
        else:
            self.view.brush.color = (0, 0, 0)
            self.image.current_layer = self.image.layers[1]
            self.test_switch = 0

    def switchBrushColor(self):
        if self.test_switch_3 == 0:
            self.view.brush.color = (255, 0, 0)
            self.test_switch_3 = 1
        elif self.test_switch_3 == 1:
            self.view.brush.color = (0, 0, 255)
            self.test_switch_3 = 2
        else:
            self.view.brush.color = (127, 255, 0)
            self.test_switch_3 = 0

    def switchBrush(self):
        if self.test_switch_2 == 0:
            self.view.brush = EraserBrush()
            self.test_switch_2 = 1
        else:
            self.view.brush = CircleBrush()
            self.test_switch_2 = 0

    def switchText(self):
        Text(self.main_c, self.view, self.width, self.height, self.image)

    def onWheel(self, angleDeltaY):
        self.image.scale += angleDeltaY * 0.01
        self.image.scale = max(self.image.min_scale, min(self.image.scale, self.image.max_scale))
        self.view.display(self.image)

    def onLeave(self):
        self.image.top_layer.clear()
        self.view.display(self.image)
        self.main_c.view.showArrowCursor()



class MainController:

    def __init__(self, view):
        self.view = view
        self.command_pressed = False

    def onControlPressed(self):
        self.command_pressed = True
        self.view.showOpenHandCursor()

    def onControlReleased(self):
        self.command_pressed = False
        self.view.showArrowCursor()

    def onMousePressed(self, pos):
        if self.command_pressed:
            self.startBoard = self.view.drawing_board.pos()
            self.startPoint = pos
            self.view.showClosedHandCursor()

    def onMouseReleased(self):
        if self.command_pressed:
            self.view.showOpenHandCursor()

    def onMouseMove(self, pos):
        if self.command_pressed:
            end_point = pos

            deltaX = end_point.x() - self.startPoint.x()
            deltaY = end_point.y() - self.startPoint.y()

            newX = self.startBoard.x() + deltaX
            newY = self.startBoard.y() + deltaY

            self.view.drawing_board.move(newX, newY)
