from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QFrame, QColorDialog


class ColorFrameWidget(QFrame):

    def __init__(self, tool):
        super(ColorFrameWidget, self).__init__()
        self.tool = tool

        self.setFixedHeight(20)
        self.setFixedWidth(20)
        self.setFrameStyle(1)
        self.setStyleSheet('QWidget { background-color: rgb%s }' % (self.tool.color,))

    def mousePressEvent(self, e):
        if e.buttons() == Qt.LeftButton:
            old_color = QColor(self.tool.color[0], self.tool.color[1], self.tool.color[2], 255)
            new_color = QColorDialog.getColor(old_color, self)

            if new_color.isValid():
                self.tool.color = (new_color.red(), new_color.green(), new_color.blue(), new_color.alpha())
                self.setStyleSheet('QWidget { background-color: rgb%s }' % (self.tool.color,))
