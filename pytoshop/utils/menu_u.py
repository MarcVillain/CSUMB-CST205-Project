from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction


class MenuHelper:

    @staticmethod
    def createFrom(menu, dict):
        for key,value in dict:
            action = QAction(QIcon('pytoshop/views/images/' + value['icon']), '&' + key, menu)
            menu.addAction(action)
