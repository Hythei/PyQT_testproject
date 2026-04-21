import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt6.QtCore import QSize, Qt

def button_clicked():
    print("button clicked")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Application1")

        button = QPushButton("Click the Button!")
        button.setFixedSize(QSize(100, 100))
        button.clicked.connect(button_clicked)

        self.setFixedSize(QSize(400, 300))
        self.setMaximumSize(QSize(800, 600))
        self.setMinimumSize(QSize(200, 150))
        self.setCentralWidget(button)

app = QApplication(sys.argv)


window = MainWindow()
window.show()

app.exec()

