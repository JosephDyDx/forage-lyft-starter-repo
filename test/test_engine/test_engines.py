'''
import part to test
create function and class to test part
create parameters and assign their values
pass values to imported part (class)
assert using unittest
method names must start with test
'''

from engine.willoughby_engine import willoughbyEngine
from engine.sternman_engine import sternmanEngine
from engine.capulet_engine import capuletEngine

import unittest

#driver code 
class test_willoughby_engine(unittest.TestCase):
    def test_willoughby(self):
        #>60,000 criteria
        current_mileage = 61000
        last_service_mileage = 0
        engine = willoughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service(), "Should be True")

    def test_willoughby_False_case(self):
        #<60,000 criteria
        current_mileage = 50000
        last_service_mileage = 0
        engine = willoughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service(), "Should be False")

class test_sternman_engine(unittest.TestCase):
    def test_sternman(self):
        #warning light : True 
        warning_light_is_on = True
        engine = sternmanEngine(warning_light_is_on)
        self.assertTrue(battery.needs_service(), "should be True")
    
    def test_sternman_False_case(self):
        #warning light : False
        warning_light_is_on = False
        engine = sternmanEngine(warning_light_is_on)
        self.assertTrue(battery.needs_service(), "should be false")

class test_capulet_engine(unittest.TestCase):
    def test_capulet(self):
        #>30,000 criteria
        current_mileage = 31000
        last_service_mileage = 0
        engine = capuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service(), "should be True")

    def test_capulet_False_case(self):
        #<30,000 criteria
        current_mileage = 20000
        last_service_mileage = 0
        engine = capuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service(), "should be false")

if __name__ == "__main__":
    unittest.main()
