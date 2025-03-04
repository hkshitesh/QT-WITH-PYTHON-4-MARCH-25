import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QFileDialog
class ImageWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Viewer - PyQt6")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        # QLabel to display image
        self.label = QLabel(self)
        image_path, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if image_path:
            pixmap = QPixmap(image_path)
            self.label.setPixmap(pixmap)

        # pixmap = QPixmap("assets/nplogo.png")  # Path to the image file
        # self.label.setPixmap(pixmap)
        self.label.setScaledContents(False)  # Scale image to fit the label

        layout.addWidget(self.label)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageWindow()
    window.show()
    sys.exit(app.exec())
