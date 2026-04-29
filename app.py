import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QComboBox, QMainWindow, QListWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Application")

        widget = QListWidget()
        widget.addItems(["Item 1", "Item 2", "Item 3"])

        widget.currentItemChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def index_changed(self, i):
        print(i.text())

    def text_changed(self, s):
        print(s)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())