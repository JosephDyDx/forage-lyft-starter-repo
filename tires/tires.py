from abc import ABC, abstractmethod

#abstract class. interface for engine
class car_Tires(ABC):
    
    #abstract method
    @abstractmethod
    def needs_service():
        pass
