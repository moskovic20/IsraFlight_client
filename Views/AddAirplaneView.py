from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy, QMessageBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class AddAirplaneView(QWidget):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.setWindowTitle('Add Airplane')
        self.setGeometry(100, 100, 800, 600)

        # Main Layout with spacers on both sides
        main_layout = QHBoxLayout()

        # Add spacers to the left and right of the form
        left_spacer = QSpacerItem(50, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        right_spacer = QSpacerItem(50, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Form Layout (all elements stacked vertically)
        form_layout = QVBoxLayout()
        form_layout.setSpacing(10)  # Spacing between form elements
        form_layout.setAlignment(Qt.AlignCenter)

        # Add spacer above all elements
        top_spacer = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Expanding)
        form_layout.addSpacerItem(top_spacer)

        # Manufacturer Input
        manufacturer_label = QLabel("Manufacturer:")
        self.manufacturer_input = QLineEdit()
        self.manufacturer_input.setStyleSheet(self.text_input_style())
        form_layout.addWidget(manufacturer_label)
        form_layout.addWidget(self.manufacturer_input)

        # Nickname Input
        nickname_label = QLabel("Airplane Nickname:")
        self.nickname_input = QLineEdit()
        self.nickname_input.setStyleSheet(self.text_input_style())
        form_layout.addWidget(nickname_label)
        form_layout.addWidget(self.nickname_input)

        # Year of Manufacture Input
        year_label = QLabel("Year of Manufacture:")
        self.year_input = QLineEdit()
        self.year_input.setStyleSheet(self.text_input_style())
        form_layout.addWidget(year_label)
        form_layout.addWidget(self.year_input)

        # Seat Count Input
        seat_count_label = QLabel("Seat Count:")
        self.seat_count_input = QLineEdit()
        self.seat_count_input.setStyleSheet(self.text_input_style())
        form_layout.addWidget(seat_count_label)
        form_layout.addWidget(self.seat_count_input)

        # Image URL Input
        image_url_label = QLabel("Image URL:")
        self.image_url_input = QLineEdit()
        self.image_url_input.setStyleSheet(self.text_input_style())
        form_layout.addWidget(image_url_label)
        form_layout.addWidget(self.image_url_input)

        # Error message (hidden initially)
        self.error_label = QLabel("All fields must be filled, including an image URL!")
        self.error_label.setStyleSheet("color: red; font-size: 14px;")
        self.error_label.setVisible(False)
        form_layout.addWidget(self.error_label)

        # Submit Button
        submit_button = QPushButton("Add Airplane")
        submit_button.setFixedHeight(50)
        submit_button.setFixedWidth(200)
        submit_button.setStyleSheet(self.submit_button_style())
        submit_button.clicked.connect(self.add_airplane)
        form_layout.addWidget(submit_button, alignment=Qt.AlignCenter)

        # Add spacer below all elements
        bottom_spacer = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Expanding)
        form_layout.addSpacerItem(bottom_spacer)

        # Add spacers and form layout to main layout
        main_layout.addSpacerItem(left_spacer)
        main_layout.addLayout(form_layout)
        main_layout.addSpacerItem(right_spacer)

        # Set the main layout
        self.setLayout(main_layout)

        # Connect inputs to clear error message when user starts typing or loads an image
        self.manufacturer_input.textChanged.connect(self.hide_error_message)
        self.nickname_input.textChanged.connect(self.hide_error_message)
        self.year_input.textChanged.connect(self.hide_error_message)
        self.seat_count_input.textChanged.connect(self.hide_error_message)
        self.image_url_input.textChanged.connect(self.hide_error_message)

    def text_input_style(self):
        # Modern style for QLineEdit inputs
        return """
        QLineEdit {
            border: 2px solid #007bff;
            border-radius: 10px;
            padding: 8px;
            font-size: 16px;
            background-color: #f0f0f0;
        }
        QLineEdit:focus {
            border: 2px solid #0056b3;
            background-color: #e6f7ff;
        }
        """

    def submit_button_style(self):
        # Modern style for the Submit button (larger and more present)
        return """
        QPushButton {
            background-color: #28a745;
            color: white;
            font-size: 18px;
            font-weight: bold;
            border-radius: 25px;
            padding: 10px 20px;
        }
        QPushButton:hover {
            background-color: #218838;
        }
        """

    def add_airplane(self):
        # Call controller function to add airplane
        manufacturer = self.manufacturer_input.text()
        nickname = self.nickname_input.text()
        year_of_manufacture = self.year_input.text()
        seat_count = self.seat_count_input.text()
        image_url = self.image_url_input.text()

        # Example validation for empty fields and image URL
        if not manufacturer or not nickname or not year_of_manufacture or not seat_count or not image_url:
            self.error_label.setVisible(True)  # Show error message if fields or image URL are missing
        else:
            self.error_label.setVisible(False)  # Hide error message
            # Call the controller function to add the airplane
            self.controller.add_airplane(manufacturer, nickname, year_of_manufacture, seat_count, image_url)

    def hide_error_message(self):
        # Hide the error message when user starts typing
        self.error_label.setVisible(False)
