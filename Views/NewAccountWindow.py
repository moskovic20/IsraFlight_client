import re  # Import regex module for email and phone validation
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpacerItem, QSizePolicy
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtCore import Qt
import os


class NewAccountWindow(QWidget):
    def __init__(self, controller):
        super(NewAccountWindow, self).__init__()
        self.controller = controller
        self.setWindowTitle('Create Account')
        self.setGeometry(100, 50, 400, 600)  # Adjusted for a taller window

        # Set background color to white
        self.setStyleSheet("background-color: white;")

        # Path to images folder
        images_path = os.path.join(os.path.dirname(__file__), '..', 'Images')

        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)

        # Icon (Profile icon)
        profile_image = QLabel()
        user_icon_path = os.path.join(images_path, 'new_user_icon.png')  # Path to your icon
        profile_pixmap = QPixmap(user_icon_path)
        profile_image.setPixmap(profile_pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        profile_image.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(profile_image)

        # Spacer - Small gap between icon and input fields
        main_layout.addItem(QSpacerItem(20, 10, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Full Name Input
        self.fullname_input = QLineEdit()
        self.fullname_input.setPlaceholderText('Full Name')
        self.fullname_input.setFixedHeight(40)
        self.fullname_input.setStyleSheet("""
            border: 2px solid #000; 
            border-radius: 20px; 
            background-color: #f0f0f0; 
            padding-left: 15px;
        """)
        self.fullname_input.textChanged.connect(self.clear_error_message)  # Clear error on text change
        main_layout.addWidget(self.fullname_input)

        # Phone Number Input
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText('Phone Number')
        self.phone_input.setFixedHeight(40)
        self.phone_input.setStyleSheet("""
            border: 2px solid #000; 
            border-radius: 20px; 
            background-color: #f0f0f0; 
            padding-left: 15px;
        """)
        self.phone_input.textChanged.connect(self.clear_error_message)  # Clear error on text change
        main_layout.addWidget(self.phone_input)

        # Email Input
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText('Email')
        self.email_input.setFixedHeight(40)
        self.email_input.setStyleSheet("""
            border: 2px solid #000; 
            border-radius: 20px; 
            background-color: #f0f0f0; 
            padding-left: 15px;
        """)
        self.email_input.textChanged.connect(self.clear_error_message)  # Clear error on text change
        main_layout.addWidget(self.email_input)

        # Password Input
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText('Choose Password')
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setFixedHeight(40)
        self.password_input.setStyleSheet("""
            border: 2px solid #000; 
            border-radius: 20px; 
            background-color: #f0f0f0; 
            padding-left: 15px;
        """)
        self.password_input.textChanged.connect(self.clear_error_message)  # Clear error on text change
        main_layout.addWidget(self.password_input)

        # Confirm Password Input
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setPlaceholderText('Confirm Password')
        self.confirm_password_input.setEchoMode(QLineEdit.Password)
        self.confirm_password_input.setFixedHeight(40)
        self.confirm_password_input.setStyleSheet("""
            border: 2px solid #000; 
            border-radius: 20px; 
            background-color: #f0f0f0; 
            padding-left: 15px;
        """)
        self.confirm_password_input.textChanged.connect(self.clear_error_message)  # Clear error on text change
        main_layout.addWidget(self.confirm_password_input)

        # Spacer - Small gap between input fields and create account button
        main_layout.addItem(QSpacerItem(20, 15, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Create Account Button
        self.create_button = QPushButton('Create Account')
        self.create_button.setFixedHeight(40)
        self.create_button.setFont(QFont("Arial", 12))  # Increase button text size
        self.create_button.setStyleSheet("""
            QPushButton {
                background-color: #007bff; 
                color: white; 
                font-weight: bold; 
                border-radius: 20px;
            }
            QPushButton:hover {
                background-color: #0056b3; /* Change color on hover */
            }
        """)
        self.create_button.clicked.connect(self.create_account_click)  # Connect the signal to the slot
        main_layout.addWidget(self.create_button)

        # Spacer - Small gap between button and error label
        main_layout.addItem(QSpacerItem(20, 10, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Error Message Label (hidden by default)
        self.error_label = QLabel('')
        self.error_label.setAlignment(Qt.AlignCenter)
        self.error_label.setStyleSheet("color: red;")
        self.error_label.setVisible(False)  # Hidden by default
        main_layout.addWidget(self.error_label)

        # Spacer - Medium gap between error label and logo
        main_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Logo at the bottom
        logo_label = QLabel()
        logo_path = os.path.join(images_path, 'logo.png')  # Path to logo image
        logo_pixmap = QPixmap(logo_path)
        logo_label.setPixmap(logo_pixmap.scaled(150, 75, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        logo_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(logo_label)

        # Set main layout
        self.setLayout(main_layout)

    def create_account_click(self):
        # Retrieve the input values
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()
        fullname = self.fullname_input.text()
        email = self.email_input.text()
        phone_number = self.phone_input.text()

        # Validation Logic
        if not fullname or not email or not password or not confirm_password or not phone_number:
            self.error_label.setText("All fields must be filled!")
            self.error_label.setVisible(True)
            return

        if not self.validate_email(email):
            self.error_label.setText("Invalid email address!")
            self.error_label.setVisible(True)
            return

        if not self.validate_phone(phone_number):
            self.error_label.setText("Invalid phone number!")
            self.error_label.setVisible(True)
            return

        if len(password) < 6:
            self.error_label.setText("Password must be at least 6 characters long!")
            self.error_label.setVisible(True)
            return

        if password != confirm_password:
            self.error_label.setText("Passwords do not match!")
            self.error_label.setVisible(True)
            return

        # Pass the data to the controller
        self.controller.handle_create_account(password, fullname, email, phone_number)

    def clear_error_message(self):
        # Hide the error message when the user starts typing again
        self.error_label.setVisible(False)

    def validate_email(self, email):
        # Basic email validation using regular expression
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    def validate_phone(self, phone):
        # Israeli phone number validation (must start with '05', '07', '03' and be 10 digits)
        pattern = r'^(05\d{8}|07\d{8}|03\d{7})$'
        return re.match(pattern, phone) is not None
    
    def show_error(self, message):
        # הצגת הודעת שגיאה
       self.error_label.setText(message)
       self.error_label.setVisible(True)
