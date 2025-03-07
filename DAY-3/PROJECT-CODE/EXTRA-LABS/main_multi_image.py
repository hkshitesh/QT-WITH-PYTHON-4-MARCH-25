import sys
import os
import time
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QThread, Signal, QTimer


class ImageLoaderThread(QThread):
    image_loaded = Signal(int, QPixmap)  # (Label Index, Loaded Image)

    def __init__(self, label_index, image_path):
        super().__init__()
        self.label_index = label_index
        self.image_path = image_path

    def run(self):
        """Loads the image with a slight delay to simulate real loading."""
        time.sleep(0.5)  # Simulate loading time
        pixmap = QPixmap(self.image_path)
        self.image_loaded.emit(self.label_index, pixmap)


class MultiFolderImageRotator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rotating Image Loader - PySide6")
        self.setGeometry(200, 200, 400, 300)

        # Layout
        self.layout = QVBoxLayout()

        # 4 QLabel widgets for images
        self.labels = [QLabel(f"Label {i+1}") for i in range(4)]
        for label in self.labels:
            label.setAlignment(Qt.AlignCenter)
            label.setFixedSize(100, 50)
            label.setStyleSheet("border: 2px solid black; padding: 5px;")
            self.layout.addWidget(label)

        # Select Folders Button
        self.select_button = QPushButton("Select 4 Folders")
        self.select_button.clicked.connect(self.select_folders)
        self.layout.addWidget(self.select_button)

        # Start Rotation Button
        self.start_button = QPushButton("Start Image Rotation")
        self.start_button.clicked.connect(self.start_image_rotation)
        self.layout.addWidget(self.start_button)
        self.start_button.setEnabled(False)

        self.setLayout(self.layout)

        self.image_folders = []  # Store selected folders
        self.image_paths = [[] for _ in range(4)]  # Store images per folder
        self.current_indices = [0] * 4  # Track current image index per folder
        self.threads = []  # Keep track of threads to prevent garbage collection

        # Timer to update images every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_images)

    def select_folders(self):
        """Opens dialog to select 4 folders containing images."""
        self.image_folders.clear()
        for i in range(4):
            folder = QFileDialog.getExistingDirectory(self, f"Select Folder {i+1}")
            if folder:
                self.image_folders.append(folder)

        if len(self.image_folders) == 4:
            self.find_images()
            self.start_button.setEnabled(True)

    def find_images(self):
        """Finds up to 10 images per folder."""
        self.image_paths = [[] for _ in range(4)]
        for i, folder in enumerate(self.image_folders):
            images = [os.path.join(folder, f) for f in os.listdir(folder)
                      if f.lower().endswith((".png", ".jpg", ".jpeg", ".bmp"))]
            self.image_paths[i] = images[:10]  # Store first 10 images

    def start_image_rotation(self):
        """Starts the timer to update images every second."""
        self.current_indices = [0] * 4  # Reset index counters
        self.timer.start(1000)  # Update every 1 second

    def update_images(self):
        """Loads the next image for each label using threads."""
        for i in range(4):  # Iterate through labels
            if self.image_paths[i]:  # Ensure images exist in folder
                image_index = self.current_indices[i] % len(self.image_paths[i])
                image_path = self.image_paths[i][image_index]

                thread = ImageLoaderThread(i, image_path)
                thread.image_loaded.connect(self.display_image)
                self.threads.append(thread)
                thread.start()

                self.current_indices[i] += 1  # Move to the next image

    def display_image(self, label_index, pixmap):
        """Updates the QLabel with the loaded image."""
        scaled_pixmap = pixmap.scaled(self.labels[label_index].size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.labels[label_index].setPixmap(scaled_pixmap)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MultiFolderImageRotator()
    window.show()
    sys.exit(app.exec())
