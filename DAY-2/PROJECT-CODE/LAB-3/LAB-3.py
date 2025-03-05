import sys
import time
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QProgressBar
from PySide6.QtCore import QThread, Signal

class WorkerThread(QThread):
    """ Background thread that performs a long-running task. """
    progress = Signal(int)  # Custom signal to send progress updates

    def run(self):
        """ Runs the background task """
        for i in range(1, 101):  # Simulate task from 1% to 100%
            time.sleep(0.5)  # Simulate work (sleep for 50ms)
            self.progress.emit(i)  # Emit progress value

class ThreadExample(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QThread Example - PySide6")
        self.setGeometry(300, 300, 400, 200)

        # Layout
        self.layout = QVBoxLayout()

        # Progress Bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)

        # Start Button
        self.start_button = QPushButton("Start Task")
        self.start_button.clicked.connect(self.start_task)

        # Add widgets to layout
        self.layout.addWidget(self.progress_bar)
        self.layout.addWidget(self.start_button)

        self.setLayout(self.layout)

    def start_task(self):
        """ Starts the background thread """
        self.thread = WorkerThread()
        self.thread.progress.connect(self.progress_bar.setValue)  # Update progress bar
        self.thread.start()  # Start the thread

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ThreadExample()
    window.show()
    sys.exit(app.exec())
