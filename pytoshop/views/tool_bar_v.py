import os
from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QBoxLayout, QPushButton, QHBoxLayout, QWidget, QVBoxLayout, QSlider


class ToolBarView(QWidget):

    def __init__(self, parent, icon_directory):
        super().__init__()
        layout = QVBoxLayout()
        self.setFixedWidth(40)

        self.buttons = []

        i = 0
        for filename in os.listdir(icon_directory):
            button = QPushButton(QIcon(icon_directory + filename), '', parent)
            button.setCheckable(True)
            button.clicked.connect(partial(self.pressButton, i))
            self.buttons.append(button)
            layout.addWidget(button)
            i += 1

        self.buttons[0].setChecked(True)

        layout.addStretch()
        self.setLayout(layout)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.gray)
        self.setPalette(p)

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