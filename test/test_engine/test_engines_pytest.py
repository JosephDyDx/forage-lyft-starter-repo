'''
import part to test
create function and class to test part
create parameters and assign their values
pass values to imported part (class)
assert using unittest
'''

from engine.willoughby_engine import willoughbyEngine
from engine.sternman_engine import sternmanEngine
from engine.capulet_engine import capuletEngine

#driver code 
def test_willoughby_engine():
        #>60,000 criteria
        current_mileage = 61000
        last_service_mileage = 0
        engine = willoughbyEngine(current_mileage, last_service_mileage)
        assert engine.needs_service() ==  True, "should be True"

def test_willoughby_engine_False_case():
        #<60,000 criteria
        current_mileage = 50000
        last_service_mileage = 0
        engine = willoughbyEngine(current_mileage, last_service_mileage)
        assert engine.needs_service() ==  False, "should be False"

def test_sternman_engine():
        #True criteria
        warning_light_is_on = True
        engine = sternmanEngine(warning_light_is_on)
        assert engine.needs_service() ==  True, "should be True"

def test_sternman_engine_False_case():
        #False criteria
        warning_light_is_on = False
        engine = sternmanEngine(warning_light_is_on)
        assert engine.needs_service() ==  False, "should be False"

def test_capulet_engine():
        #>30,000 criteria
        current_mileage = 31000
        last_service_mileage = 0
        engine = capuletEngine(current_mileage, last_service_mileage)
        assert engine.needs_service() ==  True, "should be True"

def test_capulet_engine_False_case():
        #<30,000 criteria
        current_mileage = 20000
        last_service_mileage = 0
        engine = capuletEngine(current_mileage, last_service_mileage)
        assert engine.needs_service() ==  False, "should be false"

test_willoughby_engine()
test_willoughby_engine_False_case()
test_sternman_engine()
test_sternman_engine_False_case()
test_capulet_engine()
test_capulet_engine_False_case()
print("Test completed sucessfully")

