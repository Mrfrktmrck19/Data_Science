sayilar = [1,2,3,4,5,6,7,8,9]

#1- hangi sayılar 3'ün katıdır
liste = []
# c++'ciler aqlıyor
# index = 0
# for item in sayilar:
#     if sayilar[index]% 3 == 0:
#         liste.append(sayilar[index])
#         index+=1
#     else:
#         index+=1

for i in sayilar:
    if i%3 ==0:
        liste.append(i)

print("3'ün katı olan sayilar: ")
print(liste)

#2- sayilar listesindeki sayiların toplamı kaçtır?
total = 0
for i in sayilar:
    total +=i
print(f"Sayıların toplamı: {total}")

#3- sayilar listsindeki tek sayiların karesini alıp yazdır
liste = []
index = 0
for i in sayilar:
    if i%2 != 0:
        temp = i**2
        liste.append(temp)
print("Teklerin kareleri: ")
print(liste)



#4- şehirlerin hangileri en fazla 5 karakterlidir?
cities = ["istanbul","ankara","izmir","bursa"]
# print(cities.__len__())
# print(cities[0].__len__())
# yada len(cities) | len(cities[0])
liste = []
for city in cities:
    if city.__len__()<=5:
        liste.append(city)
print(f"max 5 harfli olan iller:{liste}")



# 5- Ürünlerin fiyatları toplamı nedir ?
urunler = [
    {'name':'samsung S6', 'price': '3000' },
    {'name':'samsung S7', 'price': '4000' },
    {'name':'samsung S8', 'price': '5000' },
    {'name':'samsung S9', 'price': '6000' },
    {'name':'samsung S10', 'price': '7000' }
]
urunToplam =0
for urun in urunler:
    urunToplam+=int(urun["price"])
print(urunToplam)

# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz ?
liste = []
for urun in urunler:
    if int(urun['price'])<=5000:
        liste.append(urun["name"])
print(liste)
