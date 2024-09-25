# Model/Airplane.py

class Airplane:
    def __init__(self, manufacturer, nickname, year_of_manufacture, image_url, seat_count, airplane_id=0):
        self.airplane_id = airplane_id  # הגדרת ברירת מחדל ל-0
        self.manufacturer = manufacturer
        self.nickname = nickname
        self.year_of_manufacture = year_of_manufacture
        self.image_url = image_url
        self.seat_count = seat_count

    def __repr__(self):
        return (f"Airplane(ID={self.airplane_id}, Manufacturer={self.manufacturer}, "
                f"Nickname={self.nickname}, Year={self.year_of_manufacture}, "
                f"Seats={self.seat_count}, ImageURL={self.image_url})")
