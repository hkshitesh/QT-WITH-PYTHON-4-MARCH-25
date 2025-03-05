from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLabel
import sys

class ComboBoxExample(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QComboBox Example")
        self.resize(300, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Select an option:")


        self.combo = QComboBox()
        self.combo.addItems(["Python", "C++", "Java", "JavaScript"])
        self.combo.currentIndexChanged.connect(self.on_selection_change)
        layout.addWidget(self.combo)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def on_selection_change(self, index):
        self.label.setText(f"Selected: {self.combo.itemText(index)}")

app = QApplication(sys.argv)
window = ComboBoxExample()
window.show()
sys.exit(app.exec())
