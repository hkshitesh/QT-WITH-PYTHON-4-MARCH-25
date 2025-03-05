from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import QThread, Signal
import time
import sys


class WorkerThread(QThread):
    """Worker thread that supports pause, resume, and cancel."""
    progress = Signal(int)  # Signal to update UI progress
    finished = Signal(str)  # Signal to notify completion

    def __init__(self):
        super().__init__()
        self._is_paused = False
        self._is_running = True

    def run(self):
        """Background task that runs in a separate thread."""
        for i in range(10):
            if not self._is_running:
                self.finished.emit("Task Canceled")
                return

            while self._is_paused:  # Pause execution
                time.sleep(0.1)

            time.sleep(1)  # Simulate work
            self.progress.emit(i + 1)  # Emit progress

        self.finished.emit("Task Completed")  # Emit completion message

    def pause(self):
        """Pause the execution."""
        self._is_paused = True

    def resume(self):
        """Resume execution."""
        self._is_paused = False

    def stop(self):
        """Stop execution."""
        self._is_running = False


class MyWindow(QWidget):
    """Main Window with buttons to control threading."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pause, Resume, Cancel QThread")
        self.resize(300, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Click Start to begin")
        layout.addWidget(self.label)

        self.start_button = QPushButton("Start Task")
        self.start_button.clicked.connect(self.start_task)
        layout.addWidget(self.start_button)

        self.pause_button = QPushButton("Pause Task")
        self.pause_button.clicked.connect(self.pause_task)
        self.pause_button.setEnabled(False)
        layout.addWidget(self.pause_button)

        self.resume_button = QPushButton("Resume Task")
        self.resume_button.clicked.connect(self.resume_task)
        self.resume_button.setEnabled(False)
        layout.addWidget(self.resume_button)

        self.cancel_button = QPushButton("Cancel Task")
        self.cancel_button.clicked.connect(self.cancel_task)
        self.cancel_button.setEnabled(False)
        layout.addWidget(self.cancel_button)

        self.setLayout(layout)

    def start_task(self):
        """Start the worker thread."""
        self.worker = WorkerThread()
        self.worker.progress.connect(self.update_label)
        self.worker.finished.connect(self.task_finished)
        self.worker.start()

        self.start_button.setEnabled(False)
        self.pause_button.setEnabled(True)
        self.cancel_button.setEnabled(True)

    def pause_task(self):
        """Pause the worker thread."""
        self.worker.pause()
        self.pause_button.setEnabled(False)
        self.resume_button.setEnabled(True)

    def resume_task(self):
        """Resume the worker thread."""
        self.worker.resume()
        self.pause_button.setEnabled(True)
        self.resume_button.setEnabled(False)

    def cancel_task(self):
        """Stop the worker thread."""
        self.worker.stop()
        self.pause_button.setEnabled(False)
        self.resume_button.setEnabled(False)
        self.cancel_button.setEnabled(False)
        self.start_button.setEnabled(True)

    def update_label(self, value):
        """Update UI safely from worker thread."""
        self.label.setText(f"Progress: {value}/10")

    def task_finished(self, message):
        """Handle task completion."""
        self.label.setText(message)
        self.start_button.setEnabled(True)
        self.pause_button.setEnabled(False)
        self.resume_button.setEnabled(False)
        self.cancel_button.setEnabled(False)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
