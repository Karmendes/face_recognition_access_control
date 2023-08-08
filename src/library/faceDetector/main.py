
from abc import ABC,abstractmethod

class FaceDetector(ABC):
    def __init__(self):
        pass
    def load_model(self):
        pass
    def detect_face(self,frame):
        pass