import sys  
from PyQt5.QtWidgets import QApplication
from pytoshop.views.main_v import MenuBar

def start():
    app = QApplication(sys.argv)

    main = MenuBar()
    main.show()

    sys.exit(app.exec_())
