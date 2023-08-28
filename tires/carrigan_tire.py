from tires import car_Tires

class carriganTire(car_Tires):

    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
        self.tire_needs_service = 0.9

    def needs_service(self):
        wear = self.tire_wear
        for tire in wear:
            if tire >= self.tire_needs_service:
                return True

        return False
