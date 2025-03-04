from PyQt6.QtWidgets import QApplication, QMainWindow, QToolBar, QLabel
from PyQt6.QtGui import QAction  # Correct import for QAction
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QMainWindow Example")
        self.resize(600, 400)

        # Create Menu Bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        edit_menu = menu_bar.addMenu("Edit")
        help_menu = menu_bar.addMenu("Help")

        # Add Actions to Menu Bar
        open_action = QAction("Open", self)
        save_action = QAction("Save", self)
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)

        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        # Create Tool Bar
        tool_bar = QToolBar("Main Toolbar")
        self.addToolBar(tool_bar)
        tool_bar.addAction(open_action)
        tool_bar.addAction(save_action)

        # Create Status Bar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("Ready")

        # Set Central Widget (Optional)
        self.label = QLabel("Welcome to QMainWindow Example", self)
        self.label.setStyleSheet("font-size: 32px;")
        self.setCentralWidget(self.label)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
