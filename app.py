import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

from random import choice
window_titles = ["App1", "App2", "App3", "App4", "App5", "App6", "App7", "App8", "App9", "Something is very, very bad"]

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        self.button = QPushButton("Click me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Clicked!")
        new_window_title = choice(window_titles)
        print(f"Changing window title to {new_window_title}")
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        print(f"Window title changed to {window_title}")

        if window_title == "Something is very, very bad":
            self.button.setDisabled(True)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()