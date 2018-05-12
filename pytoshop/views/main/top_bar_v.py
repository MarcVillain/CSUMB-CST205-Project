from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QWidget


class TopBarView(QWidget):

    def __init__(self, tools):
        super().__init__()

        self.top_bars = {}
        for key in tools:
            self.top_bars[key] = tools[key].top_bar

        self.layout = QHBoxLayout()
        self.setFixedHeight(40)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.currentBar = self.top_bars["brush"]
        if self.currentBar is not None:
            self.layout.addWidget(self.currentBar)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.darkGray)
        self.setPalette(p)

        self.setStyleSheet('color: white;')

        self.layout.addStretch()
        self.setLayout(self.layout)

    # changes the top bar to the corresponding bar (of the clicked tool)
    def changeTopBar(self, name):
        print("cleaning the widget")
        self.currentBar.setParent(None)
        self.currentBar = self.top_bars[name]
        self.layout.addWidget(self.currentBar)
        self.setLayout(self.layout)


