import sys
import time
import random
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QTextEdit
from PySide6.QtCore import Qt, QThread, Signal, QMutex

# Shared variables
counter = 0
log_messages = []
mutex = QMutex()  # Mutex to prevent race condition


class WorkerThread(QThread):
    update_signal = Signal(int, str)

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        global counter, log_messages
        for _ in range(5):
            time.sleep(random.uniform(0.1, 0.5))  # Simulate processing delay

            mutex.lock()  # Lock before modifying shared resources
            temp = counter
            counter = temp + 1
            log_messages.append(f"{self.name} incremented counter to {counter}")
            mutex.unlock()  # Unlock after update

            self.update_signal.emit(counter, log_messages[-1])


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Race Condition Demo - Fixed")
        self.setGeometry(200, 200, 400, 300)

        self.counter_label = QLabel("Counter: 0")
        self.counter_label.setAlignment(Qt.AlignCenter)

        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)

        self.start_button = QPushButton("Start Threads")
        self.start_button.clicked.connect(self.start_threads)

        layout = QVBoxLayout()
        layout.addWidget(self.counter_label)
        layout.addWidget(self.log_text)
        layout.addWidget(self.start_button)
        self.setLayout(layout)

    def start_threads(self):
        """Start two threads that modify shared resources safely"""
        self.thread1 = WorkerThread("Thread-1")
        self.thread2 = WorkerThread("Thread-2")

        self.thread1.update_signal.connect(self.update_ui)
        self.thread2.update_signal.connect(self.update_ui)

        self.thread1.start()
        self.thread2.start()

    def update_ui(self, count, log_msg):
        """Update UI with counter and log messages"""
        self.counter_label.setText(f"Counter: {count}")
        self.log_text.append(log_msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
