from pytoshop.objects.brushes.circle_brush import CircleBrush
from pytoshop.objects.brushes.eraser_brush import EraserBrush
from pytoshop.objects.image_o import Image


class DrawingBoardController:

    def __init__(self, main_c, view, width, height, image_name=None):
        self.main_c = main_c
        self.view = view

        self.image = Image(width, height, image_name)
        self.tool = CircleBrush()

        self.mouse_pressed = False

    def onMousePressed(self, event):
        self.mouse_pressed = True
        pos = event.pos()

        self.tool.onMousePressed(self, pos.x(), pos.y())

    def onMouseMove(self, event):
        pos = event.pos()

        self.tool.onMouseMove(self, pos.x(), pos.y())

    def onMouseReleased(self, event):
        self.mouse_pressed = False
        pos = event.pos()

        self.tool.onMouseReleased(self, pos.x(), pos.y())

    def onWheel(self, angleDeltaY):
        self.image.scale += angleDeltaY * 0.01
        self.image.scale = max(self.image.min_scale, min(self.image.scale, self.image.max_scale))
        self.view.refresh()

    def onLeave(self):
        self.image.top_layer.clear()
        self.view.refresh()
        self.main_c.view.showArrowCursor()
