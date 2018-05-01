from pytoshop.objects.tool_o import Tool


class Brush(Tool):

    def __init__(self, size=20, color=(0, 0, 0), hardness=100, opacity=100):
        super().__init__()

        self.size = size
        self.color = color
        self.hardness = hardness
        self.opacity = opacity

    def onMousePressed(self, controller, x0, y0):
        controller.image.current_layer.draw(self.generate(), x0, y0)
        controller.view.refresh()

    def onMouseMove(self, controller, x0, y0, x1, y1):
        if controller.mouse_pressed:
            controller.image.current_layer.drawLine(self.generate(), x0, y0, x1, y1)

        controller.image.top_layer.clear()
        controller.image.top_layer.draw(self.generate(), x1, y1)

        controller.view.refresh()

    def onMouseReleased(self, controller):
        # TODO
        pass

    def generate(self):
        pass
