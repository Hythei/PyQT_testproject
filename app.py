import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QTextEdit, QMenu


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.show()

        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)


    def on_context_menu(self, pos):
        context = QMenu(self)
        action1 = QAction("test 1", self)
        action2 = QAction("test 2", self)
        action3 = QAction("test 3", self)

        action1.triggered.connect(lambda: print("test 1 chosen"))
        action2.triggered.connect(lambda: print("test 2 chosen"))
        action3.triggered.connect(lambda: print("test 3 chosen"))

        context.addAction(action1)
        context.addAction(action2)
        context.addAction(action3)

        context.exec(self.mapToGlobal(pos))

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()