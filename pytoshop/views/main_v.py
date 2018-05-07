from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout, QDesktopWidget, QWidget, QGridLayout
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction

from pytoshop.controllers.main_c import MainController
from pytoshop.views.drawing_board_v import DrawingBoard
from pytoshop.views.layers_v import Layers
from pytoshop.views.menu_bar_v import MenuBar
from pytoshop.views.tool_bar_v import ToolBar


class MainView(QWidget):

    def __init__(self):
        super().__init__()
        self.controller = MainController(self)

        self.setWindowTitle('Pytoshop')
        self.initGeometry(650, 400)

        self.menuBar = MenuBar(self)

        self.toolbar = ToolBar(self, 'pytoshop/views/images/')
        self.drawing_board = DrawingBoard(self, 500, 500)
        self.layers = Layers(self.drawing_board.controller.image)

        layout = QGridLayout()
        layout.addWidget(self.toolbar, 1, 1, 8, 1)  # addWidget(row, col, rowspan == height, colspan == width)
        invisible = QWidget()
        invisible.hide()
        layout.addWidget(invisible, 1, 2, 8, 8)
        layout.addWidget(self.layers, 1, 10, 8, 1)

        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)

    def initGeometry(self, width, height):
        # Set size
        self.setGeometry(0, 0, width, height)

        # Center window
        frame = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(center_point)
        self.move(frame.topLeft())

    # EVENTS #

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Control:
            self.controller.onControlKeyPressed()

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Control:
            self.controller.onControlKeyReleased()

    def mousePressEvent(self, event):
        self.controller.onMousePressed(event)

    def mouseReleaseEvent(self, event):
        self.controller.onMouseReleased()

    def mouseMoveEvent(self, event):
        self.controller.onMouseMove(event)

    def wheelEvent(self, event):
        self.controller.onWheel(event)

    # FUNCTIONS #

    def hideCursor(self):
        QApplication.setOverrideCursor(Qt.BlankCursor)

    def showOpenHandCursor(self):
        QApplication.setOverrideCursor(Qt.OpenHandCursor)

    def showClosedHandCursor(self):
        QApplication.setOverrideCursor(Qt.ClosedHandCursor)

    def showArrowCursor(self):
        QApplication.setOverrideCursor(Qt.ArrowCursor)
