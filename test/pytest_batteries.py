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
    last_service_date = current_date - relativedelta(years=4)
    battery = nubbinBattery(last_service_date, current_date)
    assert battery.needs_service() == False, "Should be False"

def test_spindler_battery():
    #>2 years
    current_date = datetime.today().date()
    last_service_date = current_date - relativedelta(years=2)
    battery = spindlerBattery(last_service_date, current_date)
    assert battery.needs_service() == False, "Should be false"

test_nubbin_battery()
test_spindler_battery()
print("Tests completed successfully")
