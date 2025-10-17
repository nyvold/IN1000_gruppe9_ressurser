class Onskeliste:
    def __init__(self):
        self.onsker = []
    
    def finn(self, beskrivelse):
        for onske in self.onsker:
            if onske.hent_beskrivelse().lower() == beskrivelse.lower():
                return onske
        print("fant iKke ØnSke :(")

    def fjern(self, beskrivelse):
        for onske in self.onsker:
            if onske.hent_beskrivelse().lower() == beskrivelse.lower():
                self.onsker.remove(onske)      
        print("fant iKke ØnSke :(") 

