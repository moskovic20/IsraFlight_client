from Model.Flight import Flight

class AddFlightController:
    def __init__(self, flight_M,airplane_M):
        self.airplaneM=airplane_M
        self.flightM=flight_M


    def get_airplane_ids(self):
        return self.flightM.get_all_airplane_ids()

    def add_flight(self, airplane_id, departure_city, departure_airport, departure_country, arrival_city, arrival_airport, 
               arrival_country, departure_date_time, arrival_date_time, price, is_sabbath_landing, available_seats):
        flight_data = {
            "flightId": 0,  # מזהה יוקצה על ידי השרת
            "airplaneId": airplane_id,
            "departureCity": departure_city,
            "departureAirport": departure_airport,
            "departureCountry": departure_country,
            "arrivalCity": arrival_city,
            "arrivalAirport": arrival_airport,
            "arrivalCountry": arrival_country,
            "departureDateTime": departure_date_time.isoformat(),  # המרת datetime ל-ISO
            "arrivalDateTime": arrival_date_time.isoformat(),      # המרת datetime ל-ISO
            "price": price,
            "isSabbathLanding": is_sabbath_landing,
            "availableSeats": available_seats
        }

        # שליחת נתוני ה-JSON ישירות למודל
        return self.flightM.add_flight(flight_data)


