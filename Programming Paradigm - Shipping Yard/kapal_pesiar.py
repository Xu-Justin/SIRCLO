from perahu import Perahu

class KapalPesiar(Perahu):
    
    cost_captain = 5000
    cost_per_crew = 1000
    
    def __init__(self, owner: str, captain: str, number_of_crew: int):
        super().__init__(owner)
        self.captain = captain
        self.number_of_crew = number_of_crew
        
    def set_captain(self, captain: str):
        self.captain = captain
        
    def get_captain(self):
        return self.captain
    
    def set_number_of_crew(self, number_of_crew: int):
        self.number_of_crew = number_of_crew
    
    def get_number_of_crew(self):
        return self.number_of_crew
    
    # overriding abstract method
    def get_cost(self):
        return self.cost_captain + self.number_of_crew * self.cost_per_crew
    
    # overriding
    @staticmethod
    def horn():
        print("prut prut prutttt")