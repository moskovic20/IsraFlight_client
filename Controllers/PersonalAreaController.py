class PersonalAreaController:
    def __init__(self, flightM,ticketM,airplaneM,customer):
        self.customer=customer
        self.flight_m=flightM
        self.ticket_m=ticketM
        self.airplane_m=airplaneM

    def get_user_name(self):
        return self.customer.full_name
    
    def get_user_email(self):
        return self.customer.email
    
    def get_user_phone(self):
        return self.customer.phone_number
    
    def get_user_tickets(self):
        return self.ticket_m.get_tickets_by_customer_id(self.customer.customer_id)
    
    def printPDF(self,ticket):
        print(ticket)