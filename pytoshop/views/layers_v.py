import cv2
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QListWidget, QHBoxLayout, QLabel, QListWidgetItem, QWidget, QListView, QFrame, \
    QAbstractItemView

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
        layout.addStretch()

        self.setLayout(layout)

    def refresh(self):
        height, width = self.layer.rgb.shape[:2]

        max_size = 40

        new_width = max_size
        new_height = height * new_width // width

        if height > max_size:
            new_height = max_size
            new_width = width * new_height // height

        rgba = cv2.resize(rgb_to_rgba(self.layer.rgb, self.layer.alpha), (new_width, new_height), cv2.INTER_AREA)
        image = QImage(rgba, new_width, new_height, 4*new_width, QImage.Format_RGBA8888)
        pixmap = QPixmap(image)
        self.pixmap.setPixmap(pixmap)


class LayersView(QListWidget):

    def __init__(self, image):
        super().__init__()

        self.layers = []

        for layer in image.layers:
            item = LayersItem(layer)
            list_item = QListWidgetItem(self)
            list_item.setSizeHint(item.sizeHint())
            self.addItem(list_item)
            self.setItemWidget(list_item, item)
            self.layers.append(item)

        self.setFixedWidth(150)
        self.setCurrentRow(0)
        self.setSelectionMode(QAbstractItemView.SingleSelection)

    def refresh(self, i):
        self.layers[i].refresh()
