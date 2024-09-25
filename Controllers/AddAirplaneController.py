# Controllers/AddAirplaneController.py
class AddAirplaneController:
    def __init__(self, model):
        self.model = model  


    def add_airplane(self, manufacturer, nickname, year_of_manufacture, seat_count, image_url):

        new_airplane = {
            'Manufacturer': manufacturer,
            'Nickname': nickname,
            'YearOfManufacture': year_of_manufacture,
            'SeatCount': seat_count,
            'ImageUrl': image_url
        }

        return self.model.create_airplane(new_airplane)


        
