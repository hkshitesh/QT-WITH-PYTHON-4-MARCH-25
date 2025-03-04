from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Signals and Slots")
        self.resize(400, 300)
        self.layout = QVBoxLayout()
        self.label = QLabel("Press the button")
        self.button = QPushButton("Click Me")
        self.button.clicked.connect(self.change_text)  # Connect event

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def change_text(self):
        self.label.setText("Button Clicked!")

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())