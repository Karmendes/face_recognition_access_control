from abc import ABC,abstractmethod

class PersonSearcher(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def search(self,encodings,know_encodings):
        pass