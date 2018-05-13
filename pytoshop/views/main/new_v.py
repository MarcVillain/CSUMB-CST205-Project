from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QDesktopWidget

from pytoshop.widgets.color_frame_w import ColorFrameWidget


class NewView(QWidget):

    def __init__(self, app):
        super().__init__()
        self.app = app

        layout = QVBoxLayout()
        onlyInt = QIntValidator()

        title = QLabel('<center><h1>New Canvas</h1></center>')
        title.setContentsMargins(0, 0, 0, 15)
        layout.addWidget(title)

        widthLayout = QHBoxLayout()
        widthLayout.addWidget(QLabel('Width: '))
        self.width_input = QLineEdit()
        self.width_input.setValidator(onlyInt)
        widthLayout.addWidget(self.width_input)
        layout.addLayout(widthLayout)

        heightLayout = QHBoxLayout()
        heightLayout.addWidget(QLabel('Height: '))
        self.height_input = QLineEdit()
        self.height_input.setValidator(onlyInt)
        heightLayout.addWidget(self.height_input)
        layout.addLayout(heightLayout)

        colorLayout = QHBoxLayout()
        colorLayout.addWidget(QLabel('Color: '))
        self.color_input = ColorFrameWidget(None, (255, 255, 255, 255))
        colorLayout.addWidget(self.color_input)
        layout.addLayout(colorLayout)

        create = QPushButton('Create')
        create.setContentsMargins(10, 10, 10, 10)
        create.clicked.connect(self.onClickCreate)
        layout.addWidget(create)

        self.setLayout(layout)

        self.initGeometry(250, 200)

    def initGeometry(self, width, height):
        # Set size
        self.setGeometry(0, 0, width, height)

        # Center window
        frame = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(center_point)
        self.move(frame.topLeft())

    def onClickCreate(self):
        width = 500 if self.width_input.text() == '' else self.width_input.text()
        height = 500 if self.height_input.text() == '' else self.height_input.text()

        self.app.start(int(width), int(height), self.color_input.color)
