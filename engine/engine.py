from abc import ABC, abstractmethod

#abstract class. interface for engine
class engine(ABC):
    
    
    #abstract method
    @abstractmethod
    def needs_service():
        pass
