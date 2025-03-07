import sys
import time
import random
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QTextEdit
from PySide6.QtCore import Qt, QThread, Signal, QMutex, QWaitCondition

# Shared resource (queue of numbers)
data_queue = []
mutex = QMutex()  # Synchronization lock
condition = QWaitCondition()  # Condition variable for signaling


class ProducerThread(QThread):
    produced_signal = Signal(str)  # Signal to update UI

    def run(self):
        global data_queue
        for _ in range(5):
            time.sleep(random.uniform(1, 2))  # Simulate time delay in producing data

            mutex.lock()
            num = random.randint(1, 100)  # Produce a random number
            data_queue.append(num)  # Add to shared list
            self.produced_signal.emit(f"Produced: {num}")
            condition.wakeOne()  # Notify waiting consumer
            mutex.unlock()


class ConsumerThread(QThread):
    consumed_signal = Signal(str)  # Signal to update UI

    def run(self):
        global data_queue
        for _ in range(5):
            mutex.lock()
            while not data_queue:  # Wait until there is data to consume
                condition.wait(mutex)  # Wait until producer signals
            num = data_queue.pop(0)  # Consume data
            self.consumed_signal.emit(f"Consumed: {num}")
            mutex.unlock()
            time.sleep(random.uniform(1, 2))  # Simulate processing time


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Thread Synchronization in PySide6")
        self.setGeometry(200, 200, 400, 300)

        # UI Elements
        self.status_label = QLabel("Press 'Start' to run producer & consumer threads.")
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)

        self.start_button = QPushButton("Start Threads")
        self.start_button.clicked.connect(self.start_threads)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.status_label)
        layout.addWidget(self.log_text)
        layout.addWidget(self.start_button)
        self.setLayout(layout)

    def start_threads(self):
        """Start producer and consumer threads."""
        self.producer = ProducerThread()
        self.consumer = ConsumerThread()

        self.producer.produced_signal.connect(self.update_log)
        self.consumer.consumed_signal.connect(self.update_log)

        self.producer.start()
        self.consumer.start()

    def update_log(self, message):
        """Update log with messages from threads."""
        self.log_text.append(message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
