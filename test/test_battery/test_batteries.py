'''
import part to test
create function and class to test part
create parameters and assign their values
pass values to imported part (class)
assert using unittest
'''

from ..battery.spindler_Battery import spindlerBattery
from ..battery.nubbin_Battery import nubbinBattery
from datetime import datetime
import unittest
from dateutil.relativedelta import *

class test_spindler_battery(unittest.TestCase):
    def test_spindler(self):
        #>2 years
        current_date = datetime.today().date()
        last_service_date = current_date - relativedelta(years=3)
        battery = spindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service(), "Should be True")
    
    def test_spindler_False_case(self):
        #<2 years
        current_date = datetime.today().date()
        last_service_date = current_date - relativedelta(years=1)
        battery = spindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service(), "Should be False")
        
class test_nubbin_battery(unittest.TestCase):
    def test_nubbin(self):
        #>4 years
        current_date = datetime.today().date()
        last_service_date = current_date - relativedelta(years=5)
        battery = nubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service(), "Should be True")
    
    def test_nubbin_False_case(self):
        #<4 years
        current_date = datetime.today().date()
        last_service_date = current_date - relativedelta(years=3)
        battery = nubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service(), "Should be False")

if __name__ == "__main__":
    unittest.main()
