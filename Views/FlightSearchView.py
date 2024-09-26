from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QAbstractItemView, QHeaderView
from PySide6.QtCore import Qt
from datetime import datetime
from Controllers.FlightDetailsController import FlightDetailsController

class FlightSearchView(QWidget):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.init_ui()

    def init_ui(self):

        # Main layout
        main_layout = QVBoxLayout(self)

        # Search layout
        search_layout = QHBoxLayout()

        # Origin ComboBox
        self.origin_combo = QComboBox()
        self.origin_combo.addItem("All")  # Option for "all" or empty selection
        self.origin_combo.addItems(self.controller.get_origins())
        self.origin_combo.setStyleSheet("""
            padding: 8px;
            border: 2px solid #007bff;
            border-radius: 5px;
            background-color: #ffffff;
            font-size: 14px;
        """)
        origin_label = QLabel("Select Origin:")
        origin_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        search_layout.addWidget(origin_label)
        search_layout.addWidget(self.origin_combo)

        # Destination ComboBox
        self.destination_combo = QComboBox()
        self.destination_combo.addItem("All")  # Option for "all" or empty selection
        self.destination_combo.addItems(self.controller.get_destinations())
        self.destination_combo.setStyleSheet("""
            padding: 8px;
            border: 2px solid #007bff;
            border-radius: 5px;
            background-color: #ffffff;
            font-size: 14px;
        """)
        destination_label = QLabel("Select Destination:")
        destination_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        search_layout.addWidget(destination_label)
        search_layout.addWidget(self.destination_combo)

        # Search Button
        self.search_button = QPushButton('Find Flight')
        self.search_button.setStyleSheet("""
            QPushButton {
                padding: 10px 20px;
                background-color: #007bff;
                color: white;
                font-weight: bold;
                border-radius: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        search_layout.addWidget(self.search_button)
        self.search_button.clicked.connect(self.on_search_clicked)

        # Add search area to main layout
        main_layout.addLayout(search_layout)

        # Flights Table
        self.flights_table = QTableWidget()
        self.flights_table.setColumnCount(7)  # 7 columns including the "Book" button
        self.flights_table.setHorizontalHeaderLabels(['Flight ID', 'Origin', 'Destination', 'Departure Time', 'Arrival Time', 'Price', 'Book'])
        self.flights_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.flights_table.setStyleSheet("""
            QTableWidget {
                background-color: #f4f6f9;
                border: 1px solid #dcdcdc;
                border-radius: 5px;
                padding: 5px;
            }
            QTableWidget::item {
                padding: 10px;
            }
            QTableWidget::item:selected {
                background-color: #007bff;
                color: white;
            }
        """)
        # Hide row numbers
        self.flights_table.verticalHeader().setVisible(False)

        # Setting row height
        self.flights_table.verticalHeader().setDefaultSectionSize(45)  # Increase the height of each row

        main_layout.addWidget(self.flights_table)

        # Message for no flights
        self.no_flights_label = QLabel("No flights found.")
        self.no_flights_label.setAlignment(Qt.AlignCenter)
        self.no_flights_label.setStyleSheet("color: #f57c00; font-size: 16px;")
        self.no_flights_label.hide()
        main_layout.addWidget(self.no_flights_label)

        # Display all flights by default
        self.on_search_clicked()  # Call search function to load all flights initially

    def on_search_clicked(self):
         # Hide the message if visible
        self.no_flights_label.hide()

        # ריקון הטבלה לפני החיפוש החדש
        self.flights_table.setRowCount(0)

        # Get selected origin and destination
        origin = self.origin_combo.currentText()
        destination = self.destination_combo.currentText()

        # Fetch flights
        flights = self.controller.get_flights(origin, destination)

        if not flights:
            self.no_flights_label.setText("No flights found.")
            self.no_flights_label.show()
        else:
            # Populate the table
            self.flights_table.setRowCount(len(flights))
            for row, flight in enumerate(flights):
                self.flights_table.setItem(row, 0, QTableWidgetItem(f"{flight.flight_id}"))  # Flight ID
                self.flights_table.setItem(row, 1, QTableWidgetItem(f"{flight.departure_city}, {flight.departure_country}"))
                self.flights_table.setItem(row, 2, QTableWidgetItem(f"{flight.arrival_city}, {flight.arrival_country}"))

                # המרה למחרוזת של departure_date_time בפורמט מתאים
                departure_str = flight.departure_date_time.strftime('%Y-%m-%d   %H:%M')
                self.flights_table.setItem(row, 3, QTableWidgetItem(departure_str))

                # המרה למחרוזת של arrival_date_time בפורמט מתאים
                arrival_str = flight.arrival_date_time.strftime('%Y-%m-%d   %H:%M')
                self.flights_table.setItem(row, 4, QTableWidgetItem(arrival_str))

                self.flights_table.setItem(row, 5, QTableWidgetItem(f"$ {flight.price}"))

                # Book Button
                book_button = QPushButton('Details')
                book_button.setEnabled(True)
                book_button.setStyleSheet("""
                    QPushButton {
                        padding: 5px 10px;
                        font-size: 11px;
                        background-color: #28a745;
                        color: white;
                        font-weight: bold;
                        border-radius: 5px;
                    }
                """)
                # חיבור הכפתור לפונקציה שתפתח את חלון פרטי הטיסה
                book_button.clicked.connect(lambda checked, f=flight: self.open_flight_details(f))
                self.flights_table.setCellWidget(row, 6, book_button)

            # Adjust column sizes after populating the table
            self.adjust_table_columns()

    def adjust_table_columns(self):
        # Set fixed column widths for uniform look
        self.flights_table.setColumnWidth(0, 100)  # Flight ID
        self.flights_table.setColumnWidth(1, 150)  # Origin
        self.flights_table.setColumnWidth(2, 150)  # Destination
        self.flights_table.setColumnWidth(3, 150)  # Departure Time
        self.flights_table.setColumnWidth(4, 150)  # Arrival Time
        self.flights_table.setColumnWidth(5, 100)  # Price
        self.flights_table.setColumnWidth(6, 100)  # Book button

        # Ensure the table stretches properly across the entire width
        self.flights_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

      
    def open_flight_details(self, flight):
        flight_details_controller = FlightDetailsController(flight)
        flight_details_controller.show_window()  


