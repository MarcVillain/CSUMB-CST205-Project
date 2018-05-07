from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMenuBar, QAction


class MenuBarView(QMenuBar):

    def __init__(self, parent):
        super().__init__()

        menuItems = {
            'File': {
                'New': {'icon': 'new.png', 'trigger': self.doNothing},
                'Open': {'icon': 'open.png', 'trigger': self.doNothing},
                'Save': {'icon': 'save.png', 'trigger': self.doNothing},
                'Save As': {'icon': 'saveAs.png', 'trigger': self.doNothing},
                'Export': {'icon': 'export.png', 'trigger': self.doNothing},
                'Exit': {'icon': 'exit.png', 'trigger': parent.close}
            },
            'Layer': {
                'Filters': {
                    'Grayscale': {'trigger': self.doNothing},
                    'Sepia': {'trigger': self.doNothing},
                    'Negative': {'trigger': self.doNothing}
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
        print('Do nothing')
        pass