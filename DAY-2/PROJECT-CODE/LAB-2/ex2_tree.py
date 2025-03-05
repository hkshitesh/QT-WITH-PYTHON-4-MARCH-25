from PySide6.QtWidgets import QApplication, QTreeView, QFileSystemModel, QMenu
from PySide6.QtCore import Qt, QPoint
import sys

class CustomTreeView(QTreeView):
    def __init__(self):
        super().__init__()

        # Set up file system model
        self.model = QFileSystemModel()
        self.model.setRootPath("")
        self.setModel(self.model)
        self.setRootIndex(self.model.index("."))

        self.setWindowTitle("Custom QTreeView")
        self.resize(600, 400)

        # Enable right-click context menu
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)

    def show_context_menu(self, position: QPoint):
        """Creates a right-click context menu."""
        menu = QMenu()
        expand_action = menu.addAction("Expand All")
        collapse_action = menu.addAction("Collapse All")

        action = menu.exec_(self.viewport().mapToGlobal(position))
        if action == expand_action:
            self.expandAll()
        elif action == collapse_action:
            self.collapseAll()

app = QApplication(sys.argv)
tree = CustomTreeView()
tree.show()
sys.exit(app.exec())
