from onske import Onske
class Onskeliste:
    def __init__(self):
        self.onsker = []

    def nytt_onske(self, beskrivelse, antall, min_pris):
        nytt = Onske(beskrivelse, antall, min_pris)
        for o in self.onsker:
            if o == nytt:
                if min_pris < o.hent_minpris():
                    self.onsker.remove(o)
                    self.onsker.append(nytt)
                    return
                return
        self.onsker.append(nytt)
    
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

