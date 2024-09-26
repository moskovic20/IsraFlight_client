# TicketModel.py

import requests
from Model.Ticket import Ticket

class TicketModel:
    def __init__(self):
        self.base_url = "http://localhost:5034/api/Ticket"  # יש לעדכן לכתובת ה-API שלך

    def get_all_tickets(self):
        response = requests.get(self.base_url)
        if response.status_code == 200:
            tickets_data = response.json()
            tickets = [Ticket(
                ticket_id=ticket['ticketId'],
                flight_id=ticket['flightId'],
                customer_id=ticket['customerId'],
                purchase_date=ticket['purchaseDate']
            ) for ticket in tickets_data]
            return tickets
        else:
            raise Exception(f"Failed to get tickets: {response.status_code}")

    def get_ticket_by_id(self, ticket_id):
        url = f"{self.base_url}/{ticket_id}"
        response = requests.get(url)
        if response.status_code == 200:
            ticket_data = response.json()
            return Ticket(
                ticket_id=ticket_data['ticketId'],
                flight_id=ticket_data['flightId'],
                customer_id=ticket_data['customerId'],
                purchase_date=ticket_data['purchaseDate']
            )
        else:
            raise Exception(f"Failed to get ticket: {response.status_code}")

    def create_ticket(self, flight_id, customer_id, purchase_date):
        new_ticket = {
            "flightId": flight_id,
            "customerId": customer_id,
            "purchaseDate": purchase_date
        }
        response = requests.post(self.base_url, json=new_ticket)
        if response.status_code == 201:
            ticket_data = response.json()
            return "Order confirmed, have a nice flight!"
        else:
            raise Exception(f"Failed to create ticket: {response.status_code}")

    def delete_ticket(self, ticket_id):
        url = f"{self.base_url}/{ticket_id}"
        response = requests.delete(url)
        if response.status_code == 204:
            return True
        else:
            return f"Failed to delete ticket: {response.status_code}"
            
    # פונקציה חדשה להחזרת כרטיסים לפי customerId
    def get_tickets_by_customer_id(self, customer_id):
        url = f"{self.base_url}/customer/{customer_id}"
        response = requests.get(url)
        if response.status_code == 200:
            tickets_data = response.json()
            tickets = [Ticket(
                ticket_id=ticket['ticketId'],
                flight_id=ticket['flightId'],
                customer_id=ticket['customerId'],
                purchase_date=ticket['purchaseDate']
            ) for ticket in tickets_data]
            return tickets
        elif response.status_code==404:
            return []
        else:
            raise Exception(f"Failed to get tickets for customer {customer_id}: {response.status_code}")
