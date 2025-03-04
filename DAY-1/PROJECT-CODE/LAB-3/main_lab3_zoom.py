from PySide6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QPushButton, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys


class ImageWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Viewer")
        self.resize(600, 500)
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # QLabel to display the image
        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap())  # Placeholder
        self.image_label.setScaledContents(True)

        # Buttons
        self.load_button = QPushButton("Load Image")
        self.zoom_in_button = QPushButton("Zoom In")
        self.zoom_out_button = QPushButton("Zoom Out")
        self.load_button.setFixedSize(100, 50)
        self.zoom_in_button.setFixedSize(100, 50)
        self.zoom_out_button.setFixedSize(100, 50)

        # Connect buttons to actions
        self.load_button.clicked.connect(self.load_image)
        self.zoom_in_button.clicked.connect(self.zoom_in)
        self.zoom_out_button.clicked.connect(self.zoom_out)

        # Add widgets to grid layout
        self.layout.addWidget(self.image_label, 0, 0, 1, 3)  # Image spans 3 columns
        self.layout.addWidget(self.load_button, 1, 0)
        self.layout.addWidget(self.zoom_in_button, 1, 1)
        self.layout.addWidget(self.zoom_out_button, 1, 2)

        self.current_pixmap = None  # Store the loaded image
        self.zoom_factor = 1.0  # Track zoom level


    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if file_path:
            self.current_pixmap = QPixmap(file_path)
            self.zoom_factor = 1.0  # Reset zoom
            self.update_image_display()


    def zoom_in(self):
        if self.current_pixmap:
            self.zoom_factor *= 1.2  # Increase size by 20%
            self.update_image_display()


    def zoom_out(self):
        if self.current_pixmap:
            self.zoom_factor *= 0.8  # Decrease size by 20%
            self.update_image_display()


    def update_image_display(self):
        if self.current_pixmap:
            scaled_pixmap = self.current_pixmap.scaled(
                self.current_pixmap.size() * self.zoom_factor,
                # Qt.AspectRatioMode.KeepAspectRatio
            )
            self.image_label.setPixmap(scaled_pixmap)


app = QApplication(sys.argv)
window = ImageWindow()
window.show()
sys.exit(app.exec())
