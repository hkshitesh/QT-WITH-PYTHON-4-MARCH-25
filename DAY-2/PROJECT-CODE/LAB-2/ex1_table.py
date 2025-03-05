from PySide6.QtWidgets import QApplication, QTableView, QVBoxLayout, QWidget, QPushButton
from PySide6.QtGui import QStandardItemModel, QStandardItem
import sys

class EditableTable(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom QTableView Example")
        self.resize(400, 300)

        layout = QVBoxLayout()

        # Create Table Model
        self.model = QStandardItemModel(3, 2)
        self.model.setHorizontalHeaderLabels(["Name", "Age"])

        # Populate table with default data
        data = [("Alice", "25"), ("Bob", "30"), ("Charlie", "28")]
        for row, (name, age) in enumerate(data):
            self.model.setItem(row, 0, QStandardItem(name))
            self.model.setItem(row, 1, QStandardItem(age))

        # Create Table View
        self.table = QTableView()
        self.table.setModel(self.model)
        layout.addWidget(self.table)

        # Button to print table data
        self.button = QPushButton("Print Table Data")
        self.button.clicked.connect(self.print_data)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def print_data(self):
        """Prints the table content"""
        for row in range(self.model.rowCount()):
            name = self.model.item(row, 0).text()
            age = self.model.item(row, 1).text()
            print(f"Row {row}: Name={name}, Age={age}")

app = QApplication(sys.argv)
window = EditableTable()
window.show()
sys.exit(app.exec())
