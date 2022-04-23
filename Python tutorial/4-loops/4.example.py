from itertools import product

"""
sayilar = [1,2,3,4,5,6,7,8,9]

#1- sayilar listesini while ile ekrana yazdir
x=0
while x<len(sayilar):
    print(sayilar[x])
    x+=1


#2-başlangıç ve bitiş değerleini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın
a = int(input("Başlangıç değeri: "))
b = int(input("Bitiş değeri: "))

while a<=b:
    print(a)
    a+=1

#3- 1-100 arası sayıları azalan biçimdeyazdırın
b =100
while b>0:
    print(b)
    b-=1

#4- kullanıcıdan alacağınız 5 sayıyı sıralı bir şekilde ekrana yazdırım
liste = []
while len(liste) <5:
    liste.append(int(input("bir sayı giriniz: ")))
liste.sort()
print(liste)
"""
#5- Kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesi içinde sakla.
    ##ürün sayısını kullanıcıya sor
    ##dictionary listesi yapısı şeklinde olsun (name,price)
    ##ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listele

numberofProduct = int(input("Ekleyeceğiniz ürün sayısını giriniz: "))
productList = []
while numberofProduct>0:
    productName = input("Ürün adı: ")
    productPrice = float(input("Ürün fiyatı: "))
    productDict = {productName:productPrice}
    productList.append(productDict)
    numberofProduct-=1

temp = len(productList)
while temp>0:
    print(productList[temp-1])
    temp-=1

