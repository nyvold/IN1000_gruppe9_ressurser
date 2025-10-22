class Vogn:
    def __init__(self, navn):
        self.navn = navn
        self.neste = None
        self.innhold = []
    
    def __str__(self):
        return f"{self.navn}"
    
