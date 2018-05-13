from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QFrame, QColorDialog


class ColorFrameWidget(QFrame):

    def __init__(self, tool=None, color=(0, 0, 0, 255)):
        super(ColorFrameWidget, self).__init__()
        self.tool = tool

        self.color = color

        self.setFixedHeight(20)
        self.setFixedWidth(20)
        self.setFrameStyle(1)

        if tool is not None:
            self.setStyleSheet('QWidget { background-color: rgb%s }' % (self.tool.color,))
        else:
            self.setStyleSheet('QWidget { background-color: rgb%s }' % (self.color,))

    def mousePressEvent(self, e):
        if e.buttons() == Qt.LeftButton:
            if self.tool is not None:
                old_color = QColor(self.tool.color[0], self.tool.color[1], self.tool.color[2], 255)
            else:
                old_color = QColor(self.color[0], self.color[1], self.color[2], self.color[3])

            new_color = QColorDialog.getColor(old_color, self)

            if new_color.isValid():
                self.color = (new_color.red(), new_color.green(), new_color.blue(), new_color.alpha())

                if self.tool is not None:
                    self.tool.color = self.color
                    self.setStyleSheet('QWidget { background-color: rgb%s }' % (self.tool.color,))
                else:
                    self.setStyleSheet('QWidget { background-color: rgb%s }' % (self.color,))
