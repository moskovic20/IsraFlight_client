from Controllers.HomeController import HomeController
from Controllers.SingInController import SingInController
from Controllers.NewAccountController import NewAccountController
from Controllers.UserController import UserController

from Model.AirplaneModel import AirplaneModel
from Model.CustomerModel import CustomerModel
from Model.FlightModel import FlightModel
from Model.TicketModel import TicketModel




class MainController:
    def __init__(self):

         # יצירת כל המודלים פעם אחת
        self.airplane_model = AirplaneModel()
        self.customer_model = CustomerModel()
        self.flight_model = FlightModel()
        self.ticket_model = TicketModel()
        
        # יצירת בקרים אחרים
        self.home_controller = HomeController(self)
        self.sing_in_controller = SingInController(self,self.customer_model)
        self.new_account_controller= NewAccountController(self,self.customer_model)
        self.user_win_controller=UserController(self,self.flight_model,self.airplane_model,self.ticket_model)

    #הצגת מסך הבית
    def show_home_window(self):
        self.home_window=self.home_controller.show_window()

    #הצגת מסך התחברות
    def show_sing_in_window(self):
        self.singWindow = self.sing_in_controller.show_window()

    #הצגת מסך יצירת חשבון
    def show_creat_account(self):
        self.new_account=self.new_account_controller.show_window()

    #הצגת מסך משתמש
    def show_user_screen(self,customer):
      #  if self.singWindow:
      #      self.singWindow.close()
      #  if self.new_account:
      #      self.new_account.close()
    #    if self.home_window:
         #   self.home_window.close()
            self.user_screen=self.user_win_controller.show_window(customer)