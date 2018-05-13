from functools import partial

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMenuBar, QAction
from pytoshop.utils.filters_u import FiltersUtil


class MenuBarView(QMenuBar):

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        menuItems = {
            'File': {
                'New': {'icon': 'new.png', 'trigger': self.doNothing},
                'Import': {'icon': 'open.png', 'trigger': parent.loadImage},
                'Save': {'icon': 'save.png', 'trigger': parent.saveImage},
                'Export': {'icon': 'export.png', 'trigger': self.doNothing},
                'Exit': {'icon': 'exit.png', 'trigger': parent.close}
            },
            'Edit': {
                'Filters': {
                    'Grayscale': {'trigger': self.grayScaleFilter},
                    'Cool': {'trigger': self.cool},
                    'Warm': {'trigger': self.warm},
                    'Sepia': {'trigger': self.sepia},
                    'Reduce Noise': {'trigger': self.reduceNoise},
                    'Blur': {'trigger': self.blur},
                    'Negative': {'trigger': self.negative}
                }
            },
            'Layer': {
                'Add New Layer': {'trigger': self.doNothing},
                'Remove Layer': {'trigger': self.doNothing}
            }
        }

        self.addMenuItems(self, menuItems)

    def addMenuItems(self, menuBar, menuItems):
        for title, subItems in menuItems.items():
            menu = menuBar.addMenu(title)

            for key, value in subItems.items():
                try:
                    action = QAction(QIcon('pytoshop/views/images/' + value['icon']), '&' + key, menu)
                except:
                    action = QAction('&' + key, menu)

                try:
                    action.triggered.connect(value['trigger'])
                    menu.addAction(action)
                except:
                    self.addMenuItems(menu, subItems)

    def doNothing(self):
        print("Do Nothing")

    def grayScaleFilter(self):
        self.parent.drawing_board.controller.image.current_layer.applyFilter(FiltersUtil.grayScaleFilter)

    def cool(self):
        self.parent.drawing_board.controller.image.current_layer.applyFilter(FiltersUtil.coolFilter)

    def warm(self):
        self.parent.drawing_board.controller.image.current_layer.applyFilter(FiltersUtil.warmFilter)

    def sepia(self):
        self.parent.drawing_board.controller.image.current_layer.applyFilter(FiltersUtil.sepiaFilter)

    def reduceNoise(self):
        self.parent.drawing_board.controller.image.current_layer.applyFilter(FiltersUtil.reduceNoise)

    def blur(self):
        self.parent.drawing_board.controller.image.current_layer.applyFilter(FiltersUtil.blur)

    def negative(self):
        self.parent.drawing_board.controller.image.current_layer.applyFilter(FiltersUtil.negativeFilter)