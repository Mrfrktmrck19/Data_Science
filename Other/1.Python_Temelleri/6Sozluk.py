    ##Key-Value Pairing (Anahtar-Değer Eşleşmesş)

Sozluk={"AnahtarKelime":"Deger"}
print(type(Sozluk))  ##dict tipinde döner

print(Sozluk) ## {'AnahtarKelime': 'Deger'} şeklinde ekrana basar


caloriDict={"elma":100,"karpuz":200,"muz":300}
print(caloriDict["elma"]) ##100 basar

caloriDict["elma"]=150 # mutable 


dict2={1:"ömer",2:"faruk",3:"tomurcuk","as":4,5:4,"asd":[1,5,7]} ##böyle fantastik dict'ler tasarlayabilirsin
##Ancak keys kısmına list tanımlayamazsın

print(caloriDict.keys())
print(dict2["asd"][0])