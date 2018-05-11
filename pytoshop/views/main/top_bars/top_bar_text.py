from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import pyqtSlot

from pytoshop.widgets.color_frame_w import ColorFrameWidget
from pytoshop.widgets.slider_widget_w import SliderWidget


class TopBarText(QWidget):

    def __init__(self, tool):
        super().__init__()
        self.tool = tool

        layout = QHBoxLayout()

        layout.addWidget(QLabel('Color: '))
        layout.addWidget(ColorFrameWidget(self.tool))

        layout.addWidget(QLabel('Size: '))
        self.size_slider = SliderWidget(1, 5, self.tool.fontScale)
        self.size_slider.valueChanged.connect(self.onSizeChanged)
        layout.addWidget(self.size_slider)

        layout.addWidget(QLabel('Text: '))
        self.textbox = QLineEdit(self)
        layout.addWidget(self.textbox)

        self.button = QPushButton('Set Text', self)
        self.button.clicked.connect(self.on_click)
        layout.addWidget(self.button)


        layout.addStretch()
        self.setLayout(layout)

    def onSizeChanged(self):
        self.tool.fontScale = self.size_slider.value()

    @pyqtSlot()
    def on_click(self):
        self.tool.text = self.textbox.text()
