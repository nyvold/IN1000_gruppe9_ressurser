class Fleet:
    def __init__(self, navn, id):
        self.navn = navn
        self.id = id
        self.cars = []
    
    def legg_til(self, car):
        self.cars.append(car)
    
    def __len__(self):
        return len(self.cars)
    
    def __str__(self):
        return f"{self.cars}"
    

f1 = Fleet("Volvo forhandler", 12)
print(f1)
