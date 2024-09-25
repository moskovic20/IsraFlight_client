# Controllers/AddAirplaneController.py
class AddAirplaneController:
    def __init__(self, model):
        self.model = model  


    def add_airplane(self, manufacturer, nickname, year_of_manufacture, seat_count, image_url):

        new_airplane = {
            'manufacturer': manufacturer,
            'nickname': nickname,
            'year_of_manufacture': year_of_manufacture,
            'seat_count': seat_count,
            'image_url': image_url
        }

        self.model.create_airplane(new_airplane)
