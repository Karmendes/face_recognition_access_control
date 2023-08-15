
from abc import ABC,abstractmethod

class FaceRecognitor(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def recognize_face(self,frame):
        pass