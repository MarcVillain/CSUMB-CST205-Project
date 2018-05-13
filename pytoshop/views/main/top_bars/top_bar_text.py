from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import pyqtSlot

from pytoshop.widgets.color_frame_w import ColorFrameWidget
from pytoshop.widgets.slider_widget_w import SliderWidget


class TopBarText(QWidget):

    def __init__(self, textTool):
        super().__init__()
        self.textTool = textTool

        layout = QHBoxLayout()

        layout.addWidget(QLabel('Color: '))
        layout.addWidget(ColorFrameWidget(self.textTool))

        layout.addWidget(QLabel('Size: '))
        self.size_slider = SliderWidget(1, 40, self.textTool.fontScale)
        self.size_slider.valueChanged.connect(self.onSizeChanged)
        layout.addWidget(self.size_slider)

        layout.addWidget(QLabel('Thickness: '))
        self.thickness_slider = SliderWidget(1, 40, self.textTool.fontScale)
        self.thickness_slider.valueChanged.connect(self.onThicknessChanged)
        layout.addWidget(self.thickness_slider)

        layout.addWidget(QLabel('Text: '))
        self.textbox = QLineEdit(self)
        layout.addWidget(self.textbox)

        self.button = QPushButton('Set Text', self)
        self.button.clicked.connect(self.on_click)
        layout.addWidget(self.button)


        layout.addStretch()
        self.setLayout(layout)

    def onSizeChanged(self):
        self.textTool.fontScale = self.size_slider.value()

    def onThicknessChanged(self):
        self.textTool.thickness = self.thickness_slider.value()

    @pyqtSlot()
    def on_click(self):
        self.textTool.text = self.textbox.text()
