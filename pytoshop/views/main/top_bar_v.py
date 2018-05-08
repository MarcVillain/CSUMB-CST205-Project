from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QWidget


class TopBarView(QWidget):

    def __init__(self, tools):
        super().__init__()

        self.top_bars = []
        for tool in tools:
            self.top_bars.append(tool.top_bar)

        layout = QHBoxLayout()
        self.setFixedHeight(40)
        layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(self.top_bars[0])

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.darkGray)
        self.setPalette(p)

        self.setStyleSheet('color: white;')

        layout.addStretch()
        self.setLayout(layout)

