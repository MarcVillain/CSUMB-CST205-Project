import sys
sys.path.append('..')

from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel
from PyQt5.QtGui import QImage,QPixmap,QPainter
from pytoshop.controllers.main_c import MainController

class DrawingBoard(QLabel):

    def __init__(self, parent, width, height, image_name=None):
        super().__init__(parent)
        self.controller = parent.controller
        self.controller.createImage(500, 500)
        
    def setImage(image, width, height, bytesPerLine):
        image = QImage(image, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap(image)
        self.setPixmap(pixmap)

    def mousePressEvent(self, event):
        self.controller.onMousePressed(event, True)

    def mouseMoveEvent(self, event):
        self.controller.onMouseMove(event, True)

class MainView(QWidget):

    def __init__(self):
        super().__init__()

        drawing_board = DrawingBoard(self, 500, 500)

        self.controller = MainController(self, drawing_board)

        self.setGeometry(0, 0, 600, 600)

    # EVENTS #

    def keyPressEvent(self, event):
        self.controller.onKeyPressed(event)

    def keyReleaseEvent(self, event):
        self.controller.onKeyReleased(event)

    def mousePressEvent(self, event):
        self.controller.onMousePressed(event, False)

    def mouseReleaseEvent(self, event):
        self.controller.onMouseReleased(event)

    def mouseMoveEvent(self, event):
        self.controller.onMouseMove(event, False)

    # FUNCTIONS #

    def changeCursor(self, cursor):
        QApplication.setOverrideCursor(cursor)
