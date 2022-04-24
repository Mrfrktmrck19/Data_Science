    ##Set
myList=[1,2,3,1,2,3]
"""
1.Set'in en büyük özelliği; içerisinde bir elemanı birden
fazla kez bulundurmaz. Listler buna izin verir ancak set
izin vermez.
2.Bir veri tipini başka bir şeye çevirmeye casting denir.
"""
mySetList=set(myList)   ##Listeyi set'e çevirdik(cast ettik).

print(mySetList)    ##tekrar eden değerler çıkartılacak

mySet={"a","b","c","c"} ##hata döndürmez ama bir tane c'yi siler ve cab sırasıyla bastırır ekrana.

print(mySet)

emptyList=[] ##type'ı list
emptySet={}  ##type'ı Dict olarak döner
emptySet["anahtarkelime"]=10
print(emptySet["anahtarkelime"])## gördüğün gibi dict oldu.

reallyEmptySet= set() ## asıl boş set böyle tanımlanır.

benimBosListem=list() ##tabi bular da denenebilinir.