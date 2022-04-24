        ##İleri Seviye İşlemler
    ##zip, listeleri birleştiriyor ve ayrı tuple'lara atıyor.
yemekListesi=["muz","ananas","elma"]
kaloriListesi=[100,200,300]
gunListesi=["Çarşamba","Periembe","Cuma"]
print(zip(yemekListesi,kaloriListesi,gunListesi))
print(list(zip(yemekListesi,kaloriListesi,gunListesi)))

#======================================================
listOrnek=[]
for harf in "Ömer Faruk Tomurcuk":
    listOrnek.append(harf)

print(listOrnek)


isimString="Ömer Faruk Tomurcuk"
yeniListe=[eleman for eleman in isimString] ##Böyle de bir yol var.
print(yeniListe)


yeniListe2=[eleman*5 for eleman in list(range(10))]
print(yeniListe2)
##Diyorki, 0 dan 9 a kadar liste oluştur her birini 5 ile çaro