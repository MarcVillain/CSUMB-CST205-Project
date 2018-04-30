from pytoshop.objects.tool_o import Tool


class Brush(Tool):

    def __init__(self, size=80, color=(0, 0, 0), hardness=0, opacity=100):
        super().__init__()

        self.size = size
        self.color = color
        self.hardness = hardness
        self.opacity = opacity

    def onMousePressed(self, controller, x, y):
        # TODO
        pass

    def onMouseMove(self, controller, x, y):
        controller.image.top_layer.clear()
        controller.image.top_layer.draw(self.generate(), x, y)
        controller.view.refresh()

    def onMouseReleased(self, controller, x, y):
        # TODO
        pass

    def generate(self):
        pass
