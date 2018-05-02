from PyQt5 import QtWidgets

from pytoshop.controllers.main_c import MainController, DrawingBoardController
from pytoshop.objects.brushes.circle_brush import CircleBrush

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QDesktopWidget, QVBoxLayout, QGroupBox, \
    QBoxLayout
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt, QEvent, QRect

import cv2

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QMenuBar, QToolBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from pytoshop.views.ToolBar import ToolBar


class DrawingBoard(QLabel):

    def __init__(self, parent, width, height, image_name=None):
        super().__init__(parent)
        self.controller = DrawingBoardController(parent.controller, self, width, height, image_name)
        self.brush = CircleBrush()
        self.setMouseTracking(True)

    def display(self, image):
        # cv2.imwrite("layer0.png", image.layers[0].values)
        # cv2.imwrite("layer1.png", image.layers[1].values)
        # cv2.imwrite("disp_layer0.png", image.layers[0].display_values)
        # cv2.imwrite("disp_layer1.png", image.layers[1].display_values)

        new_width, new_height = image.width * image.scale, image.height * image.scale

        qimage = QImage(image.top_layer.display_values, image.width, image.height, image.bytesPerLine,
                        QImage.Format_RGBA8888)
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


class MainView(QWidget):
    WINDOW_HEIGHT = 1000
    WINDOW_WIDTH = 700
    LEFT_X = 0
    LEFT_Y = 0

    def __init__(self):
        super().__init__()
        # initialize main window
        self.setWindowTitle('Pytoshop')
        self.setGeometry(self.LEFT_X, self.LEFT_Y, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        main = QHBoxLayout()

        self.menuBar = QMenuBar()
        self.initMenuBar()
        # get toolbar
        self.toolbar = ToolBar(QBoxLayout.TopToBottom, self, QRect(0, 0, 50, 50))
        # get drawing canvas
        self.canvas = QVBoxLayout()
        self.controller = MainController(self)
        self.drawing_board = DrawingBoard(self, 950, 700)
        self.canvas.addWidget(self.drawing_board)
        # adding toolbar and canvas to main window
        main.addLayout(self.toolbar)
        main.addLayout(self.canvas)
        self.setLayout(main)

    def initMenuBar(self):
        menuItems = {
            'File': {
                'New': {'icon': 'new.png', 'trigger': self.doNothing},
                'Open': {'icon': 'open.png', 'trigger': self.doNothing},
                'Save': {'icon': 'save.png', 'trigger': self.doNothing},
                'Save As': {'icon': 'saveAs.png', 'trigger': self.doNothing},
                'Export': {'icon': 'export.png', 'trigger': self.doNothing},
                'Exit': {'icon': 'exit.png', 'trigger': self.close}
            },
            'Layer': {
                'Filters': {
                    'Grayscale': {'trigger': self.doNothing},
                    'Sepia': {'trigger': self.doNothing},
                    'Negative': {'trigger': self.doNothing}
                }
            }
            # 'Toolbar': {
            #     'Brush': {'icon': 'brush.png'},
            #     'Select': {'icon': 'select.png'},
            #     'Erase': {'icon': 'erase.png'},
            #     'Color Picker': {'icon': 'color.png'},
            #     'Text': {'icon': 'text1.png'},
            #     'Magnifier': {'icon': 'zoom.png'}
            # }
        }

        self.addMenuItems(self.menuBar, menuItems)

    def addMenuItems(self, menuBar, menuItems):
        for title, subItems in menuItems.items():
            menu = menuBar.addMenu(title)

            for key, value in subItems.items():
                try:
                    action = QAction(QIcon('pytoshop/views/images/' + value['icon']), '&' + key, menu)
                except:
                    action = QAction('&' + key, menu)

                try:
                    menu.triggered.connect(value['trigger'])
                    menu.addAction(action)
                except:
                    self.addMenuItems(menu, subItems)

    def doNothing(self):
        print('Do nothing')
        pass

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
