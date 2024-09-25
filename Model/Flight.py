class Flight:
    def __init__(self, flight_id, airplane_id, departure_city, departure_airport, departure_country, 
                 arrival_city, arrival_airport, arrival_country, departure_date_time, arrival_date_time, 
                 price, is_sabbath_landing=None, available_seats=None):
        self.flight_id = flight_id
        self.airplane_id = airplane_id
        self.departure_city = departure_city
        self.departure_airport = departure_airport
        self.departure_country = departure_country
        self.arrival_city = arrival_city
        self.arrival_airport = arrival_airport
        self.arrival_country = arrival_country
        self.departure_date_time = departure_date_time
        self.arrival_date_time = arrival_date_time
        self.price = price  # הוספת שדה המחיר
        self.is_sabbath_landing = is_sabbath_landing
        self.available_seats = available_seats

    def __repr__(self):
        return (f"Flight(ID={self.flight_id}, AirplaneID={self.airplane_id}, Departure='{self.departure_city}', "
                f"Arrival='{self.arrival_city}', DepartureTime={self.departure_date_time}, "
                f"ArrivalTime={self.arrival_date_time}, Price=${self.price})")  # הצגת המחיר ב-__repr__
