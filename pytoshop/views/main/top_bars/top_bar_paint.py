from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel

from pytoshop.widgets.color_frame_w import ColorFrameWidget
from pytoshop.widgets.slider_widget_w import SliderWidget


class TopBarPaint(QWidget):

    def __init__(self, tool):
        super().__init__()
        self.tool = tool

        layout = QHBoxLayout()

        layout.addWidget(QLabel('Color: '))
        layout.addWidget(ColorFrameWidget(self.tool))

        layout.addWidget(QLabel('Size: '))
        self.size_slider = SliderWidget(2, 200, self.tool.size)
        self.size_slider.valueChanged.connect(self.onSizeChanged)
        layout.addWidget(self.size_slider)

        layout.addWidget(QLabel('Hardness: '))
        self.hardness_slider = SliderWidget(2, 100, self.tool.hardness)
        self.hardness_slider.valueChanged.connect(self.onHardnessChanged)
        layout.addWidget(self.hardness_slider)

        layout.addWidget(QLabel('Opacity: '))
        self.opacity_slider = SliderWidget(0, 100, self.tool.opacity)
        self.opacity_slider.valueChanged.connect(self.onOpacityChanged)
        layout.addWidget(self.opacity_slider)

        layout.addStretch()
        self.setLayout(layout)

    def onSizeChanged(self):
        self.tool.size = self.size_slider.value()

    def onHardnessChanged(self):
        self.tool.hardness = self.hardness_slider.value()

    def onOpacityChanged(self):
        self.tool.opacity = self.opacity_slider.value()