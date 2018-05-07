import cv2
<<<<<<< HEAD
=======
from PyQt5.QtCore import Qt
>>>>>>> master
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel

from pytoshop.controllers.drawing_board_c import DrawingBoardController
from pytoshop.utils.color_u import rgb_to_rgba


<<<<<<< HEAD
class DrawingBoard(QLabel):
=======
class DrawingBoardView(QLabel):
>>>>>>> master

    def __init__(self, parent, width, height, image_name=None):
        super().__init__(parent)
        self.parent = parent
        self.controller = DrawingBoardController(parent.controller, self, width, height, image_name)
        self.refresh()
        self.setMouseTracking(True)
<<<<<<< HEAD

    def refresh(self):
        image = self.controller.image
        #cv2.imwrite("layer0.png", rgb_to_rgba(image.layers[0].rgb, image.layers[0].alpha))
        #cv2.imwrite("layer1.png", rgb_to_rgba(image.layers[1].rgb, image.layers[1].alpha))
        #cv2.imwrite("disp_layer0.png", image.layers[0].rgba_display)
        #cv2.imwrite("disp_layer1.png", image.layers[1].rgba_display)
=======
        self.setGeometry(parent.width()//2-width//2, parent.height()//2-height//2, width, height)

    def refresh(self):
        image = self.controller.image
>>>>>>> master

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
<<<<<<< HEAD
        self.controller.onMouseReleased(event)
=======
        self.controller.onMouseReleased(event)
>>>>>>> master
