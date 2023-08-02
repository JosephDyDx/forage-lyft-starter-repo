#import all objects carfactory is associated with
from car import Car
from engine.capulet_engine import capuletEngine
from engine.sternman_engine import sternmanEngine
from engine.willoughby_engine import willoughbyEngine
from battery.nubbin_Battery import nubbinBattery
from battery.spindler_Battery import spindlerBattery

class caFactory:

    @staticmethod
    def create_Calliope(current_date,last_service_date, current_mileage, last_service_mileage):
        engine = capuletEngine(current_mileage, last_service_mileage)
        battery = spindlerBattery(last_service_date, current_date)
        car = (engine, battery)
        return car
        
    #calliope created

    @staticmethod
    def create_Glissade(current_date,last_service_date, current_mileage, last_service_mileage):
        engine = willoughbyEngine(current_mileage, last_service_mileage)
        battery = spindlerBattery(last_service_date, current_date)
        car = (engine, battery)
        return car
        
    #glissade created

    @staticmethod
    def create_pallindrome(current_date,last_service_date,warning_light_is_on):
        engine = sternmanEngine(warning_light_is_on)
        battery = spindlerBattery(last_service_date, current_date)
        car = (engine, battery)
        return car
        #pallindrome created

    @staticmethod
    def create_Rorschach(current_date,last_service_date, current_mileage, last_service_mileage):
        engine = willoughbyEngine(current_mileage, last_service_mileage)
        battery = nubbinBattery(last_service_date, current_date)
        car = (engine, battery)
        return car
        #rorschach created

    @staticmethod
    def create_Thovex(current_date,last_service_date, current_mileage, last_service_mileage):
        engine = capuletEngine(current_mileage, last_service_mileage)
        battery = nubbinBattery(last_service_date, current_date)
        car = (engine, battery)
        return car
        #thovex created


