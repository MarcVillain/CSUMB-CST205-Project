from pytoshop.objects.tool_o import Tool
from pytoshop.views.main.top_bars.top_bar_brush import TopBarBrush


class Hand(Tool):

    def __init__(self):
        super().__init__()
        self.top_bar = None

    def onMousePressed(self, controller, x, y):
        controller.main_c.onControlKeyPressed()

    def onMouseReleased(self, controller):
        controller.main_c.onControlKeyReleased()