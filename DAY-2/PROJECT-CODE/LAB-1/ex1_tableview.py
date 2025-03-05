from PySide6.QtWidgets import QApplication, QTableView
from PySide6.QtGui import QStandardItemModel, QStandardItem
import sys

app = QApplication(sys.argv)

# Create a data model
model = QStandardItemModel(4, 3)  # 4 rows, 3 columns
model.setHorizontalHeaderLabels(["Name", "Age", "Country"])

# Populate table with data
data = [
    ("Alice", 25, "USA"),
    ("Bob", 30, "UK"),
    ("Charlie", 28, "Canada"),
    ("David", 35, "Germany"),
]

for row, (name, age, country) in enumerate(data):
    model.setItem(row, 0, QStandardItem(name))
    model.setItem(row, 1, QStandardItem(str(age)))
    model.setItem(row, 2, QStandardItem(country))

# Create a table view and set the model
table = QTableView()
table.setModel(model)
table.setWindowTitle("QTableView Example")
table.resize(400, 300)
table.show()

sys.exit(app.exec())
