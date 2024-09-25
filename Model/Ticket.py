class Ticket:
    def __init__(self, ticket_id, flight_id, customer_id, purchase_date):
        self.ticket_id = ticket_id
        self.flight_id = flight_id
        self.customer_id = customer_id
        self.purchase_date = purchase_date

    def __repr__(self):
        return (f"Ticket(ID={self.ticket_id}, FlightID={self.flight_id}, CustomerID={self.customer_id}, "
                f"PurchaseDate={self.purchase_date})")
