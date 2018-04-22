import sys
from PyQt5.QtWidgets import QApplication
from pytoshop.views.main_v import MainView


def start():
    app = QApplication(sys.argv)

    main = MainView()
    main.show()

    sys.exit(app.exec_())
