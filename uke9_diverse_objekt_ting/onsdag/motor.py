class Motor:
    def __init__(self, kraft, km_stand, drivstoff):
        self.kraft = kraft
        self.km_stand = km_stand
        self.drivstoff = drivstoff

    def __str__(self):
        return f"Motor: (kraft = {self.kraft}, km stand = {self.km_stand}, drivstoff type = {self.drivstoff})"
    
    def __repr__(self):
        return f"Motor({self.kraft}, {self.km_stand}, {self.drivstoff})"
    
