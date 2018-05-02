from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout, QDesktopWidget
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction

from pytoshop.controllers.main_c import MainController
from pytoshop.views.drawing_board_v import DrawingBoard


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
