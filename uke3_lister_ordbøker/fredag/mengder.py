# 1
ord1 = "Programmering"
ord2 = "Python"

ord1 = set(ord1)
ord2 = set(ord2)

felles_bokstaver = ord1.intersection(ord2)
# eller
felles_bokstaver = ord1 & ord2 # & = AND

print(felles_bokstaver)

# 2
list = [3, 4, 5, 1, 2, 1, 4, 7, 8, 6, 7, 9, 11]
list = set(list)
ant_unike_tall = len(list)
print(ant_unike_tall)