class Abonnent: 
    def __init__(self, abonnentnavn, preferanser):
        self.abonnentnavn = abonnentnavn
        self.preferanser = preferanser
        self._påbegynte_serier = {} #<string, int>

    def hent_preferanser(self):
        return self.preferanser
    
    def sjekk_om_sett(self, serienavn):
        return serienavn in self._påbegynte_serier
    
    def se_en_episode(self, serienavn):
        if self.sjekk_om_sett(serienavn):
            self._påbegynte_serier[serienavn] += 1
        else:
            self._påbegynte_serier[serienavn] = 1

class Serie:
    def __init__(self, serienavn):
        self.serienavn = serienavn
        self.episoder = {} #<int, list>
        self.tags_i_serien = {} #<string, int>
        self._les_fra_fil()

    def _les_fra_fil(self):
        filnavn = self.serienavn + ".txt"
        with open(filnavn, "r") as fil:
            episode = 1
            
            for linje in fil:
                # 1. oppdatere self.episoder
                tags = linje.strip().split()
                self.episoder[episode] = tags
                episode += 1

                # 2. oppdatere self.tags_i_serien
                for tag in tags:
                    if tag in self.tags_i_serien:
                        self.tags_i_serien[tag] += 1
                    else:
                        self.tags_i_serien[tag] = 1
                
    def hent_serietags(self):
        return list(self.tags_i_serien.keys())

class Tjeneste:
    def __init__(self, serienavn_liste):
        self.serier = {} #<serienavn, Serie-objekt>
        self.tjeneste_tags = []
        self.abonnenter = {} #<abonnentnavn, Abonnent-objekt>
        self._oppdater_tjeneste(serienavn_liste)

    def _oppdater_tjeneste(self, serienavn_liste):
        for serienavn in serienavn_liste:
            ny_serie = Serie(serienavn)
            self.serier[serienavn] = ny_serie

            for tag in self.serier[serienavn].hent_serietags():
                 self.tjeneste_tags.append(tag)

    def ny_abonnent(self):
        navn = input("Skriv ditt navn:")
        preferanser = {}

        for tag in self.tjeneste_tags:
            preferanse = input(f"Hva er din preferanse til {tag} fra -1 til 1, (0 nøytral)")# enten 1, 0 eller -1

            while preferanse > 1 or preferanse < -1:
                print("Ugyldig input, prøv igjen")
                preferanse = input(f"Hva er din preferanse til {tag} fra -1 til 1, (0 nøytral)")# enten 1, 0 eller -1
            
            if preferanse == 0:
                continue

            preferanser[tag] = preferanse
        
        ny_abonnent = Abonnent(navn, preferanser)
        self.abonnenter[navn] = ny_abonnent
