import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog, QSlider, QHBoxLayout
from PySide6.QtGui import QPixmap, QImage, QTransform
from PySide6.QtCore import Qt

class ImageEditor(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Advanced Image Editor - PySide6")
        self.setGeometry(200, 200, 700, 600)

        # Layout
        self.layout = QVBoxLayout()

        # QLabel to display image
        self.label = QLabel(self)
        self.label.setText("No image loaded")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("QLabel { font-size: 16px; color: gray; }")

        # QPushButton to load image
        self.load_button = QPushButton("Load Image")
        self.load_button.setFixedSize(150, 80)
        self.load_button.clicked.connect(self.load_image)

        # QSlider for resizing the image
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(10)   # Minimum scale 10%
        self.slider.setMaximum(200)  # Maximum scale 200%
        self.slider.setValue(100)    # Default 100% (original size)
        self.slider.setTickInterval(10)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.valueChanged.connect(self.resize_image)

        # Rotate Button
        self.rotate_button = QPushButton("Rotate 90°")
        self.rotate_button.setFixedSize(100, 50)
        self.rotate_button.clicked.connect(self.rotate_image)

        # Grayscale Button
        self.grayscale_button = QPushButton("Grayscale")
        self.grayscale_button.setFixedSize(100, 50)
        self.grayscale_button.clicked.connect(self.convert_to_grayscale)

        # Horizontal layout for slider
        slider_layout = QHBoxLayout()
        slider_layout.addWidget(QLabel("10%"))
        slider_layout.addWidget(self.slider)
        slider_layout.addWidget(QLabel("200%"))

        # Horizontal layout for buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.rotate_button)
        button_layout.addWidget(self.grayscale_button)

        # Add widgets to layout
        self.layout.addWidget(self.label,alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.load_button,alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addLayout(slider_layout)
        self.layout.addLayout(button_layout)

        self.setLayout(self.layout)

        self.pixmap = None  # Store the original pixmap
        self.rotation_angle = 0  # Track rotation angle

    def load_image(self):
        """ Opens a file dialog to select an image and displays it in QLabel """
        image_path, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if image_path:
            self.pixmap = QPixmap(image_path)
            self.rotation_angle = 0  # Reset rotation
            self.label.setPixmap(self.pixmap)
            self.label.setScaledContents(False)  # Scale to fit label size
            self.label.setFixedSize(500, 400)   # Set fixed label size
        else:
            self.label.setText("No image selected")

    def resize_image(self):
        """ Resizes the image based on the slider value """
        if self.pixmap:
            scale_factor = self.slider.value() / 100  # Convert to percentage
            new_width = int(self.pixmap.width() * scale_factor)
            new_height = int(self.pixmap.height() * scale_factor)
            resized_pixmap = self.pixmap.scaled(new_width, new_height)
            self.label.setPixmap(resized_pixmap)

    def rotate_image(self):
        """ Rotates the image by 90 degrees """
        if self.pixmap:
            self.rotation_angle += 90  # Increase rotation angle
            transform = QTransform().rotate(self.rotation_angle)  # Rotate
            rotated_pixmap = self.pixmap.transformed(transform, Qt.TransformationMode.SmoothTransformation)
            self.label.setPixmap(rotated_pixmap)

    def convert_to_grayscale(self):
        """ Converts the image to grayscale """
        if self.pixmap:
            image = self.pixmap.toImage()
            grayscale_image = image.convertToFormat(QImage.Format_Grayscale8)
            self.pixmap = QPixmap.fromImage(grayscale_image)
            self.label.setPixmap(self.pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageEditor()
    window.show()
    sys.exit(app.exec())
