from Views.FlightDetailsWindow import FlightDetailsWindow
from PySide6.QtWidgets import QWidget

class FlightDetailsController:
    def __init__(self, flight):
        self.flight = flight
        self.flight_details_window = None  # שמירת חלון פרטי הטיסה בזיכרון
        
    def show_window(self):
        self.flight_details_window = FlightDetailsWindow(self.flight)
        self.flight_details_window.raise_()
        self.flight_details_window.show()
        

