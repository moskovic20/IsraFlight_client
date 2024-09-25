from Views.NewAccountWindow import NewAccountWindow
from Model.Customer import Customer 

class NewAccountController:
    def __init__(self, main_controller, customer_model):
        self.mainController = main_controller
        self.customerM = customer_model
        self.new_account_window = None  
    
    def show_window(self):
        if self.new_account_window:
            self.new_account_window.close()
        self.new_account_window = NewAccountWindow(self) 
        self.new_account_window.show() 
        return self.new_account_window
      


    def handle_create_account(self,password, fullname, email, phone_number):
        try:
            if self.customerM.is_email_exists(email):
                self.new_account_window.show_error("An account with this email already exists!")
                return
            
            new_customer = Customer(0,password=password, full_name=fullname, email=email,phone_number=phone_number)
            self.customerM.create_customer(new_customer)
            self.new_account_window.show_error("Account created successfully!")

        except Exception as e:
            self.new_account_window.show_error(f"An error occurred: {e}")
       
