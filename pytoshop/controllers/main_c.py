import sys
sys.path.append('..')

from pytoshop.objects.image_o import Image

class DrawingBoardController:

    def __init__(self, main_c, view):
        self.main_c = main_c
        self.view = view
        self.lastPoint = None

    def onMousePressed(self, event):
        if self.main_c.command_pressed:
            self.main_c.onMousePressed(event.globalPos())
        else:
            self.lastPoint = event.x(), event.y()
            self.image.draw(self.view.brush, event.x(), event.y())
            self.view.displayImage(self.image)

    def onMouseMove(self, event):
        if self.main_c.command_pressed:
            self.main_c.onMouseMove(event.globalPos())
        else:
            self.image.drawLine(self.view.brush, event.x(), event.y(), self.lastPoint[0], self.lastPoint[1])
            self.lastPoint = event.x(), event.y()
            self.view.displayImage(self.image)

    def onMouseReleased(self, event):
        if self.main_c.command_pressed:
            self.main_c.onMouseReleased()
        else:
            self.lastPoint = None

    def createImage(self, width, height, image_name=None):
        self.image = Image(width, height, image_name)
        self.view.displayImage(self.image)

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
            self.start_board = self.view.drawing_board.pos()
            self.start_point = pos
            self.view.showClosedHandCursor()

    def onMouseReleased(self):
        if self.command_pressed:
            self.view.showOpenHandCursor()

    def onMouseMove(self, pos):
        if self.command_pressed:
            end_point = pos

            deltaX = end_point.x() - self.start_point.x()
            deltaY = end_point.y() - self.start_point.y()

            newX = self.start_board.x() + deltaX
            newY = self.start_board.y() + deltaY

            self.view.drawing_board.move(newX, newY)
