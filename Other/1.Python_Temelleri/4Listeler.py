    ##Listeler-Collection
isimString="Ömer Faruk Tomurcuk"
##immutability/Değişmezlik-mutable/değişebilirlik
"""
isimStrind[0]="A"
gibi bir değiştirme yanlıştır. Python'da stringler değiştirilemez.
Çünkü böyle tasarlanmışlardır. Ancak listeler böyle değildir.
"""
numList=[10,20,30,40,50]
print(type(numList))    ##liste olduğuu görebilirsin.

num1=10
num2=20
numList2=[num1,num2]
numList2[0]=100 ##değiştirilebilirlik özelliği
numList2[0]+=10 ##değiştirilebilirlik özelliği,farklı bir açı



    ##Listeler'de Methotlar
numList.append(60) ##60 değerini listeye ekledi

numList.clear()  ##tüm listeyi temizler

print(numList)

print("==================")

sayilar=[10,20,30,40,50]

sayilar.pop(0) 
"""
Pop
default(yani index vermezsen) sondakini atar ve atarken return eder,
eğer index girersen de girdiğin indexteki değeri atar ve atarken
return eder.
"""
print(sayilar)

##sayilar.remove(10)
"""
Remove
bunun içine de değeri girmen gerekiyor, default değer almıyor.
Ayrıca attığı indexteki değeri geri döndürmüyor pop'taki gibi.
"""

sayilar.count(20)
"""
Count
Bir dizinin içerisinde, parametre olarak verilen değerden
kaç adet olduğunu bulmaya yarar.
"""
print(sayilar)
sayilar.append(10)

isimList1=["Ömer","Arslan","Umut"]
isimList2=["Atilla","Mustafa","Furkan"]
isimList=isimList1+isimList2    ##iki listeyi birleştiriyor
##isimList=isimList*5     ##5 kere tekrarlıyor
isimList.reverse() ##listeyi ters çeviriyor