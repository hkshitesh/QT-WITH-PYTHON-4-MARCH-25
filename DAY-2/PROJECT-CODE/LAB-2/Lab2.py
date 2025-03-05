import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox
from PySide6.QtCore import Qt

class CustomWidgetsApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Customizing Widgets - PySide6")
        self.setGeometry(300, 300, 400, 250)

        # Layout
        self.layout = QVBoxLayout()

        # QLabel - Display Message
        self.label = QLabel("Enter your name:")
        self.label.setStyleSheet("font-size: 16px; font-weight: bold;")

        # QLineEdit - Text Input
        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Type your name here...")
        self.text_input.setStyleSheet("padding: 5px; font-size: 14px;")
        self.text_input.textChanged.connect(self.update_label)

        # QComboBox - Selection Menu
        self.combo = QComboBox()
        self.combo.addItems(["Select Category", "Student", "Developer", "Designer"])
        self.combo.setStyleSheet("padding: 5px; font-size: 14px;")
        self.combo.currentIndexChanged.connect(self.update_label)

        # QPushButton - Clickable Button
        self.button = QPushButton("Submit")
        self.button.setStyleSheet(
            "background-color: #4CAF50; color: white; padding: 8px; font-size: 14px; border-radius: 5px;"
        )
        self.button.clicked.connect(self.display_message)

        # QLabel - Output Message
        self.result_label = QLabel("")
        self.result_label.setStyleSheet("font-size: 16px; color: blue; font-weight: bold;")

        # Add widgets to layout
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.text_input)
        self.layout.addWidget(self.combo)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def update_label(self):
        """ Updates the label dynamically based on user input """
        name = self.text_input.text()
        category = self.combo.currentText()
        if name and category != "Select Category":
            self.result_label.setText(f"Hello {name}, you are a {category}!")
        else:
            self.result_label.setText("")

    def display_message(self):
        """ Displays a message when the button is clicked """
        if self.result_label.text():
            self.result_label.setStyleSheet("color: green; font-weight: bold;")
        else:
            self.result_label.setText("Please enter your name and select a category!")
            self.result_label.setStyleSheet("color: red; font-weight: bold;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CustomWidgetsApp()
    window.show()
    sys.exit(app.exec())
