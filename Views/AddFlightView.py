from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLineEdit, QPushButton, QLabel, QDateTimeEdit, QFormLayout, QSpacerItem, QSizePolicy, QMessageBox
from PySide6.QtCore import Qt, QDateTime
from datetime import timedelta  # הוספנו את timedelta כדי לטפל בהוספת שעות

class AddFlightView(QWidget):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.setWindowTitle('Add Flight')
        self.setGeometry(100, 100, 900, 600)
        self.init_ui()

    def init_ui(self):
        # Main layout with vertical spacers to control top and bottom margins
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(50, 50, 50, 50)  # רווח מצדדים ומהחלק העליון והתחתון

        # Add spacer at the top
        top_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addSpacerItem(top_spacer)

        # Form layouts for left and right columns
        form_layout_left = QFormLayout()
        form_layout_right = QFormLayout()

        # Set fixed width for all input fields for consistency
        input_width = 300

        # Right column elements (Departure details)
        self.airplane_combo = QComboBox()
        self.airplane_combo.addItem("")  # הוסף ערך ריק בתור ברירת מחדל
        self.airplane_combo.addItems([str(id) for id in self.controller.get_airplane_ids()])
        self.airplane_combo.setFixedWidth(input_width)
        self.airplane_combo.setStyleSheet(self.combo_box_style())  # עיצוב הקומבו-בוקס
        airplane_label = QLabel("Airplane ID:")
        form_layout_left.addRow(airplane_label, self.airplane_combo)

        self.departure_city_edit = QLineEdit()
        self.departure_city_edit.setFixedWidth(input_width)
        self.departure_city_edit.setStyleSheet(self.text_input_style())
        departure_city_label = QLabel("Departure City:")
        form_layout_left.addRow(departure_city_label, self.departure_city_edit)

        self.departure_airport_edit = QLineEdit()
        self.departure_airport_edit.setFixedWidth(input_width)
        self.departure_airport_edit.setStyleSheet(self.text_input_style())
        departure_airport_label = QLabel("Departure Airport:")
        form_layout_left.addRow(departure_airport_label, self.departure_airport_edit)

        self.departure_country_edit = QLineEdit()
        self.departure_country_edit.setFixedWidth(input_width)
        self.departure_country_edit.setStyleSheet(self.text_input_style())
        departure_country_label = QLabel("Departure Country:")
        form_layout_left.addRow(departure_country_label, self.departure_country_edit)

        # Updated QDateTimeEdit with no date range and display format
        self.departure_date_time_edit = QDateTimeEdit()
        self.departure_date_time_edit.setCalendarPopup(True)
        self.departure_date_time_edit.setFixedWidth(input_width)
        self.departure_date_time_edit.setStyleSheet(self.date_time_style())  # עיצוב שדות תאריך
        self.departure_date_time_edit.setDisplayFormat("dd/MM/yyyy HH:mm")  # פורמט תצוגה לתאריך
        self.departure_date_time_edit.setDateTime(QDateTime.currentDateTime())  # ברירת מחדל של התאריך
        departure_date_time_label = QLabel("Departure DateTime:")
        form_layout_left.addRow(departure_date_time_label, self.departure_date_time_edit)

        # Left column elements (Arrival details)
        self.arrival_city_edit = QLineEdit()
        self.arrival_city_edit.setFixedWidth(input_width)
        self.arrival_city_edit.setStyleSheet(self.text_input_style())
        arrival_city_label = QLabel("Arrival City:")
        form_layout_right.addRow(arrival_city_label, self.arrival_city_edit)

        self.arrival_airport_edit = QLineEdit()
        self.arrival_airport_edit.setFixedWidth(input_width)
        self.arrival_airport_edit.setStyleSheet(self.text_input_style())
        arrival_airport_label = QLabel("Arrival Airport:")
        form_layout_right.addRow(arrival_airport_label, self.arrival_airport_edit)

        self.arrival_country_edit = QLineEdit()
        self.arrival_country_edit.setFixedWidth(input_width)
        self.arrival_country_edit.setStyleSheet(self.text_input_style())
        arrival_country_label = QLabel("Arrival Country:")
        form_layout_right.addRow(arrival_country_label, self.arrival_country_edit)

        # Updated QDateTimeEdit with no date range and display format
        self.arrival_date_time_edit = QDateTimeEdit()
        self.arrival_date_time_edit.setCalendarPopup(True)
        self.arrival_date_time_edit.setFixedWidth(input_width)
        self.arrival_date_time_edit.setStyleSheet(self.date_time_style())  # עיצוב שדות תאריך
        self.arrival_date_time_edit.setDisplayFormat("dd/MM/yyyy HH:mm")  # פורמט תצוגה לתאריך
        self.arrival_date_time_edit.setDateTime(QDateTime.currentDateTime())  # ברירת מחדל של התאריך
        arrival_date_time_label = QLabel("Arrival DateTime:")
        form_layout_right.addRow(arrival_date_time_label, self.arrival_date_time_edit)

        self.price_edit = QLineEdit()
        self.price_edit.setFixedWidth(input_width)
        self.price_edit.setStyleSheet(self.text_input_style())
        price_label = QLabel("Price:")
        form_layout_right.addRow(price_label, self.price_edit)

        # Spacer between the columns
        middle_spacer = QSpacerItem(50, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        # Layout for the two columns and spacer
        hbox_layout = QHBoxLayout()
        hbox_layout.addLayout(form_layout_left)
        hbox_layout.addSpacerItem(middle_spacer)
        hbox_layout.addLayout(form_layout_right)

        # Add the hbox layout to the main layout
        main_layout.addLayout(hbox_layout)

        # Add a spacer between form and the button
        form_button_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addSpacerItem(form_button_spacer)

        # Submit button centered at the bottom
        self.add_flight_button = QPushButton("Add Flight")
        self.add_flight_button.setFixedHeight(50)
        self.add_flight_button.setFixedWidth(200)
        self.add_flight_button.setStyleSheet(self.submit_button_style())
        self.add_flight_button.clicked.connect(self.on_add_flight)

        # Add the button and spacer at the bottom
        main_layout.addWidget(self.add_flight_button, alignment=Qt.AlignCenter)

        # Add bottom spacer
        bottom_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addSpacerItem(bottom_spacer)

    def text_input_style(self):
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

    def combo_box_style(self):
        return """
        QComboBox {
            border: 2px solid #007bff;
            border-radius: 10px;
            padding: 8px;
            font-size: 16px;
            background-color: #f0f0f0;
        }
        QComboBox:focus {
            border: 2px solid #0056b3;
            background-color: #e6f7ff;
        }
        """

    def date_time_style(self):
        return """
        QDateTimeEdit {
            border: 2px solid #007bff;
            border-radius: 10px;
            padding: 8px;
            font-size: 16px;
            background-color: #f0f0f0;
        }
        QDateTimeEdit:focus {
            border: 2px solid #0056b3;
            background-color: #e6f7ff;
        }
        """

    def submit_button_style(self):
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

    def on_add_flight(self):
        airplane_id = self.airplane_combo.currentText()
        departure_city = self.departure_city_edit.text()
        departure_airport = self.departure_airport_edit.text()
        departure_country = self.departure_country_edit.text()
        arrival_city = self.arrival_city_edit.text()
        arrival_airport = self.arrival_airport_edit.text()
        arrival_country = self.arrival_country_edit.text()
        departure_date_time = self.departure_date_time_edit.dateTime().toPython()  # Convert to Python datetime
        arrival_date_time = self.arrival_date_time_edit.dateTime().toPython()  # Convert to Python datetime
        price = self.price_edit.text()

        # Validate inputs: Check if any field is empty
        if not (airplane_id and departure_city and departure_airport and departure_country and arrival_city and arrival_airport and arrival_country and departure_date_time and arrival_date_time and price):
            self.show_error_message("Please fill out all fields!")
            return

        # Validate logical constraints: departure date must be in the future, arrival must be at least 1 hour after departure
        current_time = QDateTime.currentDateTime().toPython()
        if departure_date_time <= current_time:
            self.show_error_message("Departure date must be in the future.")
            return

        # Use timedelta to add 1 hour
        if arrival_date_time <= departure_date_time + timedelta(hours=1):
            self.show_error_message("Arrival date must be at least 1 hour after the departure date.")
            return

        # All validation passed, process flight addition
        new_flight = self.controller.add_flight(airplane_id, departure_city, departure_airport, departure_country,
                                                arrival_city, arrival_airport, arrival_country, departure_date_time,
                                                arrival_date_time, float(price), None, None)
        
        if isinstance(new_flight, str):
            self.show_error_message(new_flight)
        else:
            self.show_error_message("flight number: "+f"{str(new_flight.flight_id)}")

        print(f"Added Flight: {new_flight}")

    def show_error_message(self, message):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Error")
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.exec()