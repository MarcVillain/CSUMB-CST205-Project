import os
from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton, QWidget, QVBoxLayout


class ToolBarView(QWidget):

    def __init__(self, parent, icon_directory, tools):
        super().__init__()

        self.parent = parent
        self.tools = tools
        self.setFixedWidth(40)
        self.buttons = {}

        layout = QVBoxLayout()

        for filename in os.listdir(icon_directory):
            name = filename.split(".")[0]
            button = QPushButton(QIcon(icon_directory + filename), '', parent)
            button.setCheckable(True)
            button.setObjectName(name)
            button.clicked.connect(partial(self.pressButton, name))
            self.buttons[name] = button
            layout.addWidget(button)

        self.buttons['paint'].setChecked(True)
        self.currentButton = self.buttons['paint']

        layout.addStretch()
        self.setLayout(layout)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.darkGray)
        self.setPalette(p)

    # 1. set the current tool to the currently pressed tool
    # 2. unchecks the previous tool
    def pressButton(self, name):
        self.currentButton.setChecked(False)
        self.parent.drawing_board.controller.tool = self.tools[name]
        self.parent.topBar.changeTopBar(name)
        self.currentButton = self.buttons[name]
        self.currentButton.setChecked(True)
        #print(self.currentButton.objectName())
