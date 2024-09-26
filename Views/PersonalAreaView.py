from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView
from PySide6.QtCore import Qt


class PersonalAreaView(QWidget):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.setWindowTitle('Personal Area')
        self.setGeometry(100, 100, 800, 600)
        self.init_ui()

    def init_ui(self):
        # פריסה כללית של העמוד
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)

        # יצירת מלבן עם צבע רקע תכלת לפרטי המשתמש והכפתור
        user_info_box = QWidget()
        user_info_box.setStyleSheet("background-color: #e0f7fa; border-radius: 10px; padding: 20px; margin-top: 10px;")
        user_info_layout = QVBoxLayout()
        user_info_layout.setAlignment(Qt.AlignCenter)

        # כותרת מעל שורת הפרטים והכפתור
        title_label = QLabel("Personal Details")
        title_label.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 10px;")
        user_info_layout.addWidget(title_label, alignment=Qt.AlignCenter)

        # פריסה אופקית לפרטי המשתמש וכפתור העריכה
        user_details_layout = QHBoxLayout()
        user_details_layout.setSpacing(20)

        # הוספת שדות למידע האישי, מסודרים אחד ליד השני
        self.name_label = QLabel(f"Name: {self.controller.get_user_name()}")
        self.name_label.setStyleSheet("font-size: 14px; padding: 5px;")
        self.email_label = QLabel(f"Email: {self.controller.get_user_email()}")
        self.email_label.setStyleSheet("font-size: 14px; padding: 5px;")
        self.phone_label = QLabel(f"Phone: {self.controller.get_user_phone()}")
        self.phone_label.setStyleSheet("font-size: 14px; padding: 5px;")

        # הוספת פרטי המשתמש אחד ליד השני
        user_details_layout.addWidget(self.name_label, alignment=Qt.AlignLeft)
        user_details_layout.addWidget(self.email_label, alignment=Qt.AlignLeft)
        user_details_layout.addWidget(self.phone_label, alignment=Qt.AlignLeft)

        # הוספת מרווח בין פרטי המשתמש לכפתור העריכה
        user_details_layout.addStretch()

       # הוספת כפתור לעריכת המידע האישי באותה השורה
        self.edit_button = QPushButton("Edit Information")
        self.edit_button.setStyleSheet("""
            QPushButton {
                padding: 5px 10px;
                font-size: 11px;
                background-color: #28a745;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)
        self.edit_button.setFixedSize(150, 40)  # קביעת גודל הכפתור

        # הוספת הכפתור למיקום המתאים בפריסה
        user_details_layout.addWidget(self.edit_button, alignment=Qt.AlignRight)

        # הוספת הפריסה האופקית לתוך הפריסה האנכית
        user_info_layout.addLayout(user_details_layout)

        # הוספת הפריסה האנכית לתוך המלבן
        user_info_box.setLayout(user_info_layout)

        # הוספת הקופסה לפריסה הכללית
        main_layout.addWidget(user_info_box)

        # הפרדה בין חלק עליון ותחתון
        main_layout.addSpacing(20)

        # כותרת לרשימת הכרטיסים
        tickets_title_label = QLabel("Your Tickets")
        tickets_title_label.setStyleSheet("font-size: 18px; font-weight: bold; padding: 10px;")
        tickets_title_label.setAlignment(Qt.AlignCenter)  # מרכוז הכותרת ברוחב העמוד
        main_layout.addWidget(tickets_title_label, alignment=Qt.AlignCenter)

        # הודעה במידה ואין כרטיסים
        self.no_tickets_label = QLabel("No tickets to display")
        self.no_tickets_label.setStyleSheet("color: red; font-size: 16px;")
        self.no_tickets_label.setVisible(False)  # ההודעה מוסתרת בהתחלה
        main_layout.addWidget(self.no_tickets_label)

        # יצירת פריסת קופסה שתמרכז את הטבלה
        table_layout = QHBoxLayout()
        table_layout.setAlignment(Qt.AlignCenter)

        # יצירת טבלה להצגת הכרטיסים
        self.tickets_table = QTableWidget()
        self.tickets_table.setColumnCount(4)
        self.tickets_table.setHorizontalHeaderLabels(["Ticket Number", "Flight Number", "Purchase Date", "Print PDF"])
        self.tickets_table.setEditTriggers(QTableWidget.NoEditTriggers)  # מניעת עריכה ישירה של התאים

        # עיצוב הטבלה עם צבעי רקע
        self.tickets_table.setStyleSheet("""
            QTableWidget {
                background-color: #f0f8ff;  /* צבע רקע כללי לטבלה */
                gridline-color: #d3d3d3;
            }
            QHeaderView::section {
                background-color: #007bff;  /* צבע רקע לכותרות */
                color: white;
                font-weight: bold;
                padding: 4px;
                border: 1px solid #d3d3d3;
            }
            QTableWidget::item {
                padding: 5px;
            }
        """)

        # שימוש ב- QHeaderView לתיקון הבעיה
        self.tickets_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.tickets_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.tickets_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.tickets_table.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.tickets_table.setFixedWidth(800)  # שינוי הרוחב של הטבלה

        # הסתרת המספור של השורות בטבלה
        self.tickets_table.verticalHeader().setVisible(False)

        # קביעת גובה קבוע לכל שורה בטבלה
        row_height = 50  # גובה השורה שנקבע
        self.tickets_table.verticalHeader().setDefaultSectionSize(row_height)

        # הבאת נתוני הכרטיסים מהבקר והצגתם בטבלה
        tickets = self.controller.get_user_tickets()

        if not tickets:
            # אם אין כרטיסים, נציג את ההודעה
            self.no_tickets_label.setVisible(True)
            self.tickets_table.setVisible(False)  # נסתיר את הטבלה אם אין כרטיסים
        else:
            # אם יש כרטיסים, נציג אותם בטבלה
            self.no_tickets_label.setVisible(False)
            self.tickets_table.setVisible(True)
            self.tickets_table.setRowCount(len(tickets))

            for row, ticket in enumerate(tickets):
                ticket_number_item = QTableWidgetItem(str(ticket.ticket_id))
                flight_number_item = QTableWidgetItem(str(ticket.flight_id))
                purchase_date_item = QTableWidgetItem(ticket.purchase_date)
                self.tickets_table.setItem(row, 0, ticket_number_item)
                self.tickets_table.setItem(row, 1, flight_number_item)
                self.tickets_table.setItem(row, 2, purchase_date_item)

                # יצירת כפתור הדפסת PDF לכל כרטיס
                print_pdf_button = QPushButton("Print PDF")
                print_pdf_button.setStyleSheet("""
                     QPushButton {
                        padding: 5px 10px;
                        font-size: 11px;
                        background-color: #28a745;
                        color: white;
                        font-weight: bold;
                        border-radius: 5px;
                    }
                    QPushButton:hover {
                        background-color: #218838;
                    }
                """)
                print_pdf_button.setFixedSize(100, 30)  # קביעת גודל הכפתור
                # קישור הפונקציה לבקר כך שהכפתור יידע איזה כרטיס לשלוח לשרת
                print_pdf_button.clicked.connect(lambda checked, t=ticket: self.controller.printPDF(t))


                # יצירת פריסה אופקית למרכוז הכפתור בתא
                button_layout = QHBoxLayout()
                button_layout.addStretch()  # הוספת מרווח משמאל
                button_layout.addWidget(print_pdf_button, alignment=Qt.AlignCenter)
                button_layout.addStretch()  # הוספת מרווח מימין

                # יצירת קופסה עבור התא כדי להוסיף את הפריסה
                button_widget = QWidget()
                button_widget.setLayout(button_layout)

                # הוספת הקופסה עם הכפתור לתא
                self.tickets_table.setCellWidget(row, 3, button_widget)

        # הוספת הטבלה לפריסה המרכזית
        table_layout.addWidget(self.tickets_table)
        main_layout.addLayout(table_layout)

        # הגדרת הפריסה לעמוד
        self.setLayout(main_layout)

    def button_style(self):
        return """
        QPushButton {
            background-color: #28a745;
            color: white;
            font-size: 14px;
            font-weight: bold;
            border-radius: 10px;
            padding: 10px;
        }
        QPushButton:hover {
            background-color: #218838;
        }
        """
