from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLabel, QPushButton
import sys

class DynamicComboBox(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Custom QComboBox Example")
        self.resize(300, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Select an option:")
        layout.addWidget(self.label)

        self.combo = QComboBox()
        self.combo.addItems(["Python", "C++", "Java", "JavaScript"])
        self.combo.currentIndexChanged.connect(self.on_selection_change)
        layout.addWidget(self.combo)

        self.button = QPushButton("Add Item")
        self.button.clicked.connect(self.add_new_item)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def on_selection_change(self, index):
        """Handles dropdown selection changes."""
        self.label.setText(f"Selected: {self.combo.itemText(index)}")

    def add_new_item(self):
        """Adds a new item to the ComboBox dynamically."""
        new_item = f"NewLang {self.combo.count() + 1}"
        self.combo.addItem(new_item)

app = QApplication(sys.argv)
window = DynamicComboBox()
window.show()
sys.exit(app.exec())
