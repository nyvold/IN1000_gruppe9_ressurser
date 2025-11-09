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
            