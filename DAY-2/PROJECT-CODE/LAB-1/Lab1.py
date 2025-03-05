import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTreeView, QTableView, QComboBox
from PySide6.QtGui import QStandardItemModel, QStandardItem
class AdvancedWidgetsDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced Widgets in PySide6")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        # ComboBox Setup
        self.comboBox = QComboBox()
        self.comboBox.addItems(["Fruits", "Vegetables"])
        self.comboBox.currentTextChanged.connect(self.updateTableView)
        layout.addWidget(self.comboBox)

        # TreeView Setup
        self.treeView = QTreeView()
        self.treeModel = self.createTreeModel()
        self.treeView.setModel(self.treeModel)
        layout.addWidget(self.treeView)

        # TableView Setup
        self.tableView = QTableView()
        self.tableModel = self.createTableModel("Fruits")  # Default category
        self.tableView.setModel(self.tableModel)
        layout.addWidget(self.tableView)

        self.setLayout(layout)

    def createTreeModel(self):
        """Creates a tree structure with parent-child relationships."""
        model = QStandardItemModel()
        rootNode = model.invisibleRootItem()

        # Fruits Category
        fruits = QStandardItem("Fruits")
        fruits.appendRow(QStandardItem("Apple"))
        fruits.appendRow(QStandardItem("Banana"))
        fruits.appendRow(QStandardItem("Cherry"))

        # Vegetables Category
        vegetables = QStandardItem("Vegetables")
        vegetables.appendRow(QStandardItem("Carrot"))
        vegetables.appendRow(QStandardItem("Broccoli"))
        vegetables.appendRow(QStandardItem("Spinach"))

        # Add categories to root
        rootNode.appendRow(fruits)
        rootNode.appendRow(vegetables)

        return model

    def createTableModel(self, category):
        """Creates a table model based on the selected category."""
        model = QStandardItemModel(3, 2)  # 3 Rows, 2 Columns
        model.setHorizontalHeaderLabels(["Item", "Price ($)"])

        data = {
            "Fruits": [("Apple", "1.2"), ("Banana", "0.8"), ("Cherry", "2.5")],
            "Vegetables": [("Carrot", "0.5"), ("Broccoli", "1.0"), ("Spinach", "1.5")],
        }

        for row, (name, price) in enumerate(data[category]):
            model.setItem(row, 0, QStandardItem(name))
            model.setItem(row, 1, QStandardItem(price))

        return model

    def updateTableView(self, selected_category):
        """Updates the TableView based on ComboBox selection."""
        self.tableModel = self.createTableModel(selected_category)
        self.tableView.setModel(self.tableModel)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdvancedWidgetsDemo()
    window.show()
    sys.exit(app.exec())
