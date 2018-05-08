from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSlider


class SliderWidget(QSlider):

    def __init__(self, min=2, max=100, value=2, step=1):
        super().__init__(Qt.Horizontal)

        self.setMinimum(min)
        self.setMaximum(max)
        self.setValue(value)
        self.setTickInterval(step)

        self.setFixedWidth(100)
