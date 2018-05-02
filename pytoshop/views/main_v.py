from pytoshop.controllers.main_c import MainController, DrawingBoardController
from pytoshop.objects.brushes.circle_brush import CircleBrush

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QDesktopWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt, QEvent

import cv2


from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QMenuBar, QToolBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class DrawingBoard(QLabel):

    def __init__(self, parent, width, height, image_name=None):
        super().__init__(parent)
        self.controller = DrawingBoardController(parent.controller, self, width, height, image_name)
        self.brush = CircleBrush()
        self.setMouseTracking(True)

    def display(self, image):
        #cv2.imwrite("layer0.png", image.layers[0].values)
        #cv2.imwrite("layer1.png", image.layers[1].values)
        #cv2.imwrite("disp_layer0.png", image.layers[0].display_values)
        #cv2.imwrite("disp_layer1.png", image.layers[1].display_values)

        new_width, new_height = image.width * image.scale, image.height * image.scale

        qimage = QImage(image.top_layer.display_values, image.width, image.height, image.bytesPerLine, QImage.Format_RGBA8888)
        qimage = qimage.scaled(new_width, new_height)
        pixmap = QPixmap(qimage)
        pixmap = pixmap.scaled(new_width, new_height)

        self.setPixmap(pixmap)
        self.setGeometry(self.x(), self.y(), new_width, new_height)

    def mousePressEvent(self, event):
        self.controller.onMousePressed(event)

    def mouseMoveEvent(self, event):
        self.controller.onMouseMove(event)

    def mouseReleaseEvent(self, event):
        self.controller.onMouseReleased(event)

    def leaveEvent(self, event):
        self.controller.onLeave()

    def wheelEvent(self, event):
        self.controller.onWheel(event.angleDelta().y())


class MainView(QMainWindow):

    def __init__(self):
        super().__init__()
        self.controller = MainController(self)

        self.setWindowTitle('Pytoshop')
        self.initGeometry(650, 400)
        self.initMenuBar()

        self.drawing_board = DrawingBoard(self, 500, 500)

        hlayout = QHBoxLayout()
        hlayout.addWidget(self.drawing_board)
        self.setLayout(hlayout)

        self.show()

    def initMenuBar(self):
        menuItems = {
            'File': {
                'New': {'icon': 'new.png'},
                'Open': {'icon': 'open.png'},
                'Save': {'icon': 'save.png'},
                'Save As': {'icon': 'saveAs.png'},
                'Export': {'icon': 'export.png'},
                'Exit': {'icon': 'exit.png', 'trigger': self.close}
            },
            'Filters': {
                'Grayscale': {},
                'Sepia': {},
                'Negative': {}
            },
            'Toolbar': {
                'Brush': {'icon': 'brush.png'},
                'Select': {'icon': 'select.png'},
                'Erase': {'icon': 'erase.png'},
                'Color Picker': {'icon': 'color.png'},
                'Text': {'icon': 'text1.png'},
                'Magnifier': {'icon': 'zoom.png'}
            }
        }

        menuBar = self.menuBar()

        for title, subItems in menuItems.items():
            menu = menuBar.addMenu(title)

            for key, value in subItems.items():
                try:
                    action = QAction(QIcon('pytoshop/views/images/' + value['icon']), '&' + key, menu)
                except:
                    action = QAction('&' + key, menu)

                try:
                    menu.triggered.connect(value['trigger'])
                except:
                    pass

                menu.addAction(action)

    def initGeometry(self, width, height):
        # Set size
        self.setGeometry(0, 0, width, height)

        # Center window
        frame = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(centerPoint)
        self.move(frame.topLeft())

    # EVENTS #

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Control:
            self.controller.onControlPressed()
        elif event.key() == Qt.Key_A:
            self.drawing_board.controller.switchLayer()
        elif event.key() == Qt.Key_C:
            self.drawing_board.controller.switchBrushColor()
        elif event.key() == Qt.Key_B:
            self.drawing_board.controller.switchBrush()
        elif event.key() == Qt.Key_T:
            self.drawing_board.controller.switchText()

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Control:
            self.controller.onControlReleased()

    def mousePressEvent(self, event):
        self.controller.onMousePressed(event.globalPos())

    def mouseReleaseEvent(self, event):
        self.controller.onMouseReleased()

    def mouseMoveEvent(self, event):
        self.controller.onMouseMove(event.globalPos())

    def wheelEvent(self, event):
        self.drawing_board.wheelEvent(event)

    # FUNCTIONS #

    def hideCursor(self):
        QApplication.setOverrideCursor(Qt.BlankCursor)

    def showOpenHandCursor(self):
        QApplication.setOverrideCursor(Qt.OpenHandCursor)

    def showClosedHandCursor(self):
        QApplication.setOverrideCursor(Qt.ClosedHandCursor)

    def showArrowCursor(self):
        QApplication.setOverrideCursor(Qt.ArrowCursor)
