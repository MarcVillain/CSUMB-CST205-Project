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
        self.setGeometry(self.LEFT_X, self.LEFT_Y, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        main = QHBoxLayout()

        self.menuBar = QMenuBar()
        self.initMenuBar()
        # get toolbar
        self.toolbar = ToolBar(QBoxLayout.TopToBottom, self, QRect(0, 0, 50, 50))
        # get drawing canvas
        self.canvas = QHBoxLayout()
        self.controller = MainController(self)
        self.drawing_board = DrawingBoard(self, 950, 700)
        self.canvas.addWidget(self.drawing_board)
        self.canvas.addWidget(Layers(self.drawing_board.controller.image))
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
                    action.triggered.connect(value['trigger'])
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
