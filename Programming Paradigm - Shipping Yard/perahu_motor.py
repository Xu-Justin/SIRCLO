from perahu import Perahu

class PerahuMotor(Perahu):
    
    cost_per_motor = 2000
    
    def __init__(self, owner: str, number_of_motor: int):
        super().__init__(owner)
        self.number_of_motor = number_of_motor
        
    def set_number_of_motor(self, number_of_motor: int):
        self.number_of_motor = number_of_motor
    
    def get_number_of_motor(self):
        return self.number_of_motor
    
    # overriding abstract method
    def get_cost(self):
        return self.number_of_motor * self.cost_per_motor
    
    # overriding
    @staticmethod
    def horn():
        print("brm brmmmm")