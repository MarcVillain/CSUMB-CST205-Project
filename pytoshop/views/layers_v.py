import cv2
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QListWidget, QHBoxLayout, QLabel, QListWidgetItem, QWidget, QListView

from pytoshop.utils.color_u import rgb_to_rgba


class LayersItem(QWidget):

    def __init__(self, layer):
        super().__init__()
        self.layer = layer

        layout = QHBoxLayout()

        self.pixmap = QLabel()
        layout.addWidget(self.pixmap)
        layout.addWidget(QLabel('Layer 0'))

        self.refresh()

        self.setLayout(layout)

    def refresh(self):
        rgba = cv2.resize(rgb_to_rgba(self.layer.rgb, self.layer.alpha), (40, 40), cv2.INTER_AREA)
        image = QImage(rgba, 40, 40, 4*40, QImage.Format_RGBA8888)
        pixmap = QPixmap(image)
        self.pixmap.setPixmap(pixmap)

class Layers(QListWidget):

    def __init__(self, image):
        super().__init__()

        self.layers = []

        for layer in image.layers:
            qCustomWidget = LayersItem(layer)
            qListWidgetItem = QListWidgetItem(self)
            qListWidgetItem.setSizeHint(qCustomWidget.sizeHint())
            self.addItem(qListWidgetItem)
            self.setItemWidget(qListWidgetItem, qCustomWidget)
            self.layers.append(qCustomWidget)

        self.setFixedWidth(200)

    def refresh(self, i):
        self.layers[i].refresh()
