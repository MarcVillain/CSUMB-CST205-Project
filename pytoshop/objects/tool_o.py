from PyQt5.QtWidgets import QWidget


class Tool:

    def __init__(self):
        self.top_bar = QWidget()
        pass

    def onMousePressed(self, controller, x, y):
        pass

    def onMouseMove(self, controller, fromX, fromY, toX, toY):
        pass

    def onMouseReleased(self, controller):
        pass