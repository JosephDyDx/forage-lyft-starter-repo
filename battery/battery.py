from abc import ABC, abstractmethod

#abstract class. interface for battery
class Battery(ABC):
    
    #abstract method
    @abstractmethod
    def needs_service():
        pass
