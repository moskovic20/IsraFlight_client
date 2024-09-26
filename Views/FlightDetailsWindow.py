from PySide6.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QMessageBox
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from Model.Ticket import Ticket
from datetime import datetime




class FlightDetailsWindow(QMainWindow):
    def __init__(self, flight,controller, parent=None):
        super().__init__(parent)
        self.controller=controller
        self.setWindowTitle(" ")
        self.setFixedSize(900, 500)
        self.flight=flight
        

        # יצירת widget מרכזי עבור החלון
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # סגנון כללי של החלון עם תמונת רקע
        self.setStyleSheet("""
    QMainWindow {
        background-image: url('Images/flightWindow.png');
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
    }
    QLabel {
        color: white;
    }
    QPushButton {
        background-color: rgba(255, 255, 255, 0.7);
        color: #336B79;
        border-radius: 15px;
        font-size: 15px;
        font-family: "Helvetica";
        font-weight: bold;
        border: none;
        padding: 10px 20px;
    }
    QPushButton:hover { /* שינוי הצבע בעת מעבר עם העכבר */
        background-color: rgba(51, 107, 121, 0.9); /* שינוי צבע הכפתור */
        color: white; /* שינוי צבע הטקסט */
    }
""")


        # הגדרות גופן לכותרות ולתוכן
        
        header_font = QFont("Arial", 16, QFont.Bold)  # תוכן טיפה יותר גדול
        content_font = QFont("Arial", 14, )  # תוכן טיפה יותר גדול

        # תוויות פרטי טיסה כלליים
        flight_id_label = QLabel(f"Flight number: {flight.flight_id}")
        flight_id_label.setFont(header_font)

        available_seats_label = QLabel(f"Available Seats: {flight.available_seats}")
        available_seats_label.setFont(header_font)

        # כפתור תשלום - ממוקם בצד ימין למעלה
        payment_button = QPushButton("order now ->")
        payment_button.setFixedSize(205, 40)
        payment_button.clicked.connect(self.create_ticket)


        # פרטי ההמראה והנחיתה
        departure_label = QLabel("Takeoff:")
        arrival_label = QLabel("Landing:")
        departure_label.setFont(header_font)
        arrival_label.setFont(header_font)

        # פרטי ההמראה
        departure_country_label = QLabel(f"Country: {flight.departure_country}")
        departure_city_label = QLabel(f"City: {flight.departure_city}")
        departure_airport_label = QLabel(f"Airport: {flight.departure_airport}")
        departure_time_label = QLabel(f"Time: {flight.departure_date_time}")

        # פרטי הנחיתה
        arrival_country_label = QLabel(f"Country: {flight.arrival_country}")
        arrival_city_label = QLabel(f"City: {flight.arrival_city}")
        arrival_airport_label = QLabel(f"Airport: {flight.arrival_airport}")
        arrival_time_label = QLabel(f"Time: {flight.arrival_date_time}")

        # פריסת כותרות ההמראה
        departure_title_layout = QHBoxLayout()
        departure_title_layout.addWidget(departure_label)
        departure_title_layout.setContentsMargins(50, 0, 50, 0)

        # פריסת פרטי ההמראה
        departure_layout = QHBoxLayout()
        departure_layout.addWidget(departure_country_label)
        departure_layout.addWidget(departure_city_label)
        departure_layout.addWidget(departure_airport_label)
        departure_layout.addWidget(departure_time_label)
        departure_layout.setContentsMargins(50, 0, 50, 0)

        # פריסת כותרות הנחיתה
        arrival_title_layout = QHBoxLayout()
        arrival_title_layout.addWidget(arrival_label)
        arrival_title_layout.setContentsMargins(50, 0, 50, 0)

        # פריסת פרטי הנחיתה
        arrival_layout = QHBoxLayout()
        arrival_layout.addWidget(arrival_country_label)
        arrival_layout.addWidget(arrival_city_label)
        arrival_layout.addWidget(arrival_airport_label)
        arrival_layout.addWidget(arrival_time_label)
        arrival_layout.setContentsMargins(50, 0, 50, 0)

        available_seats_label.setFont(content_font)
        departure_country_label.setFont(content_font)
        departure_city_label.setFont(content_font)
        departure_airport_label.setFont(content_font)
        departure_time_label.setFont(content_font)
        arrival_country_label.setFont(content_font)
        arrival_city_label.setFont(content_font)
        arrival_airport_label.setFont(content_font)
        arrival_time_label.setFont(content_font)
        
        
        # פריסת הפרטים הראשית
        main_layout = QVBoxLayout(central_widget)

        # פריסת Flight ID וכפתור תשלום בשורה אחת
        flight_info_layout = QHBoxLayout()
        flight_info_layout.addWidget(flight_id_label)
        flight_info_layout.addStretch()
        flight_info_layout.addWidget(payment_button)

        main_layout.addLayout(flight_info_layout)
        main_layout.addWidget(available_seats_label)
        main_layout.addSpacing(15)
        main_layout.addLayout(departure_title_layout)
        main_layout.addLayout(departure_layout)
        main_layout.addSpacing(15)
        main_layout.addLayout(arrival_title_layout)
        main_layout.addLayout(arrival_layout)
        main_layout.addSpacing(20)

        # הצגת תוית על שעת הנחיתה בשבת (אם קיים תנאי כזה)
        if not flight.is_sabbath_landing:
            shabbat_label = QLabel("*This flight does not land on Shabbat")
            shabbat_label.setStyleSheet("color: #FFFFFF; font-style: italic;")
            main_layout.addWidget(shabbat_label, alignment=Qt.AlignCenter)

    def create_ticket(self):
        try:
            message = self.controller.create_ticket(self.flight.flight_id, datetime.now().isoformat())

            # הצגת ההודעה בחלון QMessageBox
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(message)
            msg_box.setWindowTitle("message")
            msg_box.exec()

        except Exception as e:
            # הצגת שגיאה אם הייתה בעיה ביצירת הכרטיס
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText(f"Failed to create the ticket: {str(e)}")
            msg_box.setWindowTitle("Error")
            msg_box.exec()