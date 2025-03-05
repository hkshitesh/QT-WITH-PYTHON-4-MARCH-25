from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout
from PySide6.QtCore import QRunnable, QThreadPool, Signal, QObject
import time
import sys

class WorkerSignals(QObject):
    """Defines custom signals for the worker."""
    progress = Signal(str, int)  # Signal to send progress messages (text, worker ID)
    finished = Signal(int)  # Signal to notify when task is complete (worker ID)

class Worker(QRunnable):
    """Worker task that runs in a thread pool."""
    def __init__(self, worker_id):
        super().__init__()
        self.worker_id = worker_id
        self.signals = WorkerSignals()

    def run(self):
        """Runs the task in a separate thread."""
        for i in range(50):
            time.sleep(0.5)
            self.signals.progress.emit(f"Task {self.worker_id} progress: {i+1}/50", self.worker_id)
        self.signals.finished.emit(self.worker_id)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QThreadPool Example")
        self.resize(400, 300)

        self.layout = QVBoxLayout()

        self.label_main = QLabel("Click to start workers")
        self.layout.addWidget(self.label_main)

        self.button = QPushButton("Start 3 Tasks")
        self.button.clicked.connect(self.start_workers)
        self.layout.addWidget(self.button)

        # Separate labels for each worker
        self.worker_labels = {}
        for i in range(3):
            label = QLabel(f"Task {i+1}: Waiting...")
            self.layout.addWidget(label)
            self.worker_labels[i + 1] = label  # Store labels in a dictionary

        self.setLayout(self.layout)

        self.threadpool = QThreadPool()

    def start_workers(self):
        """Starts multiple worker tasks in the thread pool."""
        for i in range(3):  # Start 3 workers
            worker = Worker(i + 1)
            worker.signals.progress.connect(self.update_label)
            worker.signals.finished.connect(self.task_finished)
            self.threadpool.start(worker)

    def update_label(self, msg, worker_id):
        """Updates label with worker progress."""
        self.worker_labels[worker_id].setText(msg)

    def task_finished(self, worker_id):
        """Marks task as completed."""
        self.worker_labels[worker_id].setText(f"Task {worker_id} completed!")

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())



