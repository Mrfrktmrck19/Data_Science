### For Loops

numbers = [1,2,3,4,5,6,7,8,9]
i = 0
for number in numbers:
    print(f"index {i}, değer: {number}")
    i+=1


names = ["Ömer","Faruk","Ahmet","Atilla","Onur","Umut"]
for name in names:
    print(f"name: {name}")


name = "Ömer Faruk Tomurcuk"
for char in name:
    print(char)

tuple = (1,2,3,4,5,6)
for t in tuple:
    print(t)

tuple2 = ((1,2,3),(4,5,6),(7,8,9),(10,11,12),(13,14,15))
for t in tuple2:
    print(t)

for t,p,l in tuple2:
    print(t," ",p," ",l)


dictionary = {"k1":1, "k2":2, "k3":3}
for item in dictionary:
    print(item) ##key gelecek, value değil

for key,value in dictionary.items():
    print(key,value) ## dictionary grubu gelecek. key ve value'yi ayrı ayrı da bastırabilirsin