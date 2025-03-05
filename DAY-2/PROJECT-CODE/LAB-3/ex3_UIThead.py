from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import QThread, Signal
import time
import sys

class WorkerThread(QThread):
    progress = Signal(int)  # Custom signal to update UI

    def run(self):
        """Long-running task (runs in background)."""
        for i in range(100):
            time.sleep(1)  # Simulate work
            self.progress.emit(i + 1)  # Send progress update


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QThread Example")
        self.resize(300, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Click the button to start task")
        layout.addWidget(self.label)

        self.label2 = QLabel("Another Task")
        layout.addWidget(self.label2)

        self.button = QPushButton("Start Task")
        self.button.setFixedSize(200, 50)
        self.button.clicked.connect(self.start_thread)
        layout.addWidget(self.button)

        self.button2 = QPushButton("Second Task Button")
        self.button2.clicked.connect(self.print_msg)
        layout.addWidget(self.button2)
        self.button2.setFixedSize(200, 50)
        self.setLayout(layout)

    def print_msg(self):
        self.label2.setText("This is second action")


    def start_thread(self):
        """Start the worker thread."""
        self.worker = WorkerThread()
        self.worker.progress.connect(self.update_label)  # Connect signal to UI update
        self.worker.start()

    def update_label(self, value):
        """Update the UI from the worker thread."""
        self.label.setText(f"Progress: {value}/5")

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
