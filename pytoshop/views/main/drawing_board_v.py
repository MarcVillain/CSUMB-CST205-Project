from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel

from pytoshop.controllers.main.drawing_board_c import DrawingBoardController


class DrawingBoardView(QLabel):

    def __init__(self, parent, width, height, image_name=None):
        super().__init__(parent)
        self.parent = parent
        self.controller = DrawingBoardController(parent.controller, self, width, height, image_name)
        self.refresh()
        self.setMouseTracking(True)
        self.setGeometry(parent.width()//2-width//2, parent.height()//2-height//2, width, height)

    def refresh(self):
        image = self.controller.image

        new_width, new_height = image.width * image.scale, image.height * image.scale

        qimage = QImage(image.top_layer.rgba_display, image.width, image.height, image.bytesPerLine, QImage.Format_RGBA8888)
        qimage = qimage.scaled(new_width, new_height)
        pixmap = QPixmap(qimage)
        pixmap = pixmap.scaled(new_width, new_height)

        self.setPixmap(pixmap)
        self.setGeometry(self.x(), self.y(), new_width, new_height)

    def mousePressEvent(self, event):
        self.parent.mousePressEvent(event)
        self.controller.onMousePressed(event)

    def mouseMoveEvent(self, event):
        self.parent.mouseMoveEvent(event)
        self.controller.onMouseMove(event)

    def mouseReleaseEvent(self, event):
        self.parent.mouseReleaseEvent(event)
        self.controller.onMouseReleased(event)