'''
import part to test
create function and class to test part
create parameters and assign their values
pass values to imported part (class)
assert using unittest
'''

from ..willoughby_engine import willoughbyEngine
from ..sternman_engine import sternmanEngine
from ..capulet_engine import capuletEngine

#driver code 
def test_willoughby_engine():
        #60,000 criteria
        current_mileage = 100000
        last_service_mileage = 20000
        engine = willoughbyEngine(current_mileage, last_service_mileage)
        assert engine.needs_service() ==  True, "should be True"

def test_sternman_engine():
        #True criteria
        warning_light_is_on = True
        engine = sternmanEngine(warning_light_is_on)
        assert engine.needs_service() ==  True, "should be True"

def test_capulet_engine():
        #30,000 criteria
        current_mileage = 100000
        last_service_mileage = 80000
        engine = capuletEngine(current_mileage, last_service_mileage)
        assert engine.needs_service() ==  False, "should be false"

test_willoughby_engine()
test_sternman_engine()
test_capulet_engine()
print("Test completed sucessfully")

