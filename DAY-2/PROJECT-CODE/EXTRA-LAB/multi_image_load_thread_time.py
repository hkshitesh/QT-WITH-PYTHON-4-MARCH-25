import sys
import time
import os
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QThread, Signal

class ImageLoaderThread(QThread):
    image_loaded = Signal(int, QPixmap, float)  # Add time_taken to signal

    def __init__(self, index, image_path):
        super().__init__()
        self.index = index
        self.image_path = image_path

    def run(self):
        """ Loads the image with a simulated delay and measures time taken """
        start_time = time.time()  # Record start time
        time.sleep(2)  # Simulating a delay in loading
        pixmap = QPixmap(self.image_path)
        end_time = time.time()  # Record end time

        time_taken = end_time - start_time  # Compute time taken
        print(f"Thread {self.index + 1} took {time_taken:.2f} seconds to load image")
        self.image_loaded.emit(self.index, pixmap, time_taken)  # Send time_taken to UI

class MultiFolderImageLoaderApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Multithreaded Folder Image Loader - PySide6")
        self.setGeometry(200, 200, 500, 500)

        # Layout
        self.layout = QVBoxLayout()

        # QLabel widgets to display images and time taken
        self.labels = [QLabel(f"Image {i+1} not loaded") for i in range(4)]
        self.time_labels = [QLabel("") for _ in range(4)]  # Labels for time taken
        for label, time_label in zip(self.labels, self.time_labels):
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label.setStyleSheet("border: 1px solid black; padding: 5px;")
            self.layout.addWidget(label)
            self.layout.addWidget(time_label)  # Add time label below image

        # Select Folder Button
        self.select_button = QPushButton("Select 4 Folders")
        self.select_button.setFixedSize(500, 50)
        self.select_button.clicked.connect(self.select_folders)
        self.layout.addWidget(self.select_button)

        # Load Button
        self.load_button = QPushButton("Load Images")
        self.load_button.setFixedSize(500, 50)
        self.load_button.clicked.connect(self.load_images)
        self.layout.addWidget(self.load_button)
        self.load_button.setEnabled(False)  # Disabled until folders are selected

        self.setLayout(self.layout)

        self.image_folders = []  # Store selected folders
        self.image_paths = []  # Store image file paths
        self.threads = []  # Store threads to prevent garbage collection

    def select_folders(self):
        """ Opens dialog to select 4 folders containing images """
        self.image_folders = []
        for i in range(4):
            folder = QFileDialog.getExistingDirectory(self, f"Select Folder {i+1}")
            if folder:
                self.image_folders.append(folder)

        if len(self.image_folders) == 4:
            self.find_images()
            self.load_button.setEnabled(True)  # Enable load button after folder selection

    def find_images(self):
        """ Finds the first image file in each selected folder """
        self.image_paths = []
        for folder in self.image_folders:
            for file in os.listdir(folder):
                if file.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
                    self.image_paths.append(os.path.join(folder, file))
                    break

    def load_images(self):
        """ Starts separate threads for loading each image """
        if len(self.image_paths) < 4:
            return  # Ensure we have valid image paths

        for i, image_path in enumerate(self.image_paths):
            thread = ImageLoaderThread(i, image_path)
            thread.image_loaded.connect(self.display_image)
            self.threads.append(thread)
            thread.start()

    def display_image(self, index, pixmap, time_taken):
        """ Updates the corresponding QLabel with the loaded image and time taken """
        self.labels[index].setPixmap(pixmap)
        self.labels[index].setScaledContents(False)
        self.time_labels[index].setText(f"Loaded in {time_taken:.2f} seconds")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MultiFolderImageLoaderApp()
    window.show()
    sys.exit(app.exec())
