import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox
)
from PySide6.QtGui import QIntValidator, QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression

class UserForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("User Input Form - PySide6")
        self.setGeometry(300, 200, 400, 250)

        layout = QVBoxLayout()

        # Name Input
        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter your name")
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        # Email Input with Validation
        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter your email")
        email_regex = QRegularExpression(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
        self.email_input.setValidator(QRegularExpressionValidator(email_regex))
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)

        # Age Input with Integer Validation
        self.age_label = QLabel("Age:")
        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Enter your age (18-99)")
        self.age_input.setValidator(QIntValidator(18, 99))  # Only allow ages 18-99
        layout.addWidget(self.age_label)
        layout.addWidget(self.age_input)

        # Gender Selection
        self.gender_label = QLabel("Gender:")
        self.male_radio = QRadioButton("Male")
        self.female_radio = QRadioButton("Female")

        gender_layout = QHBoxLayout()
        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)

        layout.addWidget(self.gender_label)
        layout.addLayout(gender_layout)

        # Submit Button
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.validate_form)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def validate_form(self):
        """ Validate user input and display a message box if valid """
        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        age = self.age_input.text().strip()
        gender = "Male" if self.male_radio.isChecked() else "Female" if self.female_radio.isChecked() else None

        if not name:
            QMessageBox.warning(self, "Validation Error", "Name cannot be empty!")
            return
        if not email:
            QMessageBox.warning(self, "Validation Error", "Please enter a valid email!")
            return
        if not age:
            QMessageBox.warning(self, "Validation Error", "Age is required!")
            return
        if not gender:
            QMessageBox.warning(self, "Validation Error", "Please select a gender!")
            return

        QMessageBox.information(self, "Success", f"Form Submitted!\n\nName: {name}\nEmail: {email}\nAge: {age}\nGender: {gender}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserForm()
    window.show()
    sys.exit(app.exec())
