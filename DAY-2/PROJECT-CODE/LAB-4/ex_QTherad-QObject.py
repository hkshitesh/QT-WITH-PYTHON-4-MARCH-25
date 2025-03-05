from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import QObject, QThread, Signal
import time
import sys

class Worker(QObject):
    """Worker object that runs in a separate thread."""
    progress = Signal(int)
    finished = Signal()

    def do_work(self):
        """Background task that runs in the worker thread."""
        for i in range(5):
            time.sleep(1)  # Simulate work
            self.progress.emit(i + 1)
        self.finished.emit()

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Responsive GUI with Worker QThread")
        self.resize(300, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Click button to start task")
        layout.addWidget(self.label)

        self.button = QPushButton("Start Task")
        self.button.clicked.connect(self.start_worker)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def start_worker(self):
        """Start the worker thread."""
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.do_work)
        self.worker.progress.connect(self.update_label)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()

    def update_label(self, value):
        """Update UI safely from worker thread."""
        self.label.setText(f"Progress: {value}/5")

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
