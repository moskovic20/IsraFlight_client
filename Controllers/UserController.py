from Controllers.AddAirplaneController import AddAirplaneController
from Controllers.FlightSearchController import FlightSearchController
from Controllers.AddFlightController import AddFlightController
from Controllers.PersonalAreaController import PersonalAreaController
from Views.UserWindow import UserWindow

class UserController:
    def __init__(self, main_controller, flight_M, airplane_M,ticket_M):
        self.customer = None
        self.main_controller = main_controller
        self.flightM = flight_M  
        self.airplaneM = airplane_M  # מודל המטוס
        self.ticketM=ticket_M
        self.flight_search_controller = None
        self.add_airplane_controller = None  # בקר להוספת מטוס
        self.add_flight_controller=None
        self.personal_controller=None

    def get_flight_search_controller(self):
        if not self.flight_search_controller:
            self.flight_search_controller = FlightSearchController(self.flightM)
        return self.flight_search_controller
    
    def get_personal_controller(self):
        if not self.personal_controller:
            self.personal_controller =PersonalAreaController(self.flightM,self.ticketM,self.airplaneM,self.customer)
        return self.personal_controller


    def get_add_airplane_controller(self):
        if not self.add_airplane_controller:
            self.add_airplane_controller = AddAirplaneController(self.airplaneM)
        return self.add_airplane_controller
    
    def get_add_flight_controller(self):
        if not self.add_flight_controller:
            self.add_flight_controller = AddFlightController(self.flightM,self.airplaneM)
        return self.add_flight_controller

    def get_user_name(self):
        return self.customer.full_name
    
    def show_window(self, my_customer):
        self.customer = my_customer
        self.user_window = UserWindow(self)
        self.user_window.showMaximized()

    def is_admin(self):
        # כאן תוכל להוסיף לוגיקה כדי לבדוק האם המשתמש הוא מנהל
        return self.customer.is_manager
