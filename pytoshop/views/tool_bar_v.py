import os
from functools import partial

from PyQt5 import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QBoxLayout, QPushButton


class ToolBar(QBoxLayout):
    ICON_DIRECTORY = 'pytoshop/views/images/'

    def __init__(self, QBoxLayout_Direction, QWidget, QRect):
        super().__init__(QBoxLayout_Direction)
        self.setGeometry(QRect)

        self.buttons = []

        i = 0
        for filename in os.listdir(self.ICON_DIRECTORY):
            button = QPushButton(QIcon(self.ICON_DIRECTORY + filename), '', QWidget)
            button.setCheckable(True)
            button.clicked.connect(partial(self.pressButton, i))
            self.buttons.append(button)
            self.addWidget(button, 0)
            i += 1
        self.buttons[0].setChecked(True)
        self.addStretch()

    def pressButton(self, pos):
        i = 0
        while i < pos:
            self.buttons[i].setChecked(False)
            i += 1
        self.buttons[i].setChecked(True)
        i += 1
        while i < len(self.buttons):
            self.buttons[i].setChecked(False)
            i += 1
