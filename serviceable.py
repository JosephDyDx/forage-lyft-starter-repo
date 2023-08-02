from abc import ABC, abstractmethod

#abstract class. interface for car
class Serviceable(ABC):
    
    #abstract method
    @abstractmethod
    def needs_service():
        pass
