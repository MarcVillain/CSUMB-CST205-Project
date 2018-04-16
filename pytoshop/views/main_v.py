import sys
sys.path.append('..')

from PyQt5.QtWidgets import QApplication,QWidget,QLabel
from pytoshop.controllers.main_c import MainController

class Workspace(QLabel):

    def __init__(self, parent):
        super().__init__(parent)

        self.setText('Test')
        self.width = 80
        self.height = 20
        self.setGeometry(0, 0, 80, 20)
        self.setStyleSheet('background: red')

class MainView(QWidget):

    def __init__(self):
        super().__init__()

        self.controller = MainController(self)

        self.workspace = Workspace(self)
        self.setGeometry(0, 0, 600, 600)

    # EVENTS #

    def keyPressEvent(self, event):
        self.controller.onKeyPressed(event)

    def keyReleaseEvent(self, event):
        self.controller.onKeyReleased(event)

    def mousePressEvent(self, event):
        self.controller.onMousePressed(event)

    def mouseReleaseEvent(self, event):
        self.controller.onMouseReleased(event)

    def mouseMoveEvent(self, event):
        self.controller.onMouseMove(event)

    # FUNCTIONS #

    def changeCursor(self, cursor):
        QApplication.setOverrideCursor(cursor)
