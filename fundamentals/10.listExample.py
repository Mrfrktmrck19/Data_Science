from os import name
from unittest import result


names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]

# 1-  "Cenk" ismini listenin sonuna ekleyiniz.
names.append("Cenk")

# 2-  "Sena" değerini listenin başına ekleyiniz.
names.insert(0,"Sena")

# 3-  "Deniz" ismini listeden siliniz.
print(names)
names.remove("Deniz")   
print(names)


# ya da deniz değerinin indexini bulup sileceksin
# index = names.index("Deniz")
# print(names)
# names.pop(index)
# print(names)


# 4-  "Yağmur" isminin indeksi nedir ?
index = names.index("Yağmur")
print(index)

# 5-  "Ali" listenin bir elemanı mıdır ?
result = "Ali" in names
print(result)

# 6-  Liste elemanlarını ters çevirin.
print(names[::-1])

# 7-  Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()
print(names)

# 8-  years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()
print(years)

# 9-  str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
str = "Chevrolet,Dacia"
car_list = str.split(",")
print(car_list)

# 10- years dizisinin en büyük ve en küçük elemanı nedir ?
print(min(years))
print(max(years))

# 11- years dizisinde kaç tane 1998 değeri vardır ?
print(years.count(1998))

# 12- years dizisinin tüm elemanlarını siliniz.
years.clear()

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
brands = []
brand = input("Marka:")
brands.append(brand)

brand = input("Marka:")
brands.append(brand)

brand = input("Marka:")
brands.append(brand)

print(brands)