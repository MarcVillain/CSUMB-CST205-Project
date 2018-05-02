import os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QBoxLayout, QPushButton


class ToolBar(QBoxLayout):
    ICON_DIRECTORY = 'pytoshop/views/images/'
    buttons = []

    def __init__(self, QBoxLayout_Direction, QWidget, QRect):
        super().__init__(QBoxLayout_Direction)
        self.setGeometry(QRect)
        for filename in os.listdir(self.ICON_DIRECTORY):
            button = QPushButton(QIcon(self.ICON_DIRECTORY + filename), filename.split(".")[0], QWidget)
            self.buttons.append(button)
            self.addWidget(button, 0)
        self.addStretch()
