import cv2
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QListWidget, QHBoxLayout, QLabel, QListWidgetItem, QWidget, QListView


class LayersItem(QWidget):

    def __init__(self, layer):
        super().__init__()

        layout = QHBoxLayout()

        pixmap = QLabel()
        pixmap.setPixmap(QPixmap(QImage(cv2.resize(layer.values, (80, 10), cv2.INTER_AREA), 80, 10, 4, QImage.Format_RGBA8888)))
        layout.addWidget(pixmap)
        layout.addWidget(QLabel('Layer 0'))
        self.setLayout(layout)


class Layers(QListWidget):

    def __init__(self, image):
        super().__init__()

        for layer in image.layers:
            qCustomWidget = LayersItem(layer)
            qListWidgetItem = QListWidgetItem(self)
            qListWidgetItem.setSizeHint(qCustomWidget.sizeHint())
            self.addItem(qListWidgetItem)
            self.setItemWidget(qListWidgetItem, qCustomWidget)

        self.setFixedSize(200, 400)
