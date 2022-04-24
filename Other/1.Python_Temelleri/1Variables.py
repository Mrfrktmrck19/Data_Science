    ##Variables-Değişkenler
"""
1.Python interpreter bir dil olduğu için değişken tipini 
başta belirtmemize gerek yok. 
2.Bir değişkeni yazıp nokta koyduğumuzda o değişkenin sahip
olduğu fonksyonları görürüz. Çünkü pythonda da her şey
bir nesnedir.
3.Pythonda 2 int bölüneceği zaman sonuç float çıkacaksa 
ekrana da float bastırır. Kendisi otomatik convert eder.

Not: Python çok esnek bir dil. Programlarkende farkedeceksin çoğu
şeyi senin yapmana gerek kalamdan o yapacak. Zaten pythonun amacı
oturup 2 saat program algoritması çıkartmak değil, AI, ML, DL gibi
alanlarda kodlamayı sağlayıp detaylardan kurtarmaktır.

4.CMD ekranından python kodu derleme
py dosya_adi.py
"""

greeting = "Selam"

print(greeting)

print(type(greeting))


    ##Matematiksel İşlemler
print(5**4)  ##5 üzeri 4
print(5%4)  ##Remainder-Kalanı bulma

    ##Kullanıcıdan veri alma
kullaniciYas=input("Yaşınızı giriniz: ")
print(kullaniciYas)
"""
Not:Kullanıcıdan veri almamızı sağlayan input fonksyonu,
aldığı veriyi string olarak alır. Yapacağın işleme göre
convert etmelisin.

Not 2: Öncesinden int olarak tanımladığımız bir değişkene
daha sonradan bir float string vs ataması yapabiliriz ve 
convert etmemize de gerek yok. Python gene bir şeyler deniyor.
Örn:
x=20  Burada int
x="asdasd" Burada str
x=12,5 burada float
"""

x="selamlar ben omer"

x=x.capitalize()  ##Cümlenin ilk harfini büyük yazar
print(x)

x=x.find("l")   ##stringde l harfinin ilk kaçıncı indiste olduğunu döndürür
print(x) ##burada x'i int'e çevirdi

y="ömer faruk tomurcuk"
print(y.split())    ##boşluklara göre ayırıp diziyeatacak

##Stringler de çarpma
x= "ömer"
x=x*4 ## 4 tane ömer stringini yanyana dizecek
print(x)

##String'ten int'e convert
sayiStringi="33"
sayiStringi=int(sayiStringi)    ##int'e çevrilip atanacak.
print(sayiStringi)
print(type(sayiStringi))

##Alt satıra geçme kaçış operatörü
print("Ömer Faruk\nTomurcuk")