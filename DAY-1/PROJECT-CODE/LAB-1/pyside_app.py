from PySide6.QtWidgets import QApplication, QLabel, QWidget
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("PySide Example")
window.resize(400, 300)
label = QLabel("Hello, PySide!", parent=window)
window.show()
sys.exit(app.exec())