from tires import car_Tires

class octoprimeTire(car_Tires):

    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
        self.tire_needs_service = 3

    def needs_service(self):
        if sum(self.tire_wear) >= self.tire_needs_service:
            return True
        else:
            return False
