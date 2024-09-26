# FlightDetailsController.py
from Views.FlightDetailsWindow import FlightDetailsWindow

class FlightDetailsController:
    def __init__(self, flight):
        self.flight = flight

    def show_window(self):
        self.flight_details_window = FlightDetailsWindow(self.flight)
        self.flight_details_window.show()
