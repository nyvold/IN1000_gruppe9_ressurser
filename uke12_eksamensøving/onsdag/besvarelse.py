# Eksamen H24

# p1 -> person object.  <- p3
# p2 -> person object
# tall -> 0


# oppgave 3a
def jages(dyreliste):
    if "katt" in dyreliste and "mus" in dyreliste:
        return True
    
    if "katt" in dyreliste and "hund" in dyreliste:
        return True
    
    return False

# oppgave 3b

def utvidet_jages(dyreliste, jaging):
    for jager, jaget in jaging.items():
        if jager in dyreliste and jaget in dyreliste:
            return True
    return False
        


# oppgave 3c

def flertall(dyreliste):
    # return stringen i lista som finnes flest av
    # edgecase: hvis det er flere strings med max verdi, return "uavgjort"
    ordbok = {} # <dyr, antall ganger dyr finnes>
    storts_dyr = []
    for dyr in dyreliste:
        if dyr in ordbok:
            ordbok[dyr] += 1
        else:
            ordbok[dyr] = 1

    storts = max(ordbok.values())
    
    for dyr in ordbok:
        if ordbok[dyr] == storts:
            storts_dyr.append(dyr)
    
    if len(storts_dyr) >= 2:
        return "uavgjort"
    return storts_dyr[0]



# oppgave 5a
def felles(tall_lister):
    ordbok = {}
    resultat = []
    for liste in tall_lister:
        for tall in liste:
            if tall in ordbok:
                ordbok[tall] += 1
            else:
                ordbok[tall] = 1
    
    for tall, antall in ordbok.items():
        if antall > 1:
            resultat.append(tall)
    return resultat

