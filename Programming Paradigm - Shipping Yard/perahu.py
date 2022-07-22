from abc import ABC, abstractmethod

class Perahu(ABC):
    
    def __init__(self, owner: str):
        self.owner = owner
        
    def set_owner(self, owner: str):
        self.owner = owner
    
    def get_owner(self):
        return self.owner    
    
    @abstractmethod
    def get_cost(self):
        pass
    
    @staticmethod
    def horn():
        print("default horn sound")