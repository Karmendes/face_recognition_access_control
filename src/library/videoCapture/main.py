from abc import ABC,abstractmethod

class VideoCaptor(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def capture(self):
        pass