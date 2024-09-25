from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QWidget, QLabel
from PySide6.QtCore import Qt

class HomeWindow(QMainWindow):

    def __init__(self, Controller):
        super(HomeWindow, self).__init__()
        self.controller = Controller  # Store reference to the controller

        self.setWindowTitle("IsraFlight")

        # Create SIGN IN button
        self.signIn_button = QPushButton("SIGN IN")
        self.signIn_button.setEnabled(True)
        self.signIn_button.setFixedSize(200, 50)  # Fixed size
        self.signIn_button.setObjectName("logon_button")
        self.signIn_button.clicked.connect(self.controller.show_login_screen)  # Connect the signal to the slot

        # Create CREATE ACCOUNT button
        self.createAccount_button = QPushButton("CREATE ACCOUNT")
        self.createAccount_button.setEnabled(True)
        self.createAccount_button.setFixedSize(200, 50)  # Fixed size
        self.createAccount_button.setObjectName("create_account_button")
        self.createAccount_button.clicked.connect(self.controller.show_create_account_screen)  # Connect the signal to the slot

        # Style the buttons to ensure the background color is applied correctly
        button_style = """
            QPushButton {
                background-color: #007bff; 
                color: white; 
                font-weight: bold; 
                border-radius: 25px;  /* Increased border-radius for a more rounded look */
                border: none;
                padding: 10px 20px;  /* Added padding for a more balanced look */
                box-shadow: 0px 8px 15px rgba(0, 123, 255, 0.3);  /* Added shadow for depth */
            }
            QPushButton:hover {
                background-color: #0056b3;
                box-shadow: 0px 15px 20px rgba(0, 86, 179, 0.4);  /* Increased shadow on hover */
                transform: translateY(-3px);  /* Slight lift effect on hover */
            }
            QPushButton:pressed {
                background-color: #004085;
                transform: translateY(2px);  /* Slight press effect */
            }
        """
        self.signIn_button.setStyleSheet(button_style)
        self.createAccount_button.setStyleSheet(button_style)

        # Create label for the top text
        title_label = QLabel("WELCOME TO")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 36px; color: white; background: transparent;")

        # Create label for the main title text
        main_title_label = QLabel("IsraFlight")
        main_title_label.setAlignment(Qt.AlignCenter)
        main_title_label.setStyleSheet("font-size: 90px; color: white; font-weight: bold; background: transparent;")

        # Create label for the subtitle
        subtitle_label = QLabel("Your next vacation starts here")
        subtitle_label.setAlignment(Qt.AlignCenter)
        subtitle_label.setStyleSheet("font-size: 36px; color: white; background: transparent;")

        # Spacers
        top_spacer = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Minimum)  # Top spacer
        bottom_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)  # Spacer between text and buttons
        low_spacer = QSpacerItem(20, 155, QSizePolicy.Minimum, QSizePolicy.Minimum)  # Bottom spacer

        # Set layout for the buttons
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(20)  # Spacing between buttons
        buttons_layout.addWidget(self.signIn_button)
        buttons_layout.addWidget(self.createAccount_button)

        # Set layout for the window
        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(0, 0, 0, 0)

        # Add elements to the layout
        layout.addSpacerItem(top_spacer)  # Small top spacer
        layout.addWidget(title_label)
        layout.addWidget(main_title_label)
        layout.addWidget(subtitle_label)
        layout.addSpacerItem(bottom_spacer)  # Spacer before buttons
        layout.addLayout(buttons_layout)  # Add the buttons layout to the main layout
        layout.addSpacerItem(low_spacer)  # Bottom spacer

        # Create central widget and set the layout
        container = QWidget()
        container.setLayout(layout)

        # Set background image and button styles using CSS
        container.setStyleSheet("""
            QWidget {
                background-image: url('Images/IsraFl.png');
                background-position: center;
                background-repeat: no-repeat;
                background-size: cover;
            }
            QPushButton {
                background: none;  /* Ensure background image doesn't affect the buttons */
            }
        """)

        # Set the central widget of the window
        self.setCentralWidget(container)

        # Show the window maximized
        # self.showMaximized()
