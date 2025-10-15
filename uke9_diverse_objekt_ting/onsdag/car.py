from motor import Motor

class Car:
    def __init__(self, merke, vin, motor, farge):
        self.merke = merke
        self.vin = vin
        self.motor = motor
        self.farge = farge
    
    def __eq__(self, other):
        return self.merke == other.merke and self.farge == other.farge
    
    def __repr__(self):
        return f"{self.merke} med {self.motor}"

# m1 = Motor(250, 0, "Diesel")
# c1 = Car("BMW", 54321, m1, "blå")
# c2 = Car("BMW", 12345, m1, "blå")
# c3 = Car("BMW", 54321, m1, "rød")

# print(f"Farge og merke er det samme {c1 == c2}")
# print(f"id er samme: {c1 is c2}")
# print(f"Farge og merke er det samme {c1 == c3}")