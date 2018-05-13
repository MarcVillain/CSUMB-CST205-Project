from pytoshop.objects.image_o import Image


class DrawingBoardController:

    def __init__(self, main_c, view, width, height, image_name=None):
        self.main_c = main_c
        self.view = view

        self.image = Image(width, height, image_name)
        self.tool = self.main_c.view.tools['brush']

        self.lastPos = None
        self.mouse_pressed = False

    def onMousePressed(self, event):
        if not self.main_c.control_pressed:
            self.main_c.view.layers.refresh(self.image.current_layer.pos)
            self.mouse_pressed = True
            self.lastPos = self.image.map(event.x(), event.y(), self.view.width(), self.view.height())
            self.tool.onMousePressed(self, self.lastPos[0], self.lastPos[1])

    def onMouseMove(self, event):
        if not self.main_c.control_pressed:
            self.main_c.view.layers.refresh(self.image.current_layer.pos)
            pos = self.image.map(event.x(), event.y(), self.view.width(), self.view.height())
            if self.lastPos is None:
                self.lastPos = pos
            self.tool.onMouseMove(self, self.lastPos[0], self.lastPos[1], pos[0], pos[1])
            self.lastPos = pos

    def onMouseReleased(self, event):
        if not self.main_c.control_pressed:
            self.main_c.view.layers.refresh(self.image.current_layer.pos)
            self.mouse_pressed = False
            self.tool.onMouseReleased(self)

    def onWheel(self, angleDeltaY):
        self.image.scale += angleDeltaY * 0.001
        self.image.scale = max(self.image.min_scale, min(self.image.scale, self.image.max_scale))
        self.view.refresh()

    def onLeave(self):
        self.image.top_layer.clear()
        self.view.refresh()
        self.main_c.view.showArrowCursor()
