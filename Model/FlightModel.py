import requests
from Model.Flight import Flight
from datetime import datetime

class FlightModel:
    def __init__(self):
        self.base_url = "http://localhost:5034/api/Flight"  # יש לעדכן לכתובת ה-API שלך

    # פונקציה ליצירת אובייקט טיסה מתוך נתוני JSON
    def _create_flight_from_data(self, flight_data):
        return Flight(
            flight_id=flight_data['flightId'],
            airplane_id=flight_data['airplaneId'],
            departure_city=flight_data['departureCity'],
            departure_airport=flight_data['departureAirport'],
            departure_country=flight_data['departureCountry'],
            arrival_city=flight_data['arrivalCity'],
            arrival_airport=flight_data['arrivalAirport'],
            arrival_country=flight_data['arrivalCountry'],
            departure_date_time=datetime.fromisoformat(flight_data['departureDateTime']),  # המרת תאריך
            arrival_date_time=datetime.fromisoformat(flight_data['arrivalDateTime']),  # המרת תאריך
            price=flight_data['price'],  # הוספת שדה המחיר
            is_sabbath_landing=flight_data.get('isSabbathLanding'),
            available_seats=flight_data.get('availableSeats')
        )

    # בקשה לקבלת כל הטיסות ממוין לפי תאריך המראה
    def get_all_flights(self):
        response = requests.get(self.base_url)
        if response.status_code == 200:
            flights_data = response.json()
            flights = [self._create_flight_from_data(flight) for flight in flights_data]
            # מיון הטיסות לפי תאריך ההמראה
            return sorted(flights, key=lambda flight: flight.departure_date_time)
        else:
            raise Exception(f"Failed to get flights: {response.status_code}")

    # בקשה לקבלת טיסות זמינות ממוין לפי תאריך המראה
    def get_available_flights(self):
        url = f"{self.base_url}/available-flights"
        response = requests.get(url)
        if response.status_code == 200:
            flights_data = response.json()
            flights = [self._create_flight_from_data(flight) for flight in flights_data]
            # מיון הטיסות לפי תאריך ההמראה
            return sorted(flights, key=lambda flight: flight.departure_date_time)
        elif response.status_code == 404:
            return []
        else:
            raise Exception(f"Failed to get available flights: {response.status_code}")

    # בקשה לפי מוצא ממוין לפי תאריך המראה
    def get_flights_by_origin(self, origin_city, origin_country):
        params = {
            "city": origin_city,
            "country": origin_country
        }
        url = f"{self.base_url}/by-origin"
        response = requests.get(url, params=params)
        if response.status_code == 200:
            flights_data = response.json()
            flights = [self._create_flight_from_data(flight) for flight in flights_data]
            # מיון הטיסות לפי תאריך ההמראה
            return sorted(flights, key=lambda flight: flight.departure_date_time)
        elif response.status_code == 404:
            return []
        else:
            raise Exception(f"Failed to get flights by origin: {response.status_code}")

    # בקשה לפי יעד ממוין לפי תאריך המראה
    def get_flights_by_destination(self, destination_city, destination_country):
        params = {
            "city": destination_city,
            "country": destination_country
        }
        url = f"{self.base_url}/by-destination"
        response = requests.get(url, params=params)
        if response.status_code == 200:
            flights_data = response.json()
            flights = [self._create_flight_from_data(flight) for flight in flights_data]
            # מיון הטיסות לפי תאריך ההמראה
            return sorted(flights, key=lambda flight: flight.departure_date_time)
        elif response.status_code == 404:
            return []
        else:
            raise Exception(f"Failed to get flights by destination: {response.status_code}")

    # בקשה לפי מוצא ויעד ממוין לפי תאריך המראה
    def get_flights_by_origin_and_destination(self, origin_city, origin_country, destination_city, destination_country):
        params = {
            "originCity": origin_city,
            "originCountry": origin_country,
            "destinationCity": destination_city,
            "destinationCountry": destination_country
        }
        url = f"{self.base_url}/by-origin-destination"
        response = requests.get(url, params=params)
        if response.status_code == 200:
            flights_data = response.json()
            flights = [self._create_flight_from_data(flight) for flight in flights_data]
            # מיון הטיסות לפי תאריך ההמראה
            return sorted(flights, key=lambda flight: flight.departure_date_time)
        elif response.status_code == 404:
            return []
        else:
            raise Exception(f"Failed to get flights by origin and destination: {response.status_code}")

    # פונקציה לקבלת רשימת מוצא ייחודית ממוין לפי סדר האלף-בית
    def get_all_origins(self):
        flights = self.get_all_flights()
        origins = list(set(f"{flight.departure_city}, {flight.departure_country}" for flight in flights))
        # מיון המוצאים לפי סדר האלף-בית
        return sorted(origins)

    # פונקציה לקבלת רשימת יעד ייחודית ממוין לפי סדר האלף-בית
    def get_all_destinations(self):
        flights = self.get_all_flights()
        destinations = list(set(f"{flight.arrival_city}, {flight.arrival_country}" for flight in flights))
        # מיון היעדים לפי סדר האלף-בית
        return sorted(destinations)
    
    def add_flight(self, flight_data):
        response = requests.post(self.base_url, json=flight_data)

        if response.status_code == 201:  # בדיקת הצלחה (201 Created)
            print("Flight added successfully!")
            return self._create_flight_from_data(response.json())  
        elif response.status_code == 400:
            return "SHABBAT_LANDING_NOT_ALLOWED"
        else:
                # טיפול בשגיאות אחרות
            return f"Failed to add flight:"

    

        # בקשה לקבלת כל מספרי המטוסים
    def get_all_airplane_ids(self):
        url = f"{self.base_url}/airplane-ids"
        response = requests.get(url)
        if response.status_code == 200:
            airplane_ids = response.json()  # נניח שהתגובה היא JSON עם רשימת מספרי המטוסים
            return airplane_ids
        elif response.status_code == 404:
            return []
        else:
            raise Exception(f"Failed to get airplane IDs: {response.status_code}, {response.text}")
        
    # פונקציה לקבלת טיסה לפי מספר טיסה
    def get_flight_by_id(self, flight_id):
        url = f"{self.base_url}/{flight_id}"
        response = requests.get(url)
        if response.status_code == 200:
            flight_data = response.json()
            return self._create_flight_from_data(flight_data)
        elif response.status_code == 404:
            print(f"Flight with ID {flight_id} not found.")
            return None
        else:
            raise Exception(f"Failed to get flight by ID: {response.status_code}, {response.text}")
