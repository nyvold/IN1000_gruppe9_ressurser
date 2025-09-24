
def nest_storste(liste):
    # lager bedre forutsetninger / gjør problemet enklere
    settet = set(liste)
    sortert = sorted(settet)
    # løser faktisk problemet
    element = sortert[len(sortert)-2]
    return element

liste = [4, 6, 3, 7, 8, 7, 9, 9]
print(nest_storste(liste))

