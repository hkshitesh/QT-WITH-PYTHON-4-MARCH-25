from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Grid Layout")
window.resize(400, 300)

layout = QGridLayout()  # Create a grid layout
layout.addWidget(QPushButton("Button 1"), 0, 0)  # Row 0, Column 0
layout.addWidget(QPushButton("Button 2"), 0, 1)  # Row 0, Column 1
layout.addWidget(QPushButton("Button 3"), 1, 0)  # Row 1, Column 0
layout.addWidget(QPushButton("Button 4"), 1, 1)  # Row 1, Column 1

window.setLayout(layout)
window.show()
sys.exit(app.exec())
