from PyQt5.QtWidgets import QLabel

from pytoshop.objects.tool_o import Tool


class Hand(Tool):

    def __init__(self):
        super().__init__()

        self.top_bar = QLabel('    Click and drag to move the drawing board.   (Shortcut: Hold Control or Cmd with any other tools)')

    def onMousePressed(self, controller, x, y):
        controller.main_c.onControlKeyPressed()

    def onMouseReleased(self, controller):
        controller.main_c.onControlKeyReleased()