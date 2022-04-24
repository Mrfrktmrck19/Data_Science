    ## map fonction
def bolme(num):
    return num/2
myList=[0,1,2,3,4,5,6,7,8,9]

print(map(bolme,myList))
print(list(map(bolme,myList)))
## Bir fonksiyon ve listeyi aldı. Listeyi Parametre olarak atadı.
##geriye ya tek değer döndrür ya da liste.

isim="Ömer Faruk"
def control(isim):
    return "a" in isim
print(control(isim))

isimList=["Ömer","Umut","Batu","Özgür","Arslan","Merve"]
print(list(map(control,isimList)))
sonucListesi=list(map(control,isimList))
##böyle ataya dabilirsin
print(sonucListesi.count(False))


    ##Filter
##True değerlerin değerlerini döndürecek. Liste döndürür.
print(list(filter(control,isimList)))

    ##lambda -Fonksiyonları tek satırda yazmak gibi bir şey
carpma= lambda numara: numara*3
##Geriye değer döndürür (return fonksiyo yani)
print(carpma(10))



sayiList=[10,20,30,40]
print(list(map(carpma,sayiList)))