'''
import part to test
create function and class to test part
create parameters and assign their values
pass values to imported part (class)
assert using unittest
'''

from ..spindler_Battery import spindlerBattery
from ..nubbin_Battery import nubbinBattery
from datetime import datetime
from dateutil.relativedelta import *

def test_nubbin_battery():
    #>4 years
    current_date = datetime.today().date()
    last_service_date = current_date - relativedelta(years=5)
    battery = nubbinBattery(last_service_date, current_date)
    assert battery.needs_service() == True, "Should be True"

def test_nubbin_False_case():
    #<4 years
    current_date = datetime.today().date()
    last_service_date = current_date - relativedelta(years=3)
    battery = nubbinBattery(last_service_date, current_date)
    assert battery.needs_service() == False, "Should be False"

def test_spindler_battery():
    #>2 years
    current_date = datetime.today().date()
    last_service_date = current_date - relativedelta(years=4)
    battery = spindlerBattery(last_service_date, current_date)
    assert battery.needs_service() == True, "Should be True"

def test_spindler_False_case():
    #<2 years
    current_date = datetime.today().date()
    last_service_date = current_date - relativedelta(years=1)
    battery = spindlerBattery(last_service_date, current_date)
    assert battery.needs_service() == False, "Should be False"

test_nubbin_battery()
test_spindler_battery()
test_nubbin_False_case()
test_spindler_False_case()
print("Tests completed successfully")

