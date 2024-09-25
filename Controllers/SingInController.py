from Views.SingInWindow import SingInWindow
from Model.Customer import Customer 

class SingInController:
    def __init__(self, main_controller, customer_model):
        self.mainController = main_controller
        self.customerM = customer_model
        self.sing_in_window = SingInWindow(self)
        
    def show_window(self):
        if self.sing_in_window:
            self.sing_in_window.close()
        self.sing_in_window = SingInWindow(self)
        self.sing_in_window.show()
        return self.sing_in_window
    
    #פונקציה להתחברות משתמש
    def handle_login(self, email, password):
        try:
            myCustomer = self.customerM.get_customer_by_email(email)
            if myCustomer and myCustomer.password == password:
                print("Login successful")
                self.mainController.show_user_screen(myCustomer)
            else:
                self.show_error_message("The username or password is incorrect")
        except Exception as e:
            self.show_error_message(f"Login error: {e}")

    def show_error_message(self, message):
        self.sing_in_window.show_error_message(message)
