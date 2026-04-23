import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QTextEdit


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.label = QLabel("Click within this window")
        self.label.setMouseTracking(True)
        self.setCentralWidget(self.label)
        self.setWindowTitle("My App")



    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("LEFT HAS BEEN CLICKED")
        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("RIGHT HAS BEEN CLICKED")
        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("MIDDLE HAS BEEN CLICKED")

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseReleaseEvent LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseReleaseEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseReleaseEvent RIGHT")

    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseDoubleClickEvent LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseDoubleClickEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseDoubleClickEvent RIGHT")


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()