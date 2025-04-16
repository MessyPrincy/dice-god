import random

class Die:
    def __init__(self, sides: int, type_: str):
        self.sides = sides
        self.type = type_

    def roll(self) -> int:
        return random.randint(1, self.sides)
    
    def __repr__(self):
        return f"{self.type.title()} d{self.sides}"
    

class Problem:
    def __init__(self, name, type_required, min_total):
        self.name = name
        self.type = type_required
        self.min_total = min_total
    
    def is_solved(self, assigned_rolls):
        total = sum(assigned_rolls)
        return total >= self.min_total
    
    def __repr__(self):
        return f"{self.name} (Need {self.type} dice, total ≥ {self.min_total})"