

def reverser(liste):
    ny_liste = []
    for indeks in range(len(liste), 0, -1):
        ny_liste.append(liste[indeks-1])
    return ny_liste


liste = ["en", "to", "tre", "fire", "fem"]
reversert = reverser(liste)
print(liste)
print(reversert)