from perahu import Perahu

class PerahuLayar(Perahu):
    
    cost_per_sail = 500
    
    def __init__(self, owner: str, number_of_sail: int):
        super().__init__(owner)
        self.number_of_sail = number_of_sail
        
    def set_number_of_sail(self, number_of_sail: int):
        self.number_of_sail = number_of_sail
    
    def get_number_of_sail(self):
        return self.number_of_sail
    
    # overriding abstract method
    def get_cost(self):
        return self.number_of_sail * self.cost_per_sail