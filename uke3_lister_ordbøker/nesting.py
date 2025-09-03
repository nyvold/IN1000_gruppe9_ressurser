# Liste inni liste, vi kan lage 2d space!

yttersteListe = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

var1 = yttersteListe[1] # [4, 5, 6]
var1 = var1[2] # 6
print(var1)

#eller
var2 = yttersteListe[1][2]
print(var2)



nestedDict = {1:["en", "to", "tre"], 2:["fire", "fem", "seks"], 3:["sju", "åtte", "ni"]}

seks = nestedDict[2][2]
print(seks)