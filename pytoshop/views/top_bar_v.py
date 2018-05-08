import os
from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QBoxLayout, QPushButton, QHBoxLayout, QWidget, QVBoxLayout


class TopBarView(QWidget):

    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.setFixedHeight(40)

        layout.addStretch()
        self.setLayout(layout)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.darkGray)
        self.setPalette(p)

