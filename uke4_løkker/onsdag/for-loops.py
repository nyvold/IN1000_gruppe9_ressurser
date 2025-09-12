fruits = ["banan", "eple", "pære"]

for fruit in fruits:
    print(fruit)

print("---------------")

navn = {"Jonas":"Burger", "Ola":"Nordmann", "Kari":"Nordmann"}
for fornavn in navn.keys():
    print(fornavn)

print("---------------")

streng = "Denne setning."
# andre_bokstav = streng[6]
# print(andre_bokstav)
for bokstav in streng:
    print(bokstav)

print("---------------")

for nr in range(10):
    print(nr)