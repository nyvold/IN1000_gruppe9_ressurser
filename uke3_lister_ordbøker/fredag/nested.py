studenter = [
    ["Henning", [4, 3, 3]],
    ["Halvor", [4, 3, 5]],
    ["Martin", [5, 5, 2]]
]

# 1
karakterer = studenter[0][1]
print(karakterer)

# 2
karakter = studenter[1][1][0]
print(karakter)

# 3
indre_liste = studenter[2][1]
snitt = sum(indre_liste) / len(indre_liste)
print(snitt)