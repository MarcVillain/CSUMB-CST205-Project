from pytoshop.objects.tool_o import Tool


class Zoom(Tool):

    def __init__(self):
        super().__init__()
        self.isPressed = False
        self.top_bar = None

    def onMousePressed(self, controller, x, y):
        self.isPressed = True
        self.hasMoved = False

    def onMouseMove(self, controller, fromX, fromY, toX, toY):
        if self.isPressed:
            self.hasMoved = True
            controller.onWheel(toY - fromY + toX - fromX)

    def onMouseReleased(self, controller):
        self.isPressed = False

        if not self.hasMoved:
            delta = 200
            if controller.main_c.alt_pressed:
                delta *= -1
            controller.onWheel(delta)