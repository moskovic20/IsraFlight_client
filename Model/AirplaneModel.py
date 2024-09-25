# Model/AirplaneModel.py
import requests
from Model.Airplane import Airplane

class AirplaneModel:
    def __init__(self):
        self.base_url = "http://localhost:5034/api/Airplane"  # עדכן לכתובת ה-API שלך

    def get_all_airplanes(self):
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()  # טיפול בשגיאות
            airplanes_data = response.json()
            airplanes = [Airplane(
                airplane_id=airplane['airplaneId'],  # ה-ID שמתקבל מהשרת
                manufacturer=airplane['manufacturer'],
                nickname=airplane['nickname'],
                year_of_manufacture=airplane['yearOfManufacture'],
                image_url=airplane.get('imageUrl'),
                seat_count=airplane.get('seatCount', 0)
            ) for airplane in airplanes_data]
            return airplanes
        except requests.exceptions.RequestException as e:
            raise Exception(f"שגיאה בקבלת נתוני המטוסים: {str(e)}")

    def get_airplane_by_id(self, airplane_id):
        try:
            url = f"{self.base_url}/{airplane_id}"
            response = requests.get(url)
            response.raise_for_status()  # טיפול בשגיאות
            airplane_data = response.json()
            return Airplane(
                airplane_id=airplane_data['airplaneId'],  # ה-ID שמתקבל מהשרת
                manufacturer=airplane_data['manufacturer'],
                nickname=airplane_data['nickname'],
                year_of_manufacture=airplane_data['yearOfManufacture'],
                image_url=airplane_data.get('imageUrl'),
                seat_count=airplane_data.get('seatCount', 0)
            )
        except requests.exceptions.RequestException as e:
            raise Exception(f"שגיאה בקבלת מטוס לפי ID: {str(e)}")

    def create_airplane(self, new_airplane):
        
        try:
            response = requests.post(self.base_url, json=new_airplane)
            response.raise_for_status()
            airplane_data = response.json()
            return Airplane(
                airplane_id=airplane_data['airplaneId'],  # קבלת ה-ID מהשרת לאחר יצירה
                manufacturer=airplane_data['manufacturer'],
                nickname=airplane_data['nickname'],
                year_of_manufacture=airplane_data['yearOfManufacture'],
                image_url=airplane_data.get('imageUrl'),
                seat_count=airplane_data.get('seatCount', 0)
            )
        except requests.exceptions.RequestException as e:
            raise Exception(f"שגיאה ביצירת מטוס חדש: {str(e)}")
