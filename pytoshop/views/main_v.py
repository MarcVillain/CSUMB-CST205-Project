import sys

sys.path.append('..')

from pytoshop.controllers.main_c import MainController, DrawingBoardController
from pytoshop.objects.brush_o import Brush

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QMenu, QAction, QDesktopWidget, QHBoxLayout
from PyQt5.QtGui import QImage, QPixmap, QPainter
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QMenuBar, QToolBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class DrawingBoard(QLabel):

    def __init__(self, parent, width, height, image_name=None):
        super().__init__()
        self.controller = DrawingBoardController(parent.controller, self)
        self.controller.createImage(width, height)
        self.brush = Brush()

        self.setGeometry(0, 0, width, height)

    def displayImage(self, image):
        image = QImage(image.value, image.width, image.height, image.bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap(image)
        self.setPixmap(pixmap)

    def mousePressEvent(self, event):
        self.controller.onMousePressed(event)

    def mouseMoveEvent(self, event):
        self.controller.onMouseMove(event)


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

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Control:
            self.controller.onControlReleased()

    def mousePressEvent(self, event):
        self.controller.onMousePressed(event.globalPos())

    def mouseReleaseEvent(self, event):
        self.controller.onMouseReleased()

    def mouseMoveEvent(self, event):
        self.controller.onMouseMove(event.globalPos())

    # FUNCTIONS #

    def showOpenHandCursor(self):
        QApplication.setOverrideCursor(Qt.OpenHandCursor)

    def showClosedHandCursor(self):
        QApplication.setOverrideCursor(Qt.ClosedHandCursor)

    def showArrowCursor(self):
        QApplication.setOverrideCursor(Qt.ArrowCursor)
