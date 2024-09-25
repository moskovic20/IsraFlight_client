from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt
import os

class SingInWindow(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle('User Login')
        self.setGeometry(100, 100, 400, 500)  # Adjusted for a taller window

        # Set background color to white
        self.setStyleSheet("background-color: white;")

        # Path to images folder
        images_path = os.path.join(os.path.dirname(__file__), '..', 'Images')

        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)

        # Profile Image
        profile_image = QLabel()
        user_icon_path = os.path.join(images_path, 'user_icon.png')  # Path to user_icon image
        profile_pixmap = QPixmap(user_icon_path)
        profile_image.setPixmap(profile_pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        profile_image.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(profile_image)

        # Spacer - Small gap between profile image and username input
        main_layout.addItem(QSpacerItem(20, 10, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Username Input
        username_layout = QHBoxLayout()
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText('EMAIL')
        self.username_input.setFixedHeight(40)
        self.username_input.setStyleSheet("""
            border: 2px solid #000; 
            border-radius: 20px; 
            background-color: #f0f0f0; 
            padding-left: 15px;
        """)
        username_layout.addWidget(self.username_input)
        main_layout.addLayout(username_layout)

        # חיבור סיגנל textChanged לפונקציה שמנקה את הודעת השגיאה
        self.username_input.textChanged.connect(self.clear_error_message)

        # Spacer - Small gap between username and password input
        main_layout.addItem(QSpacerItem(20, 10, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Password Input
        password_layout = QHBoxLayout()
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText('PASSWORD')
        self.password_input.setFixedHeight(40)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("""
            border: 2px solid #000; 
            border-radius: 20px; 
            background-color: #f0f0f0; 
            padding-left: 15px;
        """)
        password_layout.addWidget(self.password_input)
        main_layout.addLayout(password_layout)

        # חיבור סיגנל textChanged לפונקציה שמנקה את הודעת השגיאה
        self.password_input.textChanged.connect(self.clear_error_message)

        # Spacer - Small gap between password input and login button
        main_layout.addItem(QSpacerItem(20, 15, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Login Button
        self.login_button = QPushButton('LOGIN')
        self.login_button.setFixedHeight(40)
        self.login_button.setStyleSheet("""
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
        main_layout.addWidget(self.login_button)
        self.login_button.clicked.connect(self.log_in_click)  # Connect the signal to the slot

        # Spacer - Small gap between login button and error message
        main_layout.addItem(QSpacerItem(20, 10, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Error Message Label (hidden by default)
        self.error_label = QLabel('')
        self.error_label.setAlignment(Qt.AlignCenter)
        self.error_label.setStyleSheet("color: red;")
        self.error_label.setVisible(False)  # Hidden by default
        main_layout.addWidget(self.error_label)

        # Spacer - Small gap between error message and forgot password
        main_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Forgot Password
        forgot_password = QLabel('FORGET YOUR PASSWORD?\nCLICK HERE')
        forgot_password.setFont(QFont('Arial', 10))
        forgot_password.setAlignment(Qt.AlignCenter)
        forgot_password.setStyleSheet("color: black;")
        main_layout.addWidget(forgot_password)

        # Spacer - Medium gap between forgot password and logo
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

    def log_in_click(self):
        # Retrieve the username and password
        username = self.username_input.text()
        password = self.password_input.text()
        self.controller.handle_login(username, password)

    def show_error_message(self, message):
        # Display the error message
        self.error_label.setText(message)
        self.error_label.setVisible(True)  # Show the error label

    def clear_error_message(self):
        # Clear the error message when the user starts typing
        self.error_label.setVisible(False)  # Hide the error label
