class Gave:
    def __init__(self, beskrivelse, giver):
        self.beskrivelse = beskrivelse
        self.giver = giver
    
    def __str__(self):
        return self.giver + " ga deg " + self.beskrivelse