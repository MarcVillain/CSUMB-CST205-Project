import cv2
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QListWidget, QHBoxLayout, QLabel, QListWidgetItem, QWidget, QAbstractItemView, QComboBox, \
    QVBoxLayout, QPushButton

from pytoshop.utils.blend_u import *
from pytoshop.utils.color_u import rgb_to_rgba


class LayersItem(QWidget):

    def __init__(self, layer):
        super().__init__()
        self.layer = layer

        layout = QHBoxLayout()

        self.pixmap = QLabel()
        layout.addWidget(self.pixmap)
        layout.addWidget(QLabel('Layer ' + str(layer.pos)))

        self.refresh()
        layout.addStretch()
        self.setLayout(layout)

        self.setStyleSheet('border: none;')

    def refresh(self):
        height, width = self.layer.rgb.shape[:2]

        max_size = 40

        new_width = max_size
        new_height = height * new_width // width

        if height > max_size:
            new_height = max_size
            new_width = width * new_height // height

        new_rgb, new_alpha = blend(self.layer.rgb, self.layer.alpha, self.layer.image.bottom_layer.rgb, self.layer.image.bottom_layer.alpha)
        rgba = cv2.resize(rgb_to_rgba(new_rgb, new_alpha), (new_width, new_height), cv2.INTER_AREA)
        image = QImage(rgba, new_width, new_height, 4*new_width, QImage.Format_RGBA8888)
        pixmap = QPixmap(image)
        self.pixmap.setPixmap(pixmap)


class LayersView(QWidget):

    def __init__(self, parent, image):
        super().__init__()

        self.parent = parent
        self.image = image

        self.layers = []
        layout = QVBoxLayout()

        # --- Blending Modes --- #
        self.blend_modes = {
            'Normal': normal,
            'Multiply': multiply,
            'Screen': screen,
            # 'Darken': darken,
            # 'Lighten': lighten,
            # 'Color Dodge': color_dodge,
            # 'Color Burn': color_burn,
            # 'Hard Light': hard_light,
            # 'Soft Light': soft_light,
            'Difference': difference
        }

        self.blend_list = QComboBox()
        for blend_mode in self.blend_modes:
            name = str(blend_mode).replace('_', ' ')
            self.blend_list.addItem(name[0].upper() + name[1:])

        self.blend_list.currentIndexChanged.connect(self.onChangeBlendMode)

        layout.addWidget(self.blend_list)

        # --- Layers list --- #
        self.layers = []
        self.list = QListWidget()

        layer = image.top_layer.bottom_layer
        while layer is not None and layer.pos != -1:
            item = LayersItem(layer)
            list_item = QListWidgetItem()
            list_item.setSizeHint(item.sizeHint())

            self.list.addItem(list_item)
            self.list.setItemWidget(list_item, item)
            self.layers.insert(0, item)

            layer = layer.bottom_layer

        self.setFixedWidth(150)
        self.list.setCurrentRow(0)
        self.list.setDragEnabled(False)
        self.list.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.list.setSelectionMode(QAbstractItemView.SingleSelection)

        layout.addWidget(self.list)

        # --- Add and Remove buttons --- #
        buttons = QHBoxLayout()

        self.add = QPushButton('+')
        self.remove = QPushButton('-')

        self.add.clicked.connect(self.onClickAdd)
        self.remove.clicked.connect(self.onClickRemove)

        buttons.addWidget(self.add)
        buttons.addWidget(self.remove)

        buttons.setContentsMargins(0, 0, 0, 0)

        layout.addLayout(buttons)

        # --- Styling --- #
        self.list.setStyleSheet('selection-background-color: #cbcbcb; border: none;')
        layout.setContentsMargins(0, 0, 0, 0)
        self.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        self.list.itemClicked.connect(self.onClickItem)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.darkGray)
        self.setPalette(p)

    def onClickItem(self, item):
        self.image.current_layer = self.layers[self.list.row(item)].layer
        self.blend_list.setCurrentIndex(list(self.blend_modes.values()).index(self.image.current_layer.blend_mode))

    def onClickAdd(self):
        self.image.addLayer(self.parent)
        self.parent.drawing_board.refresh()

    def onClickRemove(self):
        self.image.removeLayer(self.parent)
        self.parent.drawing_board.refresh()

    def addLayer(self, layer):
        item = LayersItem(layer)
        list_item = QListWidgetItem()
        list_item.setSizeHint(item.sizeHint())
        list_item.pos = layer.pos

        new_pos = len(self.layers) - layer.pos

        self.list.insertItem(new_pos, list_item)
        self.list.setItemWidget(list_item, item)
        self.layers.insert(new_pos, item)

        self.list.setCurrentRow(new_pos)
        self.image.current_layer = layer

    def removeLayer(self, layer):
        new_pos = len(self.layers) - layer.pos - 1

        self.list.takeItem(new_pos)
        self.layers.pop(new_pos)

    def refresh(self):
        self.layers[self.list.currentRow()].refresh()

    def onChangeBlendMode(self):
        # Change blend mode
        pos = self.blend_list.currentIndex()
        self.image.current_layer.blend_mode = list(self.blend_modes.values())[pos]

        # Update rgba display
        self.image.current_layer.updateDisplay(0, self.image.height, 0, self.image.width)

        # Refresh drawing board
        self.parent.drawing_board.refresh()
