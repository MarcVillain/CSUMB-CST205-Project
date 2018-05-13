import sys

from PyQt5.QtWidgets import QApplication

from pytoshop.views.main.new_v import NewView
from pytoshop.views.main_v import MainView


class Pytoshop(QApplication):

    def __init__(self):
        super().__init__(sys.argv)
        self.current = None

    def start(self, width, height, color):
        main = MainView(self, width, height, color)
        main.setWindowTitle("Pytoshop")

        if self.current is None:
            new.show()
            self.current = main
            sys.exit(self.exec_())
        else:
            self.current.hide()
            main.show()
            self.current = main

        main.show()
        self.current = main

    def new(self):
        new = NewView(self)
        new.setWindowTitle("Pytoshop")

        if self.current is None:
            new.show()
            self.current = new
            sys.exit(self.exec_())
        else:
            self.current.hide()
            new.show()
            self.current = new
