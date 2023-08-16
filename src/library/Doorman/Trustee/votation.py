
from library.Doorman.Trustee.main import Trustee

class VotationTrustee(Trustee):
    def __init__(self,size:int,threshold:float):
        self.size = size
        self.threshold = threshold
    def calculate_proportions(self,data:list):
        counter = {}
        total_names = len(data)
        
        for name in data:
            if name in counter:
                counter[name] += 1
            else:
                counter[name] = 1

        return {nome: ocorrencias / total_names for nome, ocorrencias in counter.items()}
    def apply_rule(self,data:list):
        if len(data) < self.size:
            return print('The size data is not enough')
        # Get proportions
        props = self.calculate_proportions(data)
        # Get the winner
        winner = max(props, key=props.get)
        # check rule
        return props[winner] > self.threshold


        

        

        
        