import sys
sys.path.append('..')

from pytoshop.controllers.main_c import MainController,DrawingBoardController
from pytoshop.objects.brush_o import Brush

from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel, QMenu, QAction
from PyQt5.QtGui import QImage,QPixmap,QPainter
from PyQt5.QtCore import Qt


from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QMenuBar, QToolBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot



# Create GUI Menu Bar
class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.menubar()

    def menubar(self):
        menubar = self.menubar()
        filemenu = menubar.addMenu('File')

        importMenu = QMenu('Import', self)
        importApplication = QAction('Import mail', self)
        importMenu.addAction(importApplication)

        newAct = QAction('New', self)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(importMenu)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()


class DrawingBoard(QLabel):

    def __init__(self, parent, width, height, image_name=None):
        super().__init__(parent)
        self.controller = DrawingBoardController(parent.controller, self)
        self.controller.createImage(500, 500)
        self.brush = Brush()

    def displayImage(self, image):
        image = QImage(image.value, image.width, image.height, image.bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap(image)
        self.setPixmap(pixmap)

    def mousePressEvent(self, event):
        self.controller.onMousePressed(event)

    def mouseMoveEvent(self, event):
        self.controller.onMouseMove(event)

class MainView(QWidget):

    def __init__(self):
        super().__init__()

        self.controller = MainController(self)
        self.drawing_board = DrawingBoard(self, 500, 500)

        self.setGeometry(0, 0, 600, 600)

class MenuBar(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Pytoshop'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        self.menu()
        # self.toolBar()

    def menu(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        mainMenu = self.menuBar()
        mainMenu.setNativeMenuBar(False)
        fileMenu = mainMenu.addMenu('File')
        filterMenu = mainMenu.addMenu('Filters')

        #TOOLBAR CODE
        toolBar = self.menuBar()
        toolBar.setNativeMenuBar(False)
        toolMenu = toolBar.addMenu('ToolBar')

        brush = QAction(QIcon('pytoshop/views/images/brush.png'), ' &Brush', self)
        toolMenu.addAction(brush)

        select = QAction(QIcon('pytoshop/views/images/select.png'), ' &Select', self)
        toolMenu.addAction(select)

        erase = QAction(QIcon('pytoshop/views/images/erase.png'), ' &Erase', self)
        toolMenu.addAction(erase)

        color = QAction(QIcon('pytoshop/views/images/color.png'), ' &Color Picker', self)
        toolMenu.addAction(color)

        text = QAction(QIcon('pytoshop/views/images/text1.png'), ' &Text', self)
        toolMenu.addAction(text)

        zoom = QAction(QIcon('pytoshop/views/images/zoom.png'), ' &Magnifier', self)
        toolMenu.addAction(zoom)

        #FILTER CODE
        grayscale = QAction(' &Grayscale', self)
        filterMenu.addAction(grayscale)

        sepia = QAction(' &Sepia', self)
        filterMenu.addAction(sepia)

        negative = QAction(' &Negative', self)
        filterMenu.addAction(negative)

        # MENUBAR CODE
        #New
        newButton = QAction(QIcon('pytoshop/views/images/new.png'), '&New', self)
        # newButton.triggered.connect(self.new)
        fileMenu.addAction(newButton)
        #Open
        openButton = QAction(QIcon('pytoshop/views/images/open.png'), '&Open', self)
        fileMenu.addAction(openButton)
        #Save
        saveButton = QAction(QIcon('pytoshop/views/images/save.png'), ' &Save', self)
        fileMenu.addAction(saveButton)
        #Save As
        saveAsButton = QAction(QIcon('pytoshop/views/images/saveAs.png'), ' &Save As', self)
        fileMenu.addAction(saveAsButton)
        #Print
        printButton = QAction(QIcon('pytoshop/views/images/print.png'), ' &Print', self)
        fileMenu.addAction(printButton)
        #Exit
        exitButton = QAction(QIcon('pytoshop/views/images/exit.png'), ' &Exit', self)
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

        self.show()

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
