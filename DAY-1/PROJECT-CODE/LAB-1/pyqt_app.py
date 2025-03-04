from PyQt6.QtWidgets import QApplication, QLabel, QWidget
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Demo PyQt6 App')
window.resize(400,300)
label = QLabel('Hello PyQt6!', parent=window)

window.show()
sys.exit(app.exec())





