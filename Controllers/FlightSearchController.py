class FlightSearchController:
    def __init__(self, model):
        self.model = model
    
    def get_origins(self):
        return self.model.get_all_origins()
    
    def get_destinations(self):
        return self.model.get_all_destinations()
    
    def get_flights(self, origin, destination):
        # בדיקה מה נבחר ומפנה לפונקציה המתאימה במודל
        if origin != "All" and destination == "All":
            origin_city, origin_country = origin.split(", ")
            return self.model.get_flights_by_origin(origin_city, origin_country)

        elif destination != "All" and origin == "All":
            destination_city, destination_country = destination.split(", ")
            return self.model.get_flights_by_destination(destination_city, destination_country)

        elif origin != "All" and destination != "All":
            origin_city, origin_country = origin.split(", ")
            destination_city, destination_country = destination.split(", ")
            return self.model.get_flights_by_origin_and_destination(origin_city, origin_country, destination_city, destination_country)

        else:
            # אם גם המוצא וגם היעד הם "All", נקבל את כל הטיסות הזמינות
            return self.model.get_available_flights()
