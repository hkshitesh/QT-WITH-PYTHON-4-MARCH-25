import sys
import re
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout,
    QPushButton, QMessageBox, QComboBox, QSpinBox
)
from PySide6.QtGui import QIntValidator, QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression


class UserForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("User Registration Form")
        self.resize(400, 250)

        layout = QVBoxLayout()

        # Name Input
        self.name_label = QLabel("Full Name:")
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter your name")
        self.name_input.textChanged.connect(self.validate_name)
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        # Email Input
        self.email_label = QLabel("Email Address:")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter your email")
        email_regex = QRegularExpression(r"^[\w\.-]+@[\w\.-]+\.\w+$")
        self.email_input.setValidator(QRegularExpressionValidator(email_regex))
        self.email_input.textChanged.connect(self.validate_email)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)

        # Age Input
        self.age_label = QLabel("Age:")
        self.age_input = QSpinBox()
        self.age_input.setRange(18, 100)  # Accept only ages between 18 and 100
        layout.addWidget(self.age_label)
        layout.addWidget(self.age_input)

        # Country Selection
        self.country_label = QLabel("Country:")
        self.country_input = QComboBox()
        self.country_input.addItems(["Select", "USA", "Canada", "UK", "India", "Australia"])
        layout.addWidget(self.country_label)
        layout.addWidget(self.country_input)

        # Submit Button
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_form)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def validate_name(self):
        """Ensure the name field is not empty."""
        if len(self.name_input.text()) < 3:
            self.name_input.setStyleSheet("border: 3px solid red;")
        else:
            self.name_input.setStyleSheet("")

    def validate_email(self):
        """Ensure the email format is valid."""
        email_text = self.email_input.text()
        if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email_text):
            self.email_input.setStyleSheet("")
        else:
            self.email_input.setStyleSheet("border: 3px solid red;")

    def submit_form(self):
        """Validate the form before submission."""
        if len(self.name_input.text()) < 3:
            QMessageBox.warning(self, "Validation Error", "Name must be at least 3 characters long.")
            return

        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", self.email_input.text()):
            QMessageBox.warning(self, "Validation Error", "Enter a valid email address.")
            return

        if self.country_input.currentText() == "Select":
            QMessageBox.warning(self, "Validation Error", "Please select a country.")
            return

        QMessageBox.information(self, "Success", "Form submitted successfully!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserForm()
    window.show()
    sys.exit(app.exec())
