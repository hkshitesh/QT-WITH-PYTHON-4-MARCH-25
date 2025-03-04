import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog
from PyQt6.QtGui import QPixmap


class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dynamic Image Viewer - PyQt6")
        self.setGeometry(200, 200, 600, 500)

        # Layout
        self.layout = QVBoxLayout()

        # QLabel to display image
        self.label = QLabel(self)
        self.label.setText("No image loaded")
        self.label.setStyleSheet("QLabel { font-size: 16px; color: gray; }")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # QPushButton to load image
        self.load_button = QPushButton("Load Image")
        self.load_button.setFixedSize(300, 60)
        self.load_button.clicked.connect(self.load_image)
        # self.load_button.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add widgets to layout
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.load_button)

        self.setLayout(self.layout)

    def load_image(self):
        """ Opens a file dialog to select an image and displays it in QLabel """
        image_path, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if image_path:
            pixmap = QPixmap(image_path)
            self.label.setPixmap(pixmap)
            self.label.setScaledContents(False)  # Scale image to fit label size
            # self.label.setFixedSize(500, 400)  # Set a fixed size for better appearance
        else:
            self.label.setText("No image selected")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageViewer()
    window.show()
    sys.exit(app.exec())