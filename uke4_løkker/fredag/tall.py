tall = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lengde = []
# fruits = ["banan", "eple", "pære", "aprikos", "fruktsalat"]
# for fruit in fruits:
#     lengde.append(len(fruit))
# print(lengde)
nums = []
inp = input("Skriv inn et tall (0 for stopp): ")
while inp != "0":
    nums.append(int(inp))
    inp = input("Skriv inn et tall (0 for stopp): ")
print("Sum:")
print(sum(nums))
