# 1
tall = [11, 5, 6, 7, 10, 13, 12, 4, 3]

storst = tall[0]
for element in tall:
    if element > storst:
        storst = element

print(storst)

# 2
fruits = ["banan", "eple", "pære", "aprikos", "fruktsalat"]
lengde = []
for fruit in fruits:
    lengde.append(len(fruit))
print(lengde)
