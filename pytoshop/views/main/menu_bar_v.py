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
                'Load': {'icon': 'open.png', 'trigger': parent.loadImage},
                'Save': {'icon': 'save.png', 'trigger': parent.saveImage},
                'Exit': {'icon': 'exit.png', 'trigger': parent.close}
            },
            'Edit': {
                'Filters': {
                    'Grayscale': {'trigger': partial(self.applyFilter, FiltersUtil.grayScale)},
                    'Cool': {'trigger': partial(self.applyFilter, FiltersUtil.cool)},
                    'Warm': {'trigger': partial(self.applyFilter, FiltersUtil.warm)},
                    'Sepia': {'trigger': partial(self.applyFilter, FiltersUtil.sepia)},
                    'Reduce Noise': {'trigger': partial(self.applyFilter, FiltersUtil.reduceNoise)},
                    'Blur': {'trigger': partial(self.applyFilter, FiltersUtil.blur)},
                    'Negative': {'trigger': partial(self.applyFilter, FiltersUtil.negative)}
                }
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

    def applyFilter(self, filter):
        self.parent.drawing_board.controller.image.current_layer.applyFilter(filter)
        self.parent.drawing_board.refresh()
        self.parent.layers.refresh()
