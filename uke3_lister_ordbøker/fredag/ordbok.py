# 1
handleliste = {"melk":25, "brød":25, "ost":40}

melk_rabatt = handleliste["melk"] * 0.2
summen = sum(handleliste.values())

print(summen - melk_rabatt)