    #For Loop - For Döngüsü
mylist=[0,1,2,3,4,5,6,7,8,9]
for num in mylist:
    print(num)
print("Loop ended")

for num in mylist:
    print(num/5)
print("Loop ended")

for num in mylist:
    if num%2==0:    ##Çiftleri yazdıracağız.
        print(num)
print("Loop ended")
#=============================================================
isim="Ömer Faruk Tomurcuk"
for harf in isim:
    print(harf)
#=============================================================
kordinat=[(36,42),(26,45)]
for eleman in kordinat:
    print(eleman)   ##Tuple döndürür
for (x,y) in kordinat:
    print(x,y)
#=============================================================
weirdList=[(1,2,3),(4,5,6),(7,8,9)]
for (x,y,z) in weirdList:
    print(z)
#=============================================================
sozluk={"muz":100,"armut":200,"karpuz":250}
print(sozluk.items())## ayırıp gruplandırıyor 

for (anahtar,deger) in sozluk.items():
    print("anahtar:"+anahtar+" deger:"+str(deger))