from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
import sys
from PySide6.QtCore import Qt

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Basic Widgets")
window.setGeometry(300, 200, 400, 250)

main_layout = QVBoxLayout()
main_layout.setSpacing(15)  # Spacing between widgets
main_layout.setContentsMargins(20, 20, 20, 20)  # Margins around layout

# Label with fixed size
label = QLabel("Welcome to PyQt!")
# label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
label.setFixedSize(250, 50)  # Set fixed width & height

# Horizontal Layout for Buttons
button_layout = QHBoxLayout()
button_layout.setSpacing(20)  # Spacing between buttons

# Buttons with different sizes
btn_small = QPushButton("Small")
btn_small.setFixedSize(100, 40)  # Small button

btn_medium = QPushButton("Medium")
btn_medium.setFixedSize(100, 40)  # Medium button (allows expansion)

btn_large = QPushButton("Large")
btn_large.setFixedSize(100, 40)  # Large button

# Add buttons to horizontal layout
button_layout.addWidget(btn_small)
button_layout.addWidget(btn_medium)
button_layout.addWidget(btn_large)

main_layout.addWidget(btn_small)
main_layout.addWidget(btn_medium)
main_layout.addWidget(btn_large)
# main_layout.addLayout(button_layout)

window.setLayout(main_layout)

window.show()
sys.exit(app.exec())

