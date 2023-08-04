from battery import Battery
from dateutil.relativedelta import *

class spindlerBattery(Battery):

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        if relativedelta(self.current_date, self.last_service_date).years > 2:
            return True
        else:
            return False
    