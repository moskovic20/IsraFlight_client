from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QLabel, QHBoxLayout, QFrame, QPushButton
from PySide6.QtGui import QFont, QPixmap
from Views.FlightSearchView import FlightSearchView  # ייבוא תצוגת חיפוש הטיסות
from Views.AddAirplaneView import AddAirplaneView  # ייבוא תצוגת הוספת הטיסות
from Views.AddFlightView import AddFlightView
from Views.PersonalAreaView import PersonalAreaView
import os


class UserWindow(QWidget):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # הודעת "ברוך הבא"
        welcome_message = f"Welcome, {self.controller.get_user_name()} !"
        welcome_label = QLabel(welcome_message)
        welcome_label.setFont(QFont('Arial', 20, QFont.Bold))  
        welcome_label.setStyleSheet("color: #333333; padding: 10px;")

        # יצירת אייקון משתמש
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Images', 'user_icon.png')
        user_icon_label = QLabel()
        if os.path.exists(icon_path):
            user_icon_pixmap = QPixmap(icon_path).scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            user_icon_label.setPixmap(user_icon_pixmap)
            user_icon_label.setStyleSheet("padding: 10px;")

        # סידור ההודעה והאייקון בפינה השמאלית העליונה
        welcome_layout = QHBoxLayout()
        welcome_layout.addWidget(user_icon_label)
        welcome_layout.addWidget(welcome_label)
        welcome_layout.addStretch()

        # יצירת מסגרת עבור הודעת "ברוך הבא"
        welcome_frame = QFrame()
        welcome_frame_layout = QVBoxLayout()
        welcome_frame_layout.addLayout(welcome_layout)
        welcome_frame.setLayout(welcome_frame_layout)

        # יצירת Tab Widget
        self.tab_widget = QTabWidget()

        # הוספת תצוגת חיפוש הטיסות לטאב "Flights"
        self.flight_search_view = FlightSearchView(self.controller.get_flight_search_controller(),self.controller.get_customer())
        self.tab_widget.addTab(self.flight_search_view, "Flights")

        # עמודים נוספים למשתמשים רגילים
        personal_area_page = QWidget()
        self.personal_view = PersonalAreaView(self.controller.get_personal_controller())
        self.tab_widget.addTab( self.personal_view, "Personal Area")

        todays_landings_page = QWidget()
        self.tab_widget.addTab(todays_landings_page, "Today's Landings")

        # בדיקה אם המשתמש הוא מנהל
        if self.controller.is_admin():
            # חיבור תצוגת הוספת טיסה
            self.add_airplane_view = AddAirplaneView(self.controller.get_add_airplane_controller())
            self.tab_widget.addTab(self.add_airplane_view, "Add Airplane")

            self.add_airplane_page =AddFlightView(self.controller.get_add_flight_controller())  
            self.tab_widget.addTab(self.add_airplane_page, "Add Flight")

        # הגדרת פריסה
        frame = QFrame()
        frame_layout = QVBoxLayout()
        frame_layout.addWidget(self.tab_widget)
        frame.setLayout(frame_layout)

        main_layout.addWidget(welcome_frame)
        main_layout.addWidget(frame)
        self.setLayout(main_layout)
        self.setWindowTitle("User Center")
