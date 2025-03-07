import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class ImageDisplayApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fixed Size Image Display")
        self.setGeometry(100, 100, 400, 400)

        # Create a fixed-size QLabel
        self.image_label = QLabel("Select an Image")
        self.image_label.setFixedSize(100, 50)  # Fixed size label
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("border: 2px solid black;")

        # Button to load an image
        self.load_button = QPushButton("Load Image")
        self.load_button.clicked.connect(self.load_image)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.load_button)
        self.setLayout(layout)

    def load_image(self):
        """Opens a file dialog to select an image and displays it while maintaining aspect ratio."""
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg *.bmp)")

        if file_path:
            pixmap = QPixmap(file_path)
            scaled_pixmap = pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image_label.setPixmap(scaled_pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageDisplayApp()
    window.show()
    sys.exit(app.exec())
