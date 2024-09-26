from Views.FlightDetailsWindow import FlightDetailsWindow
from PySide6.QtWidgets import QWidget
from Model.TicketModel import TicketModel

class FlightDetailsController:
    def __init__(self, flight,customer):
        self.flight = flight
        self.flight_details_window = None  # שמירת חלון פרטי הטיסה בזיכרון
        self.customer=customer
        self.ticker_Model=TicketModel()
        
    def show_window(self):
        self.flight_details_window = FlightDetailsWindow(self.flight,self)
        self.flight_details_window.raise_()
        self.flight_details_window.show()
        
    def create_ticket(self, flight_id, purchase_date):
        
        return self.ticker_Model.create_ticket( flight_id, self.customer.customer_id, purchase_date)
