'''
import part to test
create function and class to test part
create parameters and assign their values
pass values to imported part (class)
assert using unittest
'''


from tires.carrigan_tire import carriganTire
from tires.octoprime_tire import octoprimeTire

import unittest

class test_carrigan_tires(unittest.TestCase):
    def test_carrigan(self):
        # 1 sensor returns a value >=0.9
        tire_wear = [0,1,0.7,1]
        tire = carriganTire(tire_wear)
        self.assertTrue(tire.needs_service(), "Should be True")
    
    def test_carrigan_False_case(self):
        # all sensors returns a value <=0.9 
        tire_wear = [0.8,0.5,0.2,0.1]
        tire = carriganTire(tire_wear)
        self.assertTrue(tire.needs_service(), "Should be False")
        
class test_octoprime_tires(unittest.TestCase):
    def test_octoprime(self):
        #all sensors return values that collectively are >= 3
        tire_wear = [1,1,1,0.5]
        tire = octoprimeTire(tire_wear)
        self.assertTrue(tire.needs_service(), "Should be True")
    
    def test_octoprime_false_case(self):
        #all sensors return values that collectively are <= 3
        tire_wear = [0.1,0.5,0.2,0.0]
        tire = octoprimeTire(tire_wear)
        self.assertTrue(tire.needs_service(), "Should be False")

if __name__ == "__main__":
    unittest.main()
