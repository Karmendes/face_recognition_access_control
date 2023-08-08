from abc import ABC,abstractmethod

class Trustee(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def apply_rule(self):
        pass
