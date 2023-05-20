from PyQt6.QtWidgets import QMainWindow
from MyWidget import MyWidget


class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setCentralWidget(MyWidget(self))